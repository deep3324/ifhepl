from .constants import PaymentStatus
import json
from django.contrib.auth.models import User
import random
import razorpay
from django.views.decorators.csrf import csrf_exempt
from ifheplapp import convert_to_html, verify_recaptcha
from datetime import timedelta, datetime
from django.db.models.query_utils import Q
import ifheplapp
from ifheplapp.models import AssociatePartner, Attendance, Contact, Gallery, HealthCard, KisanCard, Membership, Jobs, Notice, Order, Slider, Transaction
from django.conf import settings
from EmployeeProfile.models import EmployeeProfile
from django.shortcuts import redirect, render
from django.template.loader import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,  login as dj_login, logout
from django.contrib import messages
from geopy.geocoders import Nominatim
from ifheplapp.utils import filter_application_name, random_string_generator, fetch_card, regenerate_order_id

from jobApplications.models import job_application
from vendorApplication.models import vendorApplication


def offer_letter(request):
    html = render_to_string('includes/offer_letter.html', {'name': ""})
    convert_to_html(html)
    return render(request, "includes/offer_letter.html")


def index(request):
    notice = Notice.objects.all().order_by('-id')
    sliders = Slider.objects.all().order_by('-id')
    partners = AssociatePartner.objects.all().order_by('-id')
    return render(request, "index.html", {'notices': notice, 'sliders': sliders, 'partners': partners})


def aboutus(request):
    return render(request, "aboutus.html")


def ads(request):
    return render(request, "ads.txt")


"""
Set Time to show attendance submit
9:00-9:30
13:00-13:30
17:00-17:30
"""


@login_required(login_url='/login')
def attendance(request):
    return render(request, "attendance.html")


@login_required(login_url='/login')
def handleAttendance(request):
    emp = EmployeeProfile.objects.filter(user=request.user)
    for i in emp:
        empid = i.emmloyeeid
        empname = i.name
    if request.method == "POST" and request.FILES:
        geoLoc = Nominatim(user_agent="GetLoc")
        longitude = request.POST['longitude']
        lattitude = request.POST['lattitude']
        if longitude and lattitude:
            locname = geoLoc.reverse("{}, {}".format(lattitude, longitude))
            employeeID = empid
            employeeName = empname
            image = request.FILES['captureImage']
            location = locname.address
            attendance = Attendance(
                employeeID=employeeID, employeeName=employeeName, image=image, location=location)
            attendance.save()
            msg = "succ-msg-atn"
            return render(request, "index.html", {"msg": msg})
        else:
            msg = "alert-msg-loc"
            return render(request, "attendance.html", {"msg": msg})


def login(request):
    return render(request, "login.html")


@login_required(login_url='/login')
def profile(request):
    profile = EmployeeProfile.objects.filter(user=request.user)
    return render(request, "profile.html", {"profile": profile})


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername, password=loginpassword)
        if user and user.is_active:
            # if user.is_active:
            dj_login(request, user)
            request.session.set_expiry(0)
            messages.success(request, "Successfully Logged In")
            if loginusername.startswith("IFHEPLE1") or loginusername.startswith("IFHEPLV2"):
                return redirect("/profile")
            elif user.is_staff:
                return redirect("/admin")
            else:
                return redirect("/complete_profile")
        else:
            messages.warning(request, "Invalid Credentials, Please try again!")
            return redirect("/login")


def handelLogout(request):
    logout(request)
    return redirect('/')


def kisan_card(request):
    return render(request, "kisan_card.html")


# @login_required(login_url='/login')
def kisan_card_apply(request):
    if request.user.is_authenticated and (request.user.username.startswith("IFHEPLE1") or request.user.username.startswith("IFHEPLV2")):
        employee = EmployeeProfile.objects.get(user=request.user)
        return render(request, "kisan_card_apply.html", {"employee": employee if employee else ""})
    else:
        return render(request, "kisan_card_apply.html")


def health_card(request):
    return render(request, "health_card.html")


# @login_required(login_url='/login')
def health_card_apply(request):
    if request.user.is_authenticated and (request.user.username.startswith("IFHEPLE1") or request.user.username.startswith("IFHEPLV2")):
        employee = EmployeeProfile.objects.get(user=request.user)
        return render(request, "health_card_apply.html", {"employee": employee if employee else ""})
    else:
        return render(request, "health_card_apply.html")


