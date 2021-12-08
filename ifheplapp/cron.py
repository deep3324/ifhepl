import ifheplapp
from ifheplapp.models import HealthCard, KisanCard, Membership

def membership_cron_job():
    datas = Membership.objects.all()
    for data in datas:
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
            "village": data.village,
            "po": data.po,
            "ps": data.ps,
            "block":data.block,
            "district": data.district,
            "state" :data.state,
            "pin_code": data.pin_code,
        }
        ifheplapp.qr_generator("Membership",datam)
        ifheplapp.membership_card_creation(datam)
        ifheplapp.membership_card_creation_back(datam)

