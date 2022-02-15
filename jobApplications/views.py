from django.contrib import messages
import ifheplapp
import random
from django.contrib.auth import authenticate,  login as dj_login, logout
from django.shortcuts import render
from datetime import timedelta, datetime
from django.shortcuts import redirect, render
from ifheplapp.models import Jobs
from ifheplapp.utils import random_string_generator
from jobApplications.models import job_application
from django.contrib.auth.models import User
from django.template.loader import render_to_string
# Create your views here.


def complete_profile(request):
    job_profile = job_application.objects.get(user=request.user)
    if request.method == "POST" and request.FILES:
        job_profile.alt_mobile_no = request.POST.get('alt_mobile_no')
        job_profile.father_Husband_name = request.POST.get('father_name')
        job_profile.mother_name = request.POST.get('mother_name')
        job_profile.category = request.POST.get('category')
        job_profile.disability = request.POST.get('disability')
        job_profile.pan_no = request.POST.get('pan_number')
        job_profile.aadhar_no = request.POST.get('aadhar_number')
        job_profile.village = request.POST.get('village')
        job_profile.bloodgroup = request.POST.get('bloodgroup')
        job_profile.po = request.POST.get('po')
        job_profile.ps = request.POST.get('ps')
        job_profile.district = request.POST.get('district')
        job_profile.block = request.POST.get('block')
        job_profile.state = request.POST.get('state')
        job_profile.pin_code = request.POST.get('pin_code')
        job_profile.matriculation_board_university = request.POST.get('mb')
        job_profile.matriculation_school_institute = request.POST.get('ms')
        job_profile.matriculation_passing_year = request.POST.get('mp')
        job_profile.matriculation_roll_number = request.POST.get('mr')
        job_profile.matriculation_marks_gpa = request.POST.get('mm')
        job_profile.matriculation_percentage = request.POST.get('mpe')
        job_profile.intermediate_board_university = request.POST.get('ib')
        job_profile.intermediate_school_institute = request.POST.get('is')
        job_profile.intermediate_passing_year = request.POST.get('ip')
        job_profile.intermediate_roll_number = request.POST.get('ir')
        job_profile.intermediate_marks_gpa = request.POST.get('im')
        job_profile.intermediate_percentage = request.POST.get('ipe')
        job_profile.graduation_board_university = request.POST.get('gb')
        job_profile.graduation_school_institute = request.POST.get('gs')
        job_profile.graduation_passing_year = request.POST.get('gp')
        job_profile.graduation_roll_number = request.POST.get('gr')
        job_profile.graduation_marks_gpa = request.POST.get('gm')
        job_profile.graduation_percentage = request.POST.get('gpe')
        job_profile.higher_qualification_board_university = request.POST.get(
            'hb')
        job_profile.higher_qualification_school_institute = request.POST.get(
            'hs')
        job_profile.higher_qualification_passing_year = request.POST.get('hp')
        job_profile.higher_qualification_roll_number = request.POST.get('hr')
        job_profile.higher_qualification_marks_gpa = request.POST.get('hm')
        job_profile.higher_qualification_percentage = request.POST.get('hpe')
        job_profile.extra_qualification_board_university = request.POST.get(
            'eb')
        job_profile.extra_qualification_school_institute = request.POST.get(
            'es')
        job_profile.extra_qualification_passing_year = request.POST.get('ep')
        job_profile.extra_qualification_roll_number = request.POST.get('er')
        job_profile.extra_qualification_marks_gpa = request.POST.get('em')
        job_profile.extra_qualification_percentage = request.POST.get('epe')
        job_profile.sign = request.FILES['sign']
        job_profile.photo = request.FILES['photo']
        job_profile.completed = True
        job_profile.order_id = random_string_generator(
        ) + "_" + job_profile.reference_number.lower()
        job_profile.save()
        msg = "succ-msg-job"
        return render(request, "confirmation.html", {'data_ref_job': job_profile, "msg": msg})
    return render(request, "complete_profile.html", {"job": job_profile})


def job_submit(request):
    if request.method == 'POST':
        applied_for = Jobs.objects.get(slug=request.POST.get('applied_for'))
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")
                                                 [0]) + str(int(random.random() * 10000)) + "J"
        subject = render_to_string(
            'email/confirmation_job.html', {'name': name, 'request_no': reference_number, "email": email, "dob": str(dob).replace("-", "")})
        user = User.objects.create_user(
            username=email,
            email=email,
            password=str(dob).replace("-", ""),
            first_name=str(name.split(" ")[0]),
        )
        user.save()
        user = authenticate(username=email, password=str(dob).replace("-", ""))
        dj_login(request, user)
        request.session.set_expiry(0)
        job = job_application(
            reference_number=reference_number,
            user=request.user,
            applied_for=applied_for,
            name=name,
            dob=dob,
            mobile_number=mobile_number,
            email=email,
            submitted_on=datetime.today())
        prev_data_job = job_application.objects.all()
        for data_job in prev_data_job:
            if job.id_proof == data_job.id_proof:
                messages.error(
                    request, "Your application has been already Submitted")
                return redirect('/career')
        else:
            job.save()
            ifheplapp.def_mail("Job Application | IFHEPL", subject, email)
            ifheplapp.send_sms_job_submission(
                mobile_number, reference_number, "https://ifhepl.in/login")
            data_ref_job = job_application.objects.get(email=job.email)
            return render(request, "confirmation.html", {'data_ref_job': data_ref_job})
    else:
        return redirect('/career')
