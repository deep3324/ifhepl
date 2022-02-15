import random
from django.shortcuts import render
from ifheplapp import verify_recaptcha
import ifheplapp
from django.template.loader import render_to_string
from ifheplapp.utils import random_string_generator
from vendorApplication.models import vendorApplication
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.


def vendor_submit(request):
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
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        marital_status = request.POST.get('marital_status')
        language_known = request.POST.get('language_known')
        occupation = request.POST.get('occupation')
        nominee_name = request.POST.get('nominee_name')
        work_area = request.POST.get('work_area')
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
        photo = request.FILES['photo']
        signature = request.FILES['signature']
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")
                                                 [0]) + str(int(random.random() * 10000)) + "V"
        subject = render_to_string(
            'email/confirmation_vendor.html', {'name': name, 'request_no': reference_number})
        order_id = random_string_generator() + "_" + reference_number.lower()
        vendor = vendorApplication(
            reference_number=reference_number,
            name=name,
            dob=dob,
            idtype=idtype,
            id_proof=id_proof,
            father_Husband_name=father_name,
            mother_name=mother_name,
            category=category,
            disability=disability,
            gender=gender,
            religion=religion,
            marital_status=marital_status,
            language_known=language_known,
            occupation=occupation,
            nominee_name=nominee_name,
            work_area=work_area,
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
            paid=False,
            photo=photo,
            signature=signature,
            order_id=order_id,
            accept_terms=True,
            submitted_on=datetime.today())
        prev_data = vendorApplication.objects.all()
        for data in prev_data:
            if vendor.id_proof == data.id_proof:
                messages.error(
                    request, "Your application has been already Submitted")
                return redirect('/vendor-registration')
        verified_recaptcha = verify_recaptcha(
            request.POST.get('g-recaptcha-response'))
        if verified_recaptcha:
            vendor.save()
            msg = "succ-msg-ven"
            ifheplapp.def_mail(
                "Vendor Registration | IFHEPL", subject, email)
            ifheplapp.send_sms_vendor_submission(
                mobile_number, vendor.reference_number, "ifhepl.in/verify-vendor")
            data_ref = vendorApplication.objects.get(
                id_proof=vendor.id_proof)
            return render(request, "confirmation.html", {'data_ref_vendor': data_ref if data_ref else "", "msg": msg})
        else:
            return render(request, "captcha_error.html")
