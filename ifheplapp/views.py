from ifheplapp import convert_to_html
from datetime import timedelta, datetime
from django.db.models.query_utils import Q
from django.http import HttpResponse
import ifheplapp
from ifheplapp.models import AssociatePartner, Attendance, Contact, Gallery, HealthCard, KisanCard, Membership, Jobs, JobApply, Notice, Slider
from EmployeeProfile.models import EmployeeProfile
from django.shortcuts import redirect, render
from django.template.loader import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,  login as dj_login, logout
from django.contrib import messages
from geopy.geocoders import Nominatim
import pytz


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
    for i in profile:
        kisan_count = len(KisanCard.objects.filter(employeeID=i.emmloyeeid))
        kisan_count = kisan_count if kisan_count else 0
        membership_count = len(
            Membership.objects.filter(employeeID=i.emmloyeeid))
        membership_count = membership_count if membership_count else 0
        health_count = len(HealthCard.objects.filter(employeeID=i.emmloyeeid))
        health_count = health_count if health_count else 0
    return render(request, "profile.html", {"profile": profile, "kisan_count": kisan_count, "membership_count": membership_count, "health_count": health_count})


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            if user.is_active:
                dj_login(request, user)
                request.session.set_expiry(0)
                messages.success(request, "Successfully Logged In")
                return redirect("/profile")
        else:
            msg = "err-msg-login"
            return render(request, "login.html", {"msg": msg})


def handelLogout(request):
    logout(request)
    return redirect('/')


def kisan_card(request):
    return render(request, "kisan_card.html")


@login_required(login_url='/login')
def kisan_card_apply(request):
    return render(request, "kisan_card_apply.html")


def health_card(request):
    return render(request, "health_card.html")


@login_required(login_url='/login')
def health_card_apply(request):
    return render(request, "health_card_apply.html")


def reachus(request):
    return render(request, "reachus.html")


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
            return render(request, "viewDetails.html", {'membership_reference': "", "membership_card": ""})


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
            return render(request, "viewDetails.html", {'kisan_reference': "", "kisan_card": ""})


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
            return render(request, "viewDetails.html", {'Health_reference': "", "Health_card": ""})


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


@login_required(login_url='/login')
def membership(request):
    return render(request, "membership.html")


def comingsoon(request):
    return render(request, "coming_soon.html")


def career(request):
    jobs = Jobs.objects.all()
    return render(request, "career.html", {'jobs': jobs})


def careerApply(request, slug):
    jobs = Jobs.objects.filter(slug=slug)
    return render(request, "career_apply.html", {'jobs': jobs})


def membership_submit(request):
    emp = EmployeeProfile.objects.filter(user=request.user)
    empid = emp[0].emmloyeeid
    empname = emp[0].name
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
        ipdoc = request.FILES['ipdoc']
        photo = request.FILES['imgs']
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")[0]) + "M"
        subject = render_to_string(
            'email/confirmation.html', {'name': name, 'scheme': 'Membership', 'request_no': reference_number})
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
            photo=photo,
            submitted_on=datetime.today())
        prev_data = Membership.objects.all()
        for data in prev_data:
            if membership.id_proof == data.id_proof:
                messages.error(
                    request, "Your application has been already Submitted")
                return redirect('/membership')
        else:
            membership.save()
            msg = "succ-msg-mem"
            ifheplapp.def_mail("Membership | IFHEPL", subject, email)
            data_ref = Membership.objects.filter(id_proof=membership.id_proof)
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
            emp.save()
            return render(request, "confirmation.html", {'data_ref': data_ref, "msg": msg})


def kisan_submit(request):
    emp = EmployeeProfile.objects.filter(user=request.user)
    empid = emp[0].emmloyeeid
    empname = emp[0].name
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
        ipdoc = request.FILES['ipdoc']
        photo = request.FILES['imgs']
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")[0]) + "K"
        subject = render_to_string(
            'email/confirmation.html', {'name': name, 'scheme': 'Kisan', 'request_no': reference_number})
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
            photo=photo,
            submitted_on=datetime.today())
        prev_data = KisanCard.objects.all()
        for data in prev_data:
            if kisan.id_proof == data.id_proof:
                messages.error(
                    request, "Your application has been already Submitted")
                return redirect('/card/Kisan-Card')
        else:
            kisan.save()
            msg = "succ-msg-kis"
            ifheplapp.def_mail("Kisan Card | IFHEPL", subject, email)
            data_ref = KisanCard.objects.filter(id_proof=kisan.id_proof)
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
            emp.save()
            return render(request, "confirmation.html", {'data_ref_kisan': data_ref, "msg": msg})


