from django.db import models
from autoslug import AutoSlugField
from datetime import datetime
from django.contrib.auth.models import User
import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.


def membership_card_increase():
    larget = Membership.objects.all().order_by('card_number').last()
    if not larget:
        return 541219412471
    else:
        return larget.card_number + 1


def kisan_card_increase():
    larget = KisanCard.objects.all().order_by('card_number').last()
    if not larget:
        return 541219612471
    else:
        return larget.card_number + 1


def health_card_increase():
    larget = HealthCard.objects.all().order_by('card_number').last()
    if not larget:
        return 541219812471
    else:
        return larget.card_number + 1


class AssociatePartner(models.Model):
    partnerName = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.partnerName

class Jobs(models.Model):
    title = models.CharField(max_length=100, default="")
    slug = AutoSlugField(populate_from='title')
    qualification = models.CharField(max_length=500, default="")
    salary = models.CharField(max_length=500, default="")
    is_insentive = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Attendance(models.Model):
    employeeID = models.CharField(max_length=14, default="")
    employeeName = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=500, default="")
    image = models.FileField(upload_to="Attendance/")
    uploaded_at = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.employeeName
    def save(self, *args, **kwargs):
        if not self.id:
            self.image = self.compressImage(self.image)
        super(Attendance, self).save(*args, **kwargs)
    def compressImage(self,image):
        imageTemproary = Image.open(image)
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.convert('RGB')
        # imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=50)
        outputIoStream.seek(0)
        image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return image


class Gallery(models.Model):
    title = models.CharField(max_length=200, default="", blank=True)
    image = models.FileField(upload_to="Gallery/")


class Slider(models.Model):
    title = models.CharField(max_length=200, default="", blank=True)
    image = models.FileField(upload_to="Slider/")


notice_type = [
    ('Rules & Regulation', 'Rules & Regulation',),
    ('Academic Notice', 'Academic Notice',),
    ('Administrative Notice', 'Administrative Notice',),
    ('Requirement Notice', 'Requirement Notice',),
]


class Notice(models.Model):
    notice_type = models.CharField(choices=notice_type, max_length=100)
    title = models.CharField(max_length=200, default="")
    doc = models.FileField(upload_to="Notice/")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    message = models.TextField()
    contacted_on = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name


class Membership (models.Model):
    id = models.AutoField(primary_key=True)
    # =============== Personal Details =======================
    employeeID = models.CharField(max_length=100, default="")
    employeename = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    idtype = models.CharField(max_length=100, default="")
    id_proof = models.CharField(max_length=100, default="", blank=True)
    father_Husband_name = models.CharField(max_length=100, default="")
    mother_name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    disability = models.CharField(max_length=100, default="")
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
    # =========================== Document Upload ===========================
    id_proof_document = models.FileField(upload_to="Membership/ID_Proof/")
    photo = models.FileField(upload_to="Membership/Photo/")
    sign = models.FileField(upload_to="Membership/Signature/")
    submitted_on = models.DateField()
    # =========================== Card Update ===========================
    approve = models.BooleanField(default=False)
    underprocess = models.BooleanField(default=True)
    reject = models.BooleanField(default=False)
    card_number = models.IntegerField(
        default=membership_card_increase, primary_key=False)
    reference_number = models.CharField(
        max_length=15, default="")

    def __str__(self):
        return self.name + " (" + self.reference_number + ")"


class KisanCard(models.Model):
    id = models.AutoField(primary_key=True)
    # =============== Personal Details =======================
    employeeID = models.CharField(max_length=100, default="")
    employeename = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    idtype = models.CharField(max_length=100, default="")
    id_proof = models.CharField(max_length=100, default="", blank=True)
    father_Husband_name = models.CharField(max_length=100, default="")
    mother_name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    disability = models.CharField(max_length=100, default="")
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
    # =========================== Document Upload ===========================
    id_proof_document = models.FileField(upload_to="KisanCard/ID_Proof/")
    photo = models.FileField(upload_to="KisanCard/Photo/")
    submitted_on = models.DateField()
    # =========================== Card Update ===========================
    approve = models.BooleanField(default=False)
    underprocess = models.BooleanField(default=True)
    reject = models.BooleanField(default=False)
    card_number = models.IntegerField(
        default=kisan_card_increase, primary_key=False)
    reference_number = models.CharField(
        max_length=15, default="")

    def __str__(self):
        return self.name + " (" + self.reference_number + ")"


class HealthCard(models.Model):
    id = models.AutoField(primary_key=True)
    # =============== Personal Details =======================
    employeeID = models.CharField(max_length=100, default="")
    employeename = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    idtype = models.CharField(max_length=100, default="")
    id_proof = models.CharField(max_length=100, default="", blank=True)
    father_Husband_name = models.CharField(max_length=100, default="")
    mother_name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    disability = models.CharField(max_length=100, default="")
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
    # =========================== Document Upload ===========================
    id_proof_document = models.FileField(upload_to="HealthCard/ID_Proof/")
    photo = models.FileField(upload_to="HealthCard/Photo/")
    submitted_on = models.DateField()
    # =========================== Card Update ===========================
    approve = models.BooleanField(default=False)
    underprocess = models.BooleanField(default=True)
    reject = models.BooleanField(default=False)
    card_number = models.IntegerField(
        default=health_card_increase, primary_key=False)
    reference_number = models.CharField(
        max_length=15, default="")

    def __str__(self):
        return self.name + " (" + self.reference_number + ")"


class JobApply (models.Model):
    # =============== Personal Details =======================
    applied_for = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    idtype = models.CharField(max_length=100, default="")
    id_proof = models.CharField(max_length=100, default="", blank=True)
    father_Husband_name = models.CharField(max_length=100, default="")
    mother_name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    disability = models.CharField(max_length=100, default="")
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
    edudoc = models.FileField(upload_to="Job/Document/")
    imgs = models.FileField(upload_to="Job/Image/")
    sign = models.FileField(upload_to="Job/Signature/")
    submitted_on = models.DateField()
    # =========================== Status ===========================
    approve = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    reference_number = models.CharField(
        max_length=15, default="")

    def __str__(self):
        return self.name + " (" + self.reference_number + ")"
