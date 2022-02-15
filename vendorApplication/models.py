from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class vendorApplication(models.Model):
    id = models.AutoField(primary_key=True)
    # =============== Personal Details =======================
    VendorID = models.CharField(max_length=100, default="", blank=True)
    name = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    idtype = models.CharField(max_length=100, default="")
    id_proof = models.CharField(max_length=100, default="", blank=True)
    father_Husband_name = models.CharField(max_length=100, default="")
    mother_name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    disability = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=100, default="")
    religion = models.CharField(max_length=100, default="")
    marital_status = models.CharField(max_length=100, default="")
    language_known = models.CharField(max_length=100, default="")
    occupation = models.CharField(max_length=100, default="")
    nominee_name = models.CharField(max_length=100, default="")
    work_area = models.CharField(max_length=100, default="")
    mobile_number = models.CharField(max_length=100, default="")
    alt_mobile_no = models.CharField(max_length=100, default="", blank=True)
    email = models.CharField(max_length=100, default="", blank=True)
    # =========================== Address ===========================
    village = models.CharField(max_length=100, default="")
    po = models.CharField(max_length=100, default="")
    ps = models.CharField(max_length=100, default="")
    block = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    pin_code = models.CharField(max_length=100, default="")
    accept_terms = models.BooleanField(default=False)
    # =========================== Document Upload ===========================
    id_proof_document = models.FileField(upload_to="Vendor/ID_Proof/")
    photo = models.FileField(upload_to="Vendor/Photo/")
    signature = models.FileField(upload_to="Vendor/Signature/")
    submitted_on = models.DateField()
    # =========================== Card Update ===========================
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