def reachus(request):
    return render(request, "reachus.html")


def associate(request):
    associate_partners = AssociatePartner.objects.all().order_by('-id')
    return render(request, "associate.html", {'associate_partners': associate_partners})


def associate_view(request, slug):
    associate_partners = AssociatePartner.objects.get(slug=slug)
    return render(request, "associate_partner_view.html", {'partner': associate_partners})


def reachus_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, mobile=mobile, email=email,
                          message=message, contacted_on=datetime.today())
        contact.save()
    return redirect("/")


def privacypolicy(request):
    return render(request, "privacypolicy.html")


def pricing(request):
    return render(request, "pricing.html")


def vendor(request):
    return render(request, "vendor_appllication.html")


def returnpolicy(request):
    return render(request, "returnpolicy.html")


def termscondition(request):
    return render(request, "termscondition.html")


def cookiepolicy(request):
    return render(request, "cookiepolicy.html")


def gallery(request):
    images = Gallery.objects.all().order_by('-id')
    return render(request, "gallery.html", {'images': images})


def searchMembership(request):
    return render(request, "seach_membership.html")


def searchKisan(request):
    return render(request, "seach_kisan.html")


def searchHealth(request):
    return render(request, "seach_health.html")


def searchVendor(request):
    return render(request, "seach_vendor.html")


def viewVendor(request):
    if request.method == 'GET':
        query_reference = request.GET.get('query_reference')
        query_card_dob = request.GET.get('query_card_dob')
        if query_reference and query_card_dob:
            vendor = vendorApplication.objects.filter(
                Q(reference_number=query_reference) & Q(dob=query_card_dob))
            return render(request, "viewDetails.html", {'vendor': vendor[0] if vendor else ""})
        else:
            messages.warning(request,"Incorrect data, please try again")
            return redirect("/verify-vendor")


def viewMembership(request):
    if request.method == 'GET':
        query_reference = request.GET.get('query_reference')
        query_card = request.GET.get('query_card')
        query_card_dob = request.GET.get('query_card_dob')
        if query_reference:
            membership_reference = Membership.objects.filter(
                reference_number=query_reference)
            return render(request, "viewDetails.html", {'membership_reference': membership_reference[0] if membership_reference else ""})
        elif query_card and query_card_dob:
            membership_card = Membership.objects.filter(
                Q(card_number=query_card) & Q(dob=query_card_dob))
            return render(request, "viewDetails.html", {'membership_card': membership_card[0] if membership_card else ""})
        else:
            messages.warning(request,"Incorrect data, please try again")
            return redirect("/verify-membership")


def viewKisanCard(request):
    if request.method == 'GET':
        query_reference = request.GET.get('query_reference')
        query_card = request.GET.get('query_card')
        query_card_dob = request.GET.get('query_card_dob')
        if query_reference:
            kisan_reference = KisanCard.objects.filter(
                reference_number=query_reference)
            return render(request, "viewDetails.html", {'kisan_reference': kisan_reference[0] if kisan_reference else ""})
        elif query_card and query_card_dob:
            kisan_card = KisanCard.objects.filter(
                Q(card_number=query_card) & Q(dob=query_card_dob))
            return render(request, "viewDetails.html", {'kisan_card': kisan_card[0] if kisan_card else ""})
        else:
            messages.warning(request,"Incorrect data, please try again")
            return redirect("/verify-kisan")


def viewHealthCard(request):
    if request.method == 'GET':
        query_reference = request.GET.get('query_reference')
        query_card = request.GET.get('query_card')
        query_card_dob = request.GET.get('query_card_dob')
        if query_reference:
            Health_reference = HealthCard.objects.filter(
                reference_number=query_reference)
            return render(request, "viewDetails.html", {'Health_reference': Health_reference[0] if Health_reference else ""})
        elif query_card and query_card_dob:
            Health_card = HealthCard.objects.filter(
                Q(card_number=query_card) & Q(dob=query_card_dob))
            return render(request, "viewDetails.html", {'Health_card': Health_card[0] if Health_card else ""})
        else:
            messages.warning(request,"Incorrect data, please try again")
            return redirect("/verify-health")


