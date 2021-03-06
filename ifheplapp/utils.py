from urllib import response
import razorpay
from django.conf import settings
import random
import string

from jobApplications.models import job_application
from vendorApplication.models import vendorApplication
from .models import *


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "ord_" + ''.join(random.choice(chars) for _ in range(size))


def filter_application_name(order_id):
    order_id = order_id
    order_id_lst = order_id.split("_")
    reference_code = order_id_lst[-1][-1]
    if reference_code == "m":
        params = {"card_name" : "Membership Card", "amount": 119.00}
    elif reference_code == "h":
        params = {"card_name" : "Health Card", "amount": 119.00}
    elif reference_code == "k":
        params = {"card_name" : "Kisan Card", "amount": 119.00}
    elif reference_code == "v":
        params = {"card_name" : "Vendor Application", "amount": 500.00}
    else:
        params = {"card_name" : "Job Application", "amount": 300.00}
    return params


def fetch_card(order_id):
    order_id = order_id
    order_id_lst = order_id.split("_")
    reference_code = order_id_lst[-1][-1]
    if reference_code == "m":
        data = Membership.objects.get(order_id=order_id)
    elif reference_code == "h":
        data = HealthCard.objects.get(order_id=order_id)
    elif reference_code == "k":
        data = KisanCard.objects.get(order_id=order_id)
    elif reference_code == "j":
        data = job_application.objects.get(order_id=order_id)
    elif reference_code == "v":
        data = vendorApplication.objects.get(order_id=order_id)
    return data


def regenerate_order_id(card):
    if not card.paid:
        pass
    else:
        card.order_id = random_string_generator() + "_" + card.reference_number.lower()
        card.save()