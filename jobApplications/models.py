from django.contrib.auth.models import User
from django.db import models
from ifheplapp.models import Jobs

# Create your models here.

class job_application(models.Model):
    # =============== Personal Details =======================
    # =============== Step 1 =======================
    applied_for = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_application')
    name = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    mobile_number = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    # =============== Step 2 =======================
    alt_mobile_no = models.CharField(max_length=100, default="", blank=True)
    category = models.CharField(max_length=100, default="", blank=True)
    disability = models.CharField(max_length=100, default="", blank=True)
    father_Husband_name = models.CharField(max_length=100, default="",blank=True)
    mother_name = models.CharField(max_length=100, default="",blank=True)
    aadhar_no = models.CharField(max_length=12, default="", blank=True)
    pan_no = models.CharField(max_length=100, default="",blank=True)
    # =========================== Address ===========================
    village = models.CharField(max_length=100, default="",blank=True)
    po = models.CharField(max_length=100, default="",blank=True)
    ps = models.CharField(max_length=100, default="",blank=True)
    block = models.CharField(max_length=100, default="",blank=True)
    district = models.CharField(max_length=100, default="",blank=True)
    state = models.CharField(max_length=100, default="",blank=True)
    pin_code = models.CharField(max_length=100, default="",blank=True)
    # =========================== Matriculation ===========================
    board_10 = models.CharField(max_length=100, default="", blank=True)
    school_10 = models.CharField(max_length=100, default="", blank=True)
    passing_10 = models.CharField(max_length=100, default="", blank=True)
    roll_10 = models.CharField(max_length=100, default="", blank=True)
    mark_10 = models.CharField(max_length=100, default="", blank=True)
    percentage_10 = models.CharField(max_length=100, default="", blank=True)
    # =========================== Intermediate ===========================
    board_12 = models.CharField(max_length=100, default="", blank=True)
    school_12 = models.CharField(max_length=100, default="", blank=True)
    passing_12 = models.CharField(max_length=100, default="", blank=True)
    roll_12 = models.CharField(max_length=100, default="", blank=True)
    mark_12 = models.CharField(max_length=100, default="", blank=True)
    percentage_12 = models.CharField(max_length=100, default="", blank=True)
    # =========================== Graduation ===========================
    univ_graduation = models.CharField(max_length=100, default="", blank=True)
    insti_graduation = models.CharField(max_length=100, default="", blank=True)
    passing_graduation = models.CharField(
        max_length=100, default="", blank=True)
    roll_graduation = models.CharField(max_length=100, default="", blank=True)
    mark_graduation = models.CharField(max_length=100, default="", blank=True)
    percentage_graduation = models.CharField(
        max_length=100, default="", blank=True)
    # =========================== Master degree ===========================
    univ_master = models.CharField(max_length=100, default="", blank=True)
    insti_master = models.CharField(max_length=100, default="", blank=True)
    passing_master = models.CharField(max_length=100, default="", blank=True)
    roll_master = models.CharField(max_length=100, default="", blank=True)
    mark_master = models.CharField(max_length=100, default="", blank=True)
    percentage_master = models.CharField(
        max_length=100, default="", blank=True)
    # =========================== Document Upload ===========================
    edudoc = models.FileField(upload_to="Job/Document/", blank=True)
    imgs = models.FileField(upload_to="Job/Image/", blank=True)
    sign = models.FileField(upload_to="Job/Signature/", blank=True)
    submitted_on = models.DateField()
    # =========================== Status ===========================
    completed = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    reference_number = models.CharField(
        max_length=15, default="")

    def __str__(self):
        return self.name + " (" + self.reference_number + ")"
