from ifhepl.settings import MEDIA_ROOT
import pdfkit
from django.contrib.auth import authenticate
from rest_framework import serializers
from smtplib import SMTPException
from django.core.mail.message import EmailMessage




def convert_to_html(html):
    pdfkit.from_string(html, MEDIA_ROOT + '/out.pdf')

def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
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

import qrcode
import os
from django.conf import settings

def qr_generator(data):
    qr = qrcode.QRCode(
        version=5,
        box_size=5,
        border=2
    )
    data = data
    print(data)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black',back_color='white')
    img.save('{}.png'.format(data["Name"]))
    # img.save('{}.png'.format("1"))
    # uploaded_filename = img.save('{}.png'.format(data["name"]))
    # try:
    #     os.mkdir(os.path.join(settings.MEDIA_ROOT, folder))
    # except:
    #     pass

    # # save the uploaded file inside that folder.
    # full_filename = os.path.join(settings.MEDIA_ROOT, folder, uploaded_filename)
from PIL import Image, ImageFont, ImageDraw

def membership_card_creation(data):
        my_image = Image.open("kisancard.png")
        print( format_date(data["DOB"]))
        title_font = ImageFont.truetype("arial.ttf", 32)
        title_font1 = ImageFont.truetype("arial.ttf", 60)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((470, 111), data["village"].title(), (0, 0, 0), font=title_font)
        image_editable.text((470, 166), data["po"].title(), (0, 0, 0), font=title_font)
        image_editable.text((470, 216), data["ps"].title(), (0, 0, 0), font=title_font)
        image_editable.text((470, 266), data["block"].title(), (0, 0, 0), font=title_font)
        image_editable.text((470, 314), data["district"].title(), (0, 0, 0), font=title_font)
        image_editable.text((750, 366), data["pin_code"].title(), (0, 0, 0), font=title_font)
        # my_image.paste((Image.open("{}.png".format(data["Name"]))).resize(
        #     (220, 220), Image.ANTIALIAS), (58, 210))
        # my_image.save(MEDIA_ROOT + "\\converted\\" +str(member.name.title()).replace(" ","_") + ".png")
        my_image.save("{}_1.png".format(data["Name"]))
    
def format_num(strn):
    return strn[0:4] + " " + strn[4:8] + " " + strn[8: ]
from datetime import datetime


def format_date(date_string):
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    formated_date = date_object.strftime("%d/%m/%Y")
    return formated_date