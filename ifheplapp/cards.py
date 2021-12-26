from ifheplapp import convert_to_html, health_card_creation, health_card_creation_back, kisan_card_creation, kisan_card_creation_back, qr_generator
from ifheplapp.models import HealthCard, KisanCard, Membership
from django.http import HttpResponse
from datetime import datetime

def qr_generator_fuc(request):
    datas = HealthCard.objects.filter(submitted_on__gt = "2021-12-09")
    for data in datas:
        print(data.name)
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
            "ID Proof Document" : data.id_proof_document,
            "Photo" : data.photo,
            "Card Number" : data.card_number,
        }
        qr_generator("Membership",datam)
    return HttpResponse("Qr generatred")

def card_generator_fuc(request):
    datas = HealthCard.objects.filter(submitted_on__gt = "2021-12-09")
    for data in datas:
        print(data.name)
        datam = {
            "Name": data.name,
            "Mobile Number": data.mobile_number,
            "DOB": data.dob,
            "Id Proof and Number" : data.idtype + " - " + data.id_proof,
            "Father's / Husband's Name": data.father_Husband_name,
            "Mother's Name": data.mother_name,
            "Category": data.category,
            "Disability": data.disability,
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
        }
        health_card_creation_back(datam)
    return HttpResponse("Qr generatred")