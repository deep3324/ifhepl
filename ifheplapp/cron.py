import ifheplapp
from ifheplapp.models import HealthCard, KisanCard, Membership
from ifheplapp import card_creation, qr_generator
from django_cron import CronJobBase, Schedule
from datetime import datetime, timedelta

class MembershipCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'ifheplapp.cards.membership_card_generate'    # a unique code

    def do(self):
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
            if not data.created and data.approve:
                qr_generator("Membership",datam)
                card_creation("Membership",datam)
                data.created = True
                data.underprocess = False
                data.approve = False
                data.reject = False
                data.save()

class HealthCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'ifheplapp.cards.health_card_generate'    # a unique code

    def do(self):
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
            if not data.created and data.approve:
                qr_generator("HealthCard",datam)
                card_creation("HealthCard",datam)
                data.created = True
                data.underprocess = False
                data.approve = False
                data.save()

class KisanCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'ifheplapp.cards.kisan_card_generate'    # a unique code

    def do(self):
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
            if not data.created and data.approve:
                qr_generator("KisanCard",datam)
                card_creation("KisanCard",datam)
                data.created = True
                data.underprocess = False
                data.approve = False
                data.save()