def maintainance(request):
    return render(request, "maintainance.html")


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request, exception):
    return render(request, '500.html', status=500)


def rules_regulation(request):
    notices = Notice.objects.filter(notice_type="Rules & Regulation")
    return render(request, "notice.html", {'notices': notices})


def academic_notice(request):
    notices = Notice.objects.filter(notice_type="Academic Notice")
    return render(request, "notice.html", {'notices': notices})


def administrative_notice(request):
    notices = Notice.objects.filter(notice_type="Administrative Notice")
    return render(request, "notice.html", {'notices': notices})


def requirement_notice(request):
    notices = Notice.objects.filter(notice_type="Requirement Notice")
    return render(request, "notice.html", {'notices': notices})


# @login_required(login_url='/login')
def membership(request):
    if request.user.is_authenticated and (request.user.username.startswith("IFHEPLE1") or request.user.username.startswith("IFHEPLV2")):
        employee = EmployeeProfile.objects.get(user=request.user)
        return render(request, "membership.html", {"employee": employee if employee else ""})
    else:
        return render(request, "membership.html")


def print(request, order_id):
    card = fetch_card(order_id)
    return render(request, "includes/print_page.html", {"doc": card})


def comingsoon(request):
    return render(request, "coming_soon.html")


def career(request):
    jobs = Jobs.objects.all()
    return render(request, "career.html", {'jobs': jobs})


def careerApply(request, slug):
    jobs = Jobs.objects.get(slug=slug)
    return render(request, "career_apply.html", {'jobs': jobs})


def membership_submit(request):
    if request.user.is_authenticated:
        emp = EmployeeProfile.objects.filter(user=request.user)
        empid = emp[0].emmloyeeid if emp else ""
        empname = emp[0].name if emp else ""
    else:
        empid = ""
        empname = ""
    if request.method == 'POST' and request.FILES:
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        idtype = request.POST.get('idtype')
        id_proof = request.POST.get('id_proof1') or request.POST.get(
            'id_proof2') or request.POST.get('id_proof3') or request.POST.get('id_proof4')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        category = request.POST.get('category')
        disability = request.POST.get('disability')
        mobile_number = request.POST.get('mobile_number')
        alt_mobile_no = request.POST.get('alt_mobile_no')
        email = request.POST.get('email')
        village = request.POST.get('village')
        po = request.POST.get('po')
        ps = request.POST.get('ps')
        district = request.POST.get('district')
        block = request.POST.get('block')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin_code')
        payment = request.POST.get('payment')
        ipdoc = request.FILES['ipdoc']
        photo = request.FILES['imgs']
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")
                                                 [0]) + str(int(random.random() * 10000)) + "M"
        subject = render_to_string(
            'email/confirmation.html', {'name': name, 'scheme': 'Membership', 'request_no': reference_number})
        if payment == "cash":
            order_id = "CASH"
        else:
            order_id = random_string_generator() + "_" + reference_number.lower()
        membership = Membership(
            reference_number=reference_number,
            employeeID=empid,
            employeename=empname,
            name=name,
            dob=dob,
            idtype=idtype,
            id_proof=id_proof,
            father_Husband_name=father_name,
            mother_name=mother_name,
            category=category,
            disability=disability,
            mobile_number=mobile_number,
            alt_mobile_no=alt_mobile_no,
            email=email,
            village=village,
            po=po,
            ps=ps,
            district=district,
            block=block,
            state=state,
            pin_code=pin_code,
            id_proof_document=ipdoc,
            paid=True if payment == "cash" else False,
            photo=photo,
            order_id=order_id,
            submitted_on=datetime.today())
        prev_data = Membership.objects.all()
        for data in prev_data:
            if membership.id_proof == data.id_proof:
                messages.error(
                    request, "Your application has been already Submitted")
                return redirect('/membership')
        verified_recaptcha = verify_recaptcha(
            request.POST.get('g-recaptcha-response'))
        if verified_recaptcha:
            membership.save()
            msg = "succ-msg-mem"
            ifheplapp.def_mail("Membership | IFHEPL", subject, email)
            ifheplapp.send_sms_form_submission(
                mobile_number, "Membership", membership.reference_number, "ifhepl.in/verify-membership")
            data_ref = Membership.objects.filter(
                id_proof=membership.id_proof)
            if request.user.is_authenticated:
                emp = EmployeeProfile.objects.get(user=request.user)
                emp.total_membership_card_created = len(
                    Membership.objects.filter(employeeID=empid))
                curr_month = datetime.now().month
                emp.current_month_membership_card_created = len(
                    Membership.objects.filter(employeeID=empid, submitted_on__month=curr_month))
                prev_month = (datetime.now().replace(
                    day=1) - timedelta(days=1)).month
                emp.previous_month_membership_card_created = len(
                    Membership.objects.filter(employeeID=empid, submitted_on__month=prev_month))
                if membership.order_id == "CASH":
                    emp.cash_mode_total_membership_card_created = len(Membership.objects.filter(employeeID=empid, order_id = "CASH"))
                    curr_month = datetime.now().month
                    emp.cash_mode_current_month_membership_card_created = len(Membership.objects.filter(employeeID=empid, submitted_on__month=curr_month, order_id = "CASH"))
                    prev_month = (datetime.now().replace(day=1) - timedelta(days=1)).month
                    emp.cash_mode_previous_month_membership_card_created = len(Membership.objects.filter(employeeID=empid, submitted_on__month=prev_month, order_id = "CASH"))
                emp.save()
            return render(request, "confirmation.html", {'data_ref': data_ref, "msg": msg})
        else:
            return render(request, "captcha_error.html")


