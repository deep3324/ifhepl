from django.contrib.auth.models import User
from django.db import models
from EmployeeProfile.models import EmployeeProfile
from ifheplapp.models import Jobs

# Create your models here.

class job_application(models.Model):
    # =============== Personal Details =======================
    # =============== Step 1 =======================
    applied_for = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    employee_profile = models.OneToOneField(EmployeeProfile, on_delete=models.CASCADE, related_name='job_application', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_application')
    name = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    mobile_number = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    # =============== Step 2 =======================
    alt_mobile_no = models.CharField(max_length=100, default="", blank=True)
    father_Husband_name = models.CharField(max_length=100, default="",blank=True)
    mother_name = models.CharField(max_length=100, default="",blank=True)
    category = models.CharField(max_length=100, default="", blank=True)
    disability = models.CharField(max_length=100, default="", blank=True)
    aadhar_no = models.CharField(max_length=12, default="", blank=True)
    pan_no = models.CharField(max_length=100, default="",blank=True)
    bloodgroup = models.CharField(max_length=100, default="",blank=True)
    gender = models.CharField(max_length=100, default="",blank=True)
    # =========================== Address ===========================
    village = models.CharField(max_length=100, default="",blank=True)
    po = models.CharField(max_length=100, default="",blank=True)
    ps = models.CharField(max_length=100, default="",blank=True)
    block = models.CharField(max_length=100, default="",blank=True)
    district = models.CharField(max_length=100, default="",blank=True)
    state = models.CharField(max_length=100, default="",blank=True)
    pin_code = models.CharField(max_length=100, default="",blank=True)
    # =========================== Matriculation ===========================
    matriculation_board_university = models.CharField(max_length=100, default="",blank=True)
    matriculation_school_institute = models.CharField(max_length=100, default="",blank=True)
    matriculation_passing_year = models.CharField(max_length=100, default="",blank=True)
    matriculation_roll_number = models.CharField(max_length=100, default="",blank=True)
    matriculation_marks_gpa = models.CharField(max_length=100, default="",blank=True)
    matriculation_percentage = models.CharField(max_length=100, default="",blank=True)
    # =========================== Intermediate ===========================
    intermediate_board_university = models.CharField(max_length=100, default="",blank=True)
    intermediate_school_institute = models.CharField(max_length=100, default="",blank=True)
    intermediate_passing_year = models.CharField(max_length=100, default="",blank=True)
    intermediate_roll_number = models.CharField(max_length=100, default="",blank=True)
    intermediate_marks_gpa = models.CharField(max_length=100, default="",blank=True)
    intermediate_percentage = models.CharField(max_length=100, default="",blank=True)
    # =========================== Graduation ===========================
    graduation_board_university = models.CharField(max_length=100, default="",blank=True)
    graduation_school_institute = models.CharField(max_length=100, default="",blank=True)
    graduation_passing_year = models.CharField(max_length=100, default="",blank=True)
    graduation_roll_number = models.CharField(max_length=100, default="",blank=True)
    graduation_marks_gpa = models.CharField(max_length=100, default="",blank=True)
    graduation_percentage = models.CharField(max_length=100, default="",blank=True)
    # =========================== Higher Qualification ===========================
    higher_qualification_board_university = models.CharField(max_length=100, default="",blank=True)
    higher_qualification_school_institute = models.CharField(max_length=100, default="",blank=True)
    higher_qualification_passing_year = models.CharField(max_length=100, default="",blank=True)
    higher_qualification_roll_number = models.CharField(max_length=100, default="",blank=True)
    higher_qualification_marks_gpa = models.CharField(max_length=100, default="",blank=True)
    higher_qualification_percentage = models.CharField(max_length=100, default="",blank=True)
    # =========================== Higher Qualification ===========================
    extra_qualification_board_university = models.CharField(max_length=100, default="",blank=True)
    extra_qualification_school_institute = models.CharField(max_length=100, default="",blank=True)
    extra_qualification_passing_year = models.CharField(max_length=100, default="",blank=True)
    extra_qualification_roll_number = models.CharField(max_length=100, default="",blank=True)
    extra_qualification_marks_gpa = models.CharField(max_length=100, default="",blank=True)
    extra_qualification_percentage = models.CharField(max_length=100, default="",blank=True)
    # =========================== Document Upload ===========================
    sign = models.FileField(upload_to="Job/Signature/", blank=True)
    photo = models.FileField(upload_to="Job/Image/", blank=True)
    submitted_on = models.DateField()
    # =========================== Status ===========================
    completed = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    reference_number = models.CharField(
        max_length=20, default="")
    # =========================== payment Update ===========================
    order_id = models.CharField(max_length=100, default="")
    paid = models.BooleanField(default=False)
    razorpay_signature = models.CharField(max_length=100, default="")
    razorpay_payment_id = models.CharField(max_length=100, default="")
    transaction_date = models.CharField(max_length=100, default="")
    payment_status = models.CharField(max_length=100, default="")
    payment_mode = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name + " (" + self.reference_number + ")"
