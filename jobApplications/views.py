from django.shortcuts import render
from datetime import timedelta, datetime
from django.shortcuts import redirect, render
from ifheplapp.models import Jobs
from jobApplications.models import job_application
from django.contrib.auth.models import User

# Create your views here.


def job_submit(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('email'), email=request.POST.get(
            'email'),  password=str(request.POST.get('dob')).replace("/", ""))
        user.save()
        applied_for = Jobs.objects.get(slug=request.POST.get('applied_for'))
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        reference_number = "IFHE" + \
            (name.split(" ")[0].upper())[0:4] + (dob.split("-")[0]) + "J"
        job = job_application(
            reference_number=reference_number,
            user=user,
            applied_for=applied_for,
            name=name,
            dob=dob,
            mobile_number=mobile_number,
            email=email,
            submitted_on=datetime.today())
        prev_data_job = job_application.objects.all()
        for data_job in prev_data_job:
            if job.email == data_job.email:
                return redirect('/career')
        else:
            job.save()
            data_ref_job = job_application.objects.get(email=job.email)
            return render(request, "confirmation.html", {'data_ref_job': data_ref_job})
    else:
        return redirect('/career')