def kisan_submit(request):
    if request.user.is_authenticated:
        emp = EmployeeProfile.objects.filter(user=request.user)
        empid = emp[0].emmloyeeid if emp else ""
        empname = emp[0].name if emp else ""
    else:
        empid = ""
        empname = ""
    if request.method == 'POST' and request.FILES:
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        idtype = request.POST.get('idtype')
        id_proof = request.POST.get('id_proof1') or request.POST.get(
            'id_proof2') or request.POST.get('id_proof3') or request.POST.get('id_proof4')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        category = request.POST.get('category')
        disability = request.POST.get('disability')
        mobile_number = request.POST.get('mobile_number')
        alt_mobile_no = request.POST.get('alt_mobile_no')
        email = request.POST.get('email')
        village = request.POST.get('village')
        po = request.POST.get('po')
        ps = request.POST.get('ps')
        district = request.POST.get('district')
        block = request.POST.get('block')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin_code')
        payment = request.POST.get('payment')
        ipdoc = request.FILES['ipdoc']
        photo = request.FILES['imgs']
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")
                                                 [0]) + str(int(random.random() * 10000)) + "K"
        subject = render_to_string(
            'email/confirmation.html', {'name': name, 'scheme': 'Kisan', 'request_no': reference_number})
        if payment == "cash":
            order_id = "CASH"
        else:
            order_id = random_string_generator() + "_" + reference_number.lower()
        kisan = KisanCard(
            reference_number=reference_number,
            employeeID=empid,
            employeename=empname,
            name=name,
            dob=dob,
            idtype=idtype,
            id_proof=id_proof,
            father_Husband_name=father_name,
            mother_name=mother_name,
            category=category,
            disability=disability,
            mobile_number=mobile_number,
            alt_mobile_no=alt_mobile_no,
            email=email,
            village=village,
            po=po,
            ps=ps,
            district=district,
            block=block,
            state=state,
            pin_code=pin_code,
            id_proof_document=ipdoc,
            paid=True if payment == "cash" else False,
            photo=photo,
            order_id=order_id,
            submitted_on=datetime.today())
        prev_data = KisanCard.objects.all()
        for data in prev_data:
            if kisan.id_proof == data.id_proof:
                messages.error(
                    request, "Your application has been already Submitted")
                return redirect('/card/Kisan-Card')
        verified_recaptcha = verify_recaptcha(
            request.POST.get('g-recaptcha-response'))
        if verified_recaptcha:
            kisan.save()
            msg = "succ-msg-kis"
            ifheplapp.def_mail("Kisan Card | IFHEPL", subject, email)
            ifheplapp.send_sms_form_submission(
                mobile_number, "Kisan", kisan.reference_number, "https://ifhepl.in/verify-kisan")
            data_ref = KisanCard.objects.filter(id_proof=kisan.id_proof)
            if request.user.is_authenticated:
                emp = EmployeeProfile.objects.get(user=request.user)
                emp.total_kisan_card_created = len(
                    KisanCard.objects.filter(employeeID=empid))
                curr_month = datetime.now().month
                emp.current_month_kisan_card_created = len(KisanCard.objects.filter(
                    employeeID=empid, submitted_on__month=curr_month))
                prev_month = (datetime.now().replace(
                    day=1) - timedelta(days=1)).month
                emp.previous_month_kisan_card_created = len(
                    KisanCard.objects.filter(employeeID=empid, submitted_on__month=prev_month))
                if kisan.order_id == "CASH":
                    emp.cash_mode_total_kisan_card_created = len(
                        KisanCard.objects.filter(employeeID=empid, order_id = "CASH"))
                    curr_month = datetime.now().month
                    emp.cash_mode_current_month_kisan_card_created = len(KisanCard.objects.filter(
                        employeeID=empid, submitted_on__month=curr_month, order_id = "CASH"))
                    prev_month = (datetime.now().replace(
                        day=1) - timedelta(days=1)).month
                    emp.cash_mode_previous_month_kisan_card_created = len(
                        KisanCard.objects.filter(employeeID=empid, submitted_on__month=prev_month, order_id = "CASH"))
                emp.save()
            return render(request, "confirmation.html", {'data_ref_kisan': data_ref if data_ref else "", "msg": msg})
        else:
            return render(request, "captcha_error.html")


