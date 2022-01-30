import random
import string
from .models import *

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "ord_" + ''.join(random.choice(chars) for _ in range(size))


def filter_card_name(order_id):
    order_id = order_id
    order_id_lst = order_id.split("_")
    reference_code = order_id_lst[-1][-1]
    if reference_code == "m":
        return "Membership Card"
    elif reference_code == "h":
        return "Health Card"
    elif reference_code == "k":
        return "Kisan Card"
    else: pass

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
    return data

def regenerate_order_id(card):
    card.order_id = random_string_generator() + card.reference_number.lower()
    card.save()