def health_submit(request):
    emp = EmployeeProfile.objects.filter(user=request.user)
    empid = emp[0].emmloyeeid
    empname = emp[0].name
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
        ipdoc = request.FILES['ipdoc']
        photo = request.FILES['imgs']
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")[0]) + "H"
        subject = render_to_string(
            'email/confirmation.html', {'name': name, 'scheme': 'Health', 'request_no': reference_number})
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
            submitted_on=datetime.today())
        prev_data = HealthCard.objects.all()
        for data in prev_data:
            if health.id_proof == data.id_proof:
                messages.error(
                    request, "Your application has been already Submitted")
                return redirect('/card/Health-Card')
        else:
            health.save()
            msg = "succ-msg-hel"
            ifheplapp.def_mail("Health Card | IFHEPL", subject, email)
            data_ref = HealthCard.objects.filter(id_proof=health.id_proof)
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
            emp.save()
            return render(request, "confirmation.html", {'data_ref_health': data_ref, "msg": msg})


def job_submit(request):
    if request.method == 'POST' and request.FILES:
        applied_for = request.POST.get('applied_for')
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
        board_10 = request.POST.get('board_10')
        school_10 = request.POST.get('school_10')
        passing_10 = request.POST.get('passing_10')
        roll_10 = request.POST.get('roll_10')
        mark_10 = request.POST.get('mark_10')
        percentage_10 = request.POST.get('percentage_10')
        board_12 = request.POST.get('board_12')
        school_12 = request.POST.get('school_12')
        passing_12 = request.POST.get('passing_12')
        roll_12 = request.POST.get('roll_12')
        mark_12 = request.POST.get('mark_12')
        percentage_12 = request.POST.get('percentage_12')
        univ_graduation = request.POST.get('univ_graduation')
        insti_graduation = request.POST.get('insti_graduation')
        passing_graduation = request.POST.get('passing_graduation')
        roll_graduation = request.POST.get('roll_graduation')
        mark_graduation = request.POST.get('mark_graduation')
        percentage_graduation = request.POST.get('percentage_graduation')
        univ_master = request.POST.get('univ_master')
        insti_master = request.POST.get('insti_master')
        passing_master = request.POST.get('passing_master')
        roll_master = request.POST.get('roll_master')
        mark_master = request.POST.get('mark_master')
        percentage_master = request.POST.get('percentage_master')
        edudoc = request.FILES['edudoc']
        imgs = request.FILES['imgs']
        sign = request.FILES['sign']
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")[0]) + "J"
        job = JobApply(
            reference_number=reference_number,
            applied_for=applied_for,
            name=name,
            dob=dob,
            idtype=idtype,
            id_proof=id_proof,
            father_name=father_name,
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
            board_10=board_10,
            school_10=school_10,
            passing_10=passing_10,
            roll_10=roll_10,
            mark_10=mark_10,
            percentage_10=percentage_10,
            board_12=board_12,
            school_12=school_12,
            passing_12=passing_12,
            roll_12=roll_12,
            mark_12=mark_12,
            percentage_12=percentage_12,
            univ_graduation=univ_graduation,
            insti_graduation=insti_graduation,
            passing_graduation=passing_graduation,
            roll_graduation=roll_graduation,
            mark_graduation=mark_graduation,
            percentage_graduation=percentage_graduation,
            univ_master=univ_master,
            insti_master=insti_master,
            passing_master=passing_master,
            roll_master=roll_master,
            mark_master=mark_master,
            percentage_master=percentage_master,
            edudoc=edudoc,
            imgs=imgs,
            sign=sign,
            submitted_on=datetime.today())
        prev_data_job = JobApply.objects.all()
        for data_job in prev_data_job:
            if job.email == data_job.email:
                return redirect('/career')
        else:
            job.save()
            data_ref_job = JobApply.objects.filter(email=job.email)
            return render(request, "confirmation.html", {'data_ref_job': data_ref_job})
