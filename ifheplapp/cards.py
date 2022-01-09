from ifheplapp import card_creation, qr_generator
from ifheplapp.models import HealthCard, KisanCard, Membership
from django.http import HttpResponse
from datetime import datetime, timedelta

def membership_card_generate(request):
    datas = Membership.objects.all()
    for data in datas:
        submitted_on = datetime.strptime(str(data.submitted_on), "%Y-%m-%d")
        exp = submitted_on + timedelta(days=335)
        expiry = datetime.strftime(exp, "%m/%Y")
        datam = {
            "Company": "IFHE Pvt. Ltd. Email: care@ifhepl.in  Website: ifhepl.in Contact Number: +91 88098 61888",
            "Name": data.name,
            "Mobile Number": data.mobile_number,
            "DOB": data.dob,
            "Id Proof and Number" : data.idtype + " - " + data.id_proof,
            "Father's / Husband's Name": data.father_Husband_name,
            "Mother's Name": data.mother_name,
            "Category": data.category,
            "Disability": data.disability,
            "Address": "village: "+ data.village + ", po: "+ data.po + ", ps: "+ data.ps +", block: "+ data.block + ", district: "+ data.district + ", state: " +data.state + ", pin_code: "+ data.pin_code,
            "village": data.village,
            "po": data.po,
            "ps": data.ps,
            "block":data.block,
            "district": data.district,
            "state" :data.state,
            "pin_code": data.pin_code,
            "ID Proof Document" : data.id_proof_document,
            "Photo" : data.photo,
            "Card Number" : data.card_number,
            "Expiry" : expiry,
        }
        if not data.created:
            qr_generator("Membership",datam)
            card_creation("Membership",datam)
            data.created = True
            data.underprocess = False
            data.approve = False
            data.save()
    return HttpResponse("Membership Card generatred")
    
def health_card_generate(request):
    datas = HealthCard.objects.all()
    for data in datas:
        submitted_on = datetime.strptime(str(data.submitted_on), "%Y-%m-%d")
        exp = submitted_on + timedelta(days=335)
        expiry = datetime.strftime(exp, "%m/%Y")
        datam = {
            "Company": "IFHE Pvt. Ltd. Email: care@ifhepl.in  Website: ifhepl.in Contact Number: +91 88098 61888",
            "Name": data.name,
            "Mobile Number": data.mobile_number,
            "DOB": data.dob,
            "Id Proof and Number" : data.idtype + " - " + data.id_proof,
            "Father's / Husband's Name": data.father_Husband_name,
            "Mother's Name": data.mother_name,
            "Category": data.category,
            "Disability": data.disability,
            "Address": "village: "+ data.village + ", po: "+ data.po + ", ps: "+ data.ps +", block: "+ data.block + ", district: "+ data.district + ", state: " +data.state + ", pin_code: "+ data.pin_code,
            "village": data.village,
            "po": data.po,
            "ps": data.ps,
            "block":data.block,
            "district": data.district,
            "state" :data.state,
            "pin_code": data.pin_code,
            "ID Proof Document" : data.id_proof_document,
            "Photo" : data.photo,
            "Card Number" : data.card_number,
            "Expiry" : expiry,
        }
        if not data.created:
            qr_generator("HealthCard",datam)
            card_creation("HealthCard",datam)
            data.created = True
            data.underprocess = False
            data.approve = False
            data.save()
    return HttpResponse("Health Card generatred")
    
def kisan_card_generate(request):
    datas = KisanCard.objects.all()
    for data in datas:
        submitted_on = datetime.strptime(str(data.submitted_on), "%Y-%m-%d")
        exp = submitted_on + timedelta(days=335)
        expiry = datetime.strftime(exp, "%m/%Y")
        datam = {
            "Company": "IFHE Pvt. Ltd. Email: care@ifhepl.in  Website: ifhepl.in Contact Number: +91 88098 61888",
            "Name": data.name,
            "Mobile Number": data.mobile_number,
            "DOB": data.dob,
            "Id Proof and Number" : data.idtype + " - " + data.id_proof,
            "Father's / Husband's Name": data.father_Husband_name,
            "Mother's Name": data.mother_name,
            "Category": data.category,
            "Disability": data.disability,
            "Address": "village: "+ data.village + ", po: "+ data.po + ", ps: "+ data.ps +", block: "+ data.block + ", district: "+ data.district + ", state: " +data.state + ", pin_code: "+ data.pin_code,
            "village": data.village,
            "po": data.po,
            "ps": data.ps,
            "block":data.block,
            "district": data.district,
            "state" :data.state,
            "pin_code": data.pin_code,
            "ID Proof Document" : data.id_proof_document,
            "Photo" : data.photo,
            "Card Number" : data.card_number,
            "Expiry" : expiry,
        }
        if not data.created:
            qr_generator("KisanCard",datam)
            card_creation("KisanCard",datam)
            data.created = True
            data.underprocess = False
            data.approve = False
            data.save()
    return HttpResponse("Kisan Card generatred")
    