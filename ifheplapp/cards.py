from ifheplapp import convert_to_html, membership_card_creation, qr_generator,membership_card_creation_back
from ifheplapp.models import Membership
from django.http import HttpResponse

def qr_generator_fuc(request):
    datas = Membership.objects.all()
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
    datas = Membership.objects.all()
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
        membership_card_creation_back(datam)
    return HttpResponse("Qr generatred")