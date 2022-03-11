import requests
import json
import time
import os
import qrcode
import pdfkit
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from smtplib import SMTPException
from django.core.mail.message import EmailMessage
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw


def convert_to_html(html):
    pdfkit.from_string(html, settings.MEDIA_ROOT + '/out.pdf')


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError(
            "Invalid username/password. Please try again!")
    return user


def def_mail(subject, html, receiver_email):
    subject, from_email, to = subject, 'care@ifhepl.in', receiver_email
    msg = EmailMessage(subject, html, from_email, [to])
    msg.content_subtype = "html"  # Main content is now text/html
    try:
        msg.send()
        status = "Success"
    except SMTPException:
        status = "Failed"
    return {"status": status}


"""
QR Generator
pip install qrcode #To generate QR code
pip install Pillow #To manage Images
"""


def qr_generator(card_name, data):
    qr = qrcode.QRCode(
        version=5,
        box_size=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        border=2
    )
    data = data
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    path = settings.MEDIA_ROOT + f"/{card_name}/"
    path_exist = os.path.exists(path)
    if not path_exist:
        os.mkdir(path)
    else:
        pass
    qr_path = path + "QR"
    qr_path_exist = os.path.exists(qr_path)
    if not qr_path_exist:
        os.mkdir(qr_path)
    else:
        pass
    if qr_path:
        img.save(f'{qr_path}/{data["Card Number"]}.png')


def card_creation(card_name, data):
    path = settings.MEDIA_ROOT + f"/{card_name}/"
    path_exist = os.path.exists(path)
    if not path_exist:
        os.mkdir(path)
    else:
        pass
    card_path = path + "CARD"
    card_path_exist = os.path.exists(card_path)
    if not card_path_exist:
        os.mkdir(card_path)
    else:
        pass
    """Front image data fill"""
    front_image = Image.open(settings.MEDIA_ROOT +
                             f"/{card_name}/{card_name}.png")
    text_font = ImageFont.truetype("arial.ttf", 35)
    card_number_font = ImageFont.truetype("arial.ttf", 60)
    front_edit = ImageDraw.Draw(front_image)
    front_edit.text(
        (635, 299), data["Name"].title(), (0, 0, 0), font=text_font)
    front_edit.text((635, 352), format_date(
        data["DOB"]), (0, 0, 0), font=text_font)
    front_edit.text(
        (635, 400), data["Father's / Husband's Name"].title(), (0, 0, 0), font=text_font)
    front_edit.text(
        (635, 450), data["Expiry"], (0, 0, 0), font=text_font)
    front_edit.text((420, 556), format_num(
        str(data["Card Number"])), (255, 253, 246), font=card_number_font)
    front_image.paste((Image.open(path + "QR/{}.png".format(data["Card Number"]))).resize(
        (220, 220), Image.ANTIALIAS), (58, 210))

    """Back image data fill"""
    back_image = Image.open(settings.MEDIA_ROOT +
                            f"/{card_name}/{card_name}_1.png")
    back_edit = ImageDraw.Draw(back_image)
    back_edit.text(
        (510, 100), data["village"].title(), (0, 0, 0), font=text_font)
    back_edit.text(
        (510, 152), data["po"].title(), (0, 0, 0), font=text_font)
    back_edit.text(
        (510, 203), data["ps"].title(), (0, 0, 0), font=text_font)
    back_edit.text(
        (510, 252), data["block"].title(), (0, 0, 0), font=text_font)
    back_edit.text(
        (510, 300), data["district"].title(), (0, 0, 0), font=text_font)
    back_edit.text(
        (760, 348), data["pin_code"].title(), (0, 0, 0), font=text_font)
    if card_path:
        front_image.save(f'{card_path}/{data["Card Number"]}.png')
        back_image.save(f'{card_path}/{data["Card Number"]}_1.png')
        # os.remove(path + "QR/{}.png".format(data["Card Number"]))
        time.sleep(7)


def format_num(strn):
    return strn[0:4] + " " + strn[4:8] + " " + strn[8:]


def format_date(date_string):
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    formated_date = date_object.strftime("%d/%m/%Y")
    return formated_date


def verify_recaptcha(recaptha_response):
    recaptha_response = recaptha_response
    captaData = {
        "secret": "6LfQqGUeAAAAAO-GGEGklpMpeYfsxI8S3uCbIWqL",
        "response":  recaptha_response
    }
    r = requests.post(
        'https://www.google.com/recaptcha/api/siteverify', data=captaData)
    response = json.loads(r.text)
    verify = response["success"]
    return verify


def send_sms_form_submission(receiver_name, card_name,reference_number,link):
    url = "https://www.fast2sms.com/dev/bulkV2?numbers={}&sender_id=IFHEPL&route=dlt&variables_values={}|{}|{}&message=137304".format(receiver_name,card_name,reference_number,link)
    headers = {
        "authorization": "GfudeC2NmBDPlpIhXLVv3inyRvgdXiO2sX46r48lGVqAa9lrQJoJlZ87FGMv",
        "Content-Type": "application/json",
        'Cache-Control': "no-cache"
    }
    requests.request("POST", url, headers=headers)

def send_sms_job_submission(receiver_name ,reference_number,link):
    url = "https://www.fast2sms.com/dev/bulkV2?numbers={}&sender_id=IFHEPL&route=dlt&variables_values={}|{}&message=137363".format(receiver_name,reference_number,link)
    headers = {
        "authorization": "GfudeC2NmBDPlpIhXLVv3inyRvgdXiO2sX46r48lGVqAa9lrQJoJlZ87FGMv",
        "Content-Type": "application/json",
        'Cache-Control': "no-cache"
    }
    requests.request("POST", url, headers=headers)

def send_sms_vendor_submission(receiver_name ,reference_number,link):
    url = "https://www.fast2sms.com/dev/bulkV2?numbers={}&sender_id=IFHEPL&route=dlt&variables_values={}|{}&message=137364".format(receiver_name,reference_number,link)
    headers = {
        "authorization": "GfudeC2NmBDPlpIhXLVv3inyRvgdXiO2sX46r48lGVqAa9lrQJoJlZ87FGMv",
        "Content-Type": "application/json",
        'Cache-Control': "no-cache"
    }
    requests.request("POST", url, headers=headers)

def send_sms_vendor_username(receiver_name ,reference_number,link):
    url = "https://www.fast2sms.com/dev/bulkV2?numbers={}&sender_id=IFHEPL&route=dlt&variables_values={}|{}&message=137364".format(receiver_name,reference_number,link)
    headers = {
        "authorization": "GfudeC2NmBDPlpIhXLVv3inyRvgdXiO2sX46r48lGVqAa9lrQJoJlZ87FGMv",
        "Content-Type": "application/json",
        'Cache-Control': "no-cache"
    }
    requests.request("POST", url, headers=headers)