def health_submit(request):
    if request.user.is_authenticated:
        emp = EmployeeProfile.objects.filter(user=request.user)
        empid = emp[0].emmloyeeid if emp else ""
        empname = emp[0].name if emp else ""
    else:
        empid = ""
        empname = ""
    if request.method == 'POST' and request.FILES:
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        idtype = request.POST.get('idtype')
        id_proof = request.POST.get('id_proof1') or request.POST.get(
            'id_proof2') or request.POST.get('id_proof3') or request.POST.get('id_proof4')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        category = request.POST.get('category')
        disability = request.POST.get('disability')
        mobile_number = request.POST.get('mobile_number')
        alt_mobile_no = request.POST.get('alt_mobile_no')
        email = request.POST.get('email')
        village = request.POST.get('village')
        po = request.POST.get('po')
        ps = request.POST.get('ps')
        district = request.POST.get('district')
        block = request.POST.get('block')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin_code')
        payment = request.POST.get('payment')
        ipdoc = request.FILES['ipdoc']
        photo = request.FILES['imgs']
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")
                                                 [0]) + str(int(random.random() * 10000)) + "H"
        subject = render_to_string(
            'email/confirmation.html', {'name': name, 'scheme': 'Health', 'request_no': reference_number})
        if payment == "cash":
            order_id = "CASH"
        else:
            order_id = random_string_generator() + "_" + reference_number.lower()
        health = HealthCard(
            reference_number=reference_number,
            employeeID=empid,
            employeename=empname,
            name=name,
            dob=dob,
            idtype=idtype,
            id_proof=id_proof,
            father_Husband_name=father_name,
            mother_name=mother_name,
            category=category,
            disability=disability,
            mobile_number=mobile_number,
            alt_mobile_no=alt_mobile_no,
            email=email,
            village=village,
            po=po,
            ps=ps,
            district=district,
            block=block,
            state=state,
            pin_code=pin_code,
            id_proof_document=ipdoc,
            photo=photo,
            order_id=order_id,
            paid=True if payment == "cash" else False,
            submitted_on=datetime.today())
        prev_data = HealthCard.objects.all()
        for data in prev_data:
            if health.id_proof == data.id_proof:
                messages.error(
                    request, "Your application has been already Submitted")
                return redirect('/card/Health-Card')
        verified_recaptcha = verify_recaptcha(
            request.POST.get('g-recaptcha-response'))
        if verified_recaptcha:
            health.save()
            msg = "succ-msg-hel"
            ifheplapp.def_mail("Health Card | IFHEPL", subject, email)
            ifheplapp.send_sms_form_submission(
                mobile_number, "Health", health.reference_number, "https://ifhepl.in/verify-health")
            data_ref = HealthCard.objects.filter(id_proof=health.id_proof)
            if request.user.is_authenticated:
                emp = EmployeeProfile.objects.get(user=request.user)
                emp.total_health_card_created = len(
                    HealthCard.objects.filter(employeeID=empid))
                curr_month = datetime.now().month
                emp.current_month_health_card_created = len(
                    HealthCard.objects.filter(employeeID=empid, submitted_on__month=curr_month))
                prev_month = (datetime.now().replace(
                    day=1) - timedelta(days=1)).month
                emp.previous_month_health_card_created = len(
                    HealthCard.objects.filter(employeeID=empid, submitted_on__month=prev_month))
                if health.order_id == "CASH":
                    emp.cash_mode_total_health_card_created = len(
                        HealthCard.objects.filter(employeeID=empid, order_id="CASH"))
                    curr_month = datetime.now().month
                    emp.cash_mode_current_month_health_card_created = len(
                        HealthCard.objects.filter(employeeID=empid, submitted_on__month=curr_month, order_id="CASH"))
                    prev_month = (datetime.now().replace(
                        day=1) - timedelta(days=1)).month
                    emp.cash_mode_previous_month_health_card_created = len(
                        HealthCard.objects.filter(employeeID=empid, submitted_on__month=prev_month, order_id="CASH"))
                emp.save()
            return render(request, "confirmation.html", {'data_ref_health': data_ref, "msg": msg})
        else:
            return render(request, "captcha_error.html")


def initiate_payment(request, order_id):
    application_name = filter_application_name(order_id)
    if application_name:
        transaction = Transaction.objects.create(
            made_for=application_name["card_name"], order_id=order_id, amount=application_name["amount"])
        transaction.save()
        data = {"amount": application_name["amount"] * 100, "currency": "INR",
                "receipt": str(order_id), "payment_capture": '1'}
        razorpay_client = razorpay.Client(
            auth=(str(settings.RAZORPAY_ID), str(settings.RAZORPAY_SECRET)))
        payment = razorpay_client.order.create(data=data)
        transaction.razorpay_id = payment['id']
        transaction.status = payment['status']
        transaction.save()
        card = fetch_card(order_id)
        order = Order.objects.create(
            name=card.name, amount=application_name["amount"], provider_order_id=payment["id"]
        )
        order.save()
        return render(
            request,
            "payments/redirect.html",
            {
                "callback_url": "https://" + "ifhepl.in" + "/success/",
                "razorpay_key": settings.RAZORPAY_ID,
                "order": order,
                "card": card,
                "card_name": application_name["card_name"]
            },
        )
    return render(request, "payments/redirect.html")


def verify_signature(response_data):
    client = razorpay.Client(
        auth=(settings.RAZORPAY_ID, settings.RAZORPAY_SECRET))
    return client.utility.verify_payment_signature(response_data)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        if signature_id:
            order = Order.objects.get(provider_order_id=provider_order_id)
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()
            transaction = Transaction.objects.get(
                razorpay_id=provider_order_id)
            application_name = filter_application_name(
                transaction.order_id)
            card = fetch_card(transaction.order_id)
            if not verify_signature(request.POST):
                order.status = PaymentStatus.SUCCESS
                order.save()
                transaction.razorpay_payment_id = payment_id
                transaction.signature = signature_id
                transaction.save()
                razorpay_client = razorpay.Client(
                    auth=(settings.RAZORPAY_ID, settings.RAZORPAY_SECRET))
                payment_details = razorpay_client.payment.fetch(payment_id)
                card.transaction_date = transaction.made_on
                card.razorpay_signature = signature_id
                card.razorpay_payment_id = payment_id
                card.payment_mode = payment_details['method']
                card.payment_status = payment_details['status']
                card.paid = True
                if application_name['card_name'] == "Job Application":
                    card.completed = True
                    card.accept = True
                else:
                    card.approve = True
                    card.created = False
                    card.underprocess = False
                card.reject = False
                card.save()
                payment_details['transaction_date'] = card.transaction_date
                payment_details['order_id'] = card.order_id
                subject = render_to_string(
                    'email/payment_confirmation.html', {'name': card.name, 'scheme': application_name['card_name'], 'request_no': card.reference_number})
                if application_name['card_name'] == "Vendor Application":
                    vendor = vendorApplication.objects.get(
                        reference_number=card.reference_number)
                    vendor_id = "IFHEPLV2" + \
                        str(vendor.dob.split("-")[0]) + \
                        str(int(random.random() * 100))
                    check_vendor_user = User.objects.filter(
                        username=vendor_id).exists()
                    if check_vendor_user:
                        pass
                    else:
                        vendor_user = User.objects.create_user(
                            username=vendor_id,
                            email=vendor.email,
                            password=str(vendor.dob).replace("-", ""),
                            first_name=str(vendor.name.split(" ")[0]),
                        )
                        vendor_user.is_active = False
                        vendor_user.save()
                        vendor.VendorID = vendor_id
                        vendor.save()
                        employee = EmployeeProfile.objects.create(
                            emmloyeeid=vendor_id,
                            email=vendor.email,
                            user=vendor_user,
                            name=vendor.name,
                            phone_number=vendor.mobile_number,
                            gender=vendor.gender,
                            job_location="",
                            designation="Vendor",
                            bloodgroup=vendor.bloodgroup,
                            dob=vendor.dob,
                            Address=vendor.village + " " + vendor.bloodgroup + " " + vendor.po + " " + vendor.ps +
                            " " + vendor.district + " " + vendor.block +
                            " " + vendor.state + " " + vendor.pin_code,
                            image=vendor.photo
                        )
                        employee.save()
                if application_name['card_name'] == "Job Application":
                    payment_details['type'] = "JOB"
                    appli = job_application.objects.get(
                        reference_number=card.reference_number)
                    employee_id = "IFHEPLE1" + \
                        str(appli.dob.split("-")[0]) + \
                        str(int(random.random() * 100))
                    check_employee_user = User.objects.filter(
                        username=employee_id).exists()
                    if check_employee_user:
                        pass
                    else:
                        employee_user = User.objects.create_user(
                            username=employee_id,
                            email=appli.email,
                            password=str(appli.dob).replace("-", ""),
                            first_name=str(appli.name.split(" ")[0]),
                        )
                        employee_user.is_active = False
                        employee_user.save()
                    check_employee = EmployeeProfile.objects.filter(
                        emmloyeeid=employee_id).exists()
                    if check_employee:
                        pass
                    else:
                        employee = EmployeeProfile.objects.create(
                            emmloyeeid=employee_id,
                            email=appli.email,
                            user=employee_user,
                            name=appli.name,
                            phone_number=appli.mobile_number,
                            gender=appli.gender,
                            job_location="",
                            designation=appli.applied_for.title,
                            bloodgroup=appli.bloodgroup,
                            dob=appli.dob,
                            Address=appli.village + " " + appli.bloodgroup + " " + appli.po + " " + appli.ps +
                            " " + appli.district + " " + appli.block +
                            " " + appli.state + " " + appli.pin_code,
                            image=appli.photo
                        )
                        employee.save()
                        appli.employee_profile = employee
                        appli.save()

                else:
                    payment_details['type'] = "CARD"
                ifheplapp.def_mail(
                    "Payment Confirmation | IFHEPL", subject, card.email)
                return render(request, "confirmation.html", context={"received_data": payment_details})
            else:
                order.status = PaymentStatus.FAILURE
                order.save()
                regenerate_order_id(card)
                return render(request, "confirmation.html", context={"regenerate": card})
        else:
            payment_id = json.loads(request.POST.get(
                "error[metadata]")).get("payment_id")
            provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
                "order_id"
            )
            order = Order.objects.get(provider_order_id=provider_order_id)
            order.payment_id = payment_id
            order.status = PaymentStatus.FAILURE
            order.save()
            regenerate_order_id(card)
            return render(request, "confirmation.html", context={"regenerate": card})
