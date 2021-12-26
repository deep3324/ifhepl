from datetime import datetime
import os
import qrcode
import pdfkit
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from smtplib import SMTPException
from django.core.mail.message import EmailMessage
from datetime import datetime, timedelta
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
        border=2
    )
    data = data
    print(data)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    print(settings.MEDIA_ROOT)
    parent_dir = settings.MEDIA_ROOT
    card_path = os.path.join(parent_dir, "{}".format(card_name))
    # if not os.path.exists(card_path):
    try:
        os.mkdir(card_path)
    except:
        pass
    final_path = os.path.join(card_path, "{}\\QR".format(datetime.now().strftime("%d %m %y")))
    try:
        os.mkdir(final_path)
    except:
        pass
    img.save('{}.png'.format(data["Name"]))


<<<<<<< HEAD
# def health_card_creation(data):
#     my_image = Image.open(settings.MEDIA_ROOT + "\\Membership\\health.png")
#     title_font = ImageFont.truetype("arial.ttf", 35)
#     title_font1 = ImageFont.truetype("arial.ttf", 60)
#     image_editable = ImageDraw.Draw(my_image)
#     image_editable.text(
#         (635, 299), data["Name"].title(), (0, 0, 0), font=title_font)
#     image_editable.text((635, 352), format_date(
#         data["DOB"]), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (635, 400), data["Father's / Husband's Name"].title(), (0, 0, 0), font=title_font)
#     image_editable.text((420, 556), format_num(
#         str(data["Card Number"])), (255, 253, 246), font=title_font1)
#     my_image.paste((Image.open("{}.png".format(data["Name"]))).resize(
#         (220, 220), Image.ANTIALIAS), (58, 210))
#     # path = os.path.join(settings.MEDIA_ROOT + '\\Membership\\{}\\cards'.format(datetime.now().strftime("%d %m %y")))
#     # if not path:
#     #     os.mkdir(path)
#     my_image.save('{}.png'.format(data["Name"]))


# def health_card_creation_back(data):
#     my_image = Image.open(settings.MEDIA_ROOT +
#                           "\\Membership\\health_1.png")
#     print(data["Name"])
#     title_font = ImageFont.truetype("arial.ttf", 35)
#     image_editable = ImageDraw.Draw(my_image)
#     image_editable.text(
#         (510, 100), data["village"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (510, 152), data["po"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (510, 203), data["ps"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (510, 252), data["block"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (510, 300), data["district"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (760, 348), data["pin_code"].title(), (0, 0, 0), font=title_font)
#     # path = os.path.join(settings.MEDIA_ROOT +
#     #                     '\\Membership\\{}\\cards'.format(datetime.now().strftime("%d %m %y")))
#     # if not path:
#     #     os.mkdir(path)
#     my_image.save('{}_1.png'.format(data["Name"]))
def kisan_card_creation(data):
    my_image = Image.open(settings.MEDIA_ROOT + "\\Membership\\kisan.png")
=======
def health_card_creation(data):
    my_image = Image.open(settings.MEDIA_ROOT + "\\Membership\\health.png")
>>>>>>> 251e91c42869b07e385db33b1b44f7ae85631880
    title_font = ImageFont.truetype("arial.ttf", 35)
    title_font1 = ImageFont.truetype("arial.ttf", 60)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text(
        (635, 299), data["Name"].title(), (0, 0, 0), font=title_font)
    image_editable.text((635, 352), format_date(
        data["DOB"]), (0, 0, 0), font=title_font)
    image_editable.text(
        (635, 400), data["Father's / Husband's Name"].title(), (0, 0, 0), font=title_font)
    image_editable.text((420, 556), format_num(
        str(data["Card Number"])), (255, 253, 246), font=title_font1)
    my_image.paste((Image.open("{}.png".format(data["Name"]))).resize(
        (220, 220), Image.ANTIALIAS), (58, 210))
    # path = os.path.join(settings.MEDIA_ROOT + '\\Membership\\{}\\cards'.format(datetime.now().strftime("%d %m %y")))
    # if not path:
    #     os.mkdir(path)
    my_image.save('{}.png'.format(data["Name"]))


<<<<<<< HEAD
def kisan_card_creation_back(data):
    my_image = Image.open(settings.MEDIA_ROOT +
                          "\\Membership\\kisan_1.png")
=======
def health_card_creation_back(data):
    my_image = Image.open(settings.MEDIA_ROOT +
                          "\\Membership\\health_1.png")
>>>>>>> 251e91c42869b07e385db33b1b44f7ae85631880
    print(data["Name"])
    title_font = ImageFont.truetype("arial.ttf", 35)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text(
        (510, 100), data["village"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (510, 152), data["po"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (510, 203), data["ps"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (510, 252), data["block"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (510, 300), data["district"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (760, 348), data["pin_code"].title(), (0, 0, 0), font=title_font)
    # path = os.path.join(settings.MEDIA_ROOT +
    #                     '\\Membership\\{}\\cards'.format(datetime.now().strftime("%d %m %y")))
    # if not path:
    #     os.mkdir(path)
    my_image.save('{}_1.png'.format(data["Name"]))
<<<<<<< HEAD
=======
def kisan_card_creation(data):
    my_image = Image.open(settings.MEDIA_ROOT + "\\Membership\\kisan.png")
    title_font = ImageFont.truetype("arial.ttf", 35)
    title_font1 = ImageFont.truetype("arial.ttf", 60)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text(
        (635, 299), data["Name"].title(), (0, 0, 0), font=title_font)
    image_editable.text((635, 352), format_date(
        data["DOB"]), (0, 0, 0), font=title_font)
    image_editable.text(
        (635, 400), data["Father's / Husband's Name"].title(), (0, 0, 0), font=title_font)
    image_editable.text((420, 556), format_num(
        str(data["Card Number"])), (255, 253, 246), font=title_font1)
    my_image.paste((Image.open("{}.png".format(data["Name"]))).resize(
        (220, 220), Image.ANTIALIAS), (58, 210))
    # path = os.path.join(settings.MEDIA_ROOT + '\\Membership\\{}\\cards'.format(datetime.now().strftime("%d %m %y")))
    # if not path:
    #     os.mkdir(path)
    my_image.save('{}.png'.format(data["Name"]))


def kisan_card_creation_back(data):
    my_image = Image.open(settings.MEDIA_ROOT +
                          "\\Membership\\kisan_1.png")
    print(data["Name"])
    title_font = ImageFont.truetype("arial.ttf", 35)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text(
        (510, 100), data["village"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (510, 152), data["po"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (510, 203), data["ps"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (510, 252), data["block"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (510, 300), data["district"].title(), (0, 0, 0), font=title_font)
    image_editable.text(
        (760, 348), data["pin_code"].title(), (0, 0, 0), font=title_font)
    # path = os.path.join(settings.MEDIA_ROOT +
    #                     '\\Membership\\{}\\cards'.format(datetime.now().strftime("%d %m %y")))
    # if not path:
    #     os.mkdir(path)
    my_image.save('{}_1.png'.format(data["Name"]))
>>>>>>> 251e91c42869b07e385db33b1b44f7ae85631880

# def membership_card_creation(data):
#     my_image = Image.open(settings.MEDIA_ROOT + "\\Membership\\membership.png")
#     title_font = ImageFont.truetype("arial.ttf", 35)
#     title_font1 = ImageFont.truetype("arial.ttf", 60)
#     image_editable = ImageDraw.Draw(my_image)
#     image_editable.text(
#         (635, 299), data["Name"].title(), (0, 0, 0), font=title_font)
#     image_editable.text((635, 352), format_date(
#         data["DOB"]), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (635, 400), data["Father's / Husband's Name"].title(), (0, 0, 0), font=title_font)
#     image_editable.text((420, 556), format_num(
#         str(data["Card Number"])), (255, 253, 246), font=title_font1)
#     my_image.paste((Image.open("{}.png".format(data["Name"]))).resize(
#         (220, 220), Image.ANTIALIAS), (58, 210))
#     # path = os.path.join(settings.MEDIA_ROOT + '\\Membership\\{}\\cards'.format(datetime.now().strftime("%d %m %y")))
#     # if not path:
#     #     os.mkdir(path)
#     my_image.save('{}.png'.format(data["Name"]))


# def membership_card_creation_back(data):
#     my_image = Image.open(settings.MEDIA_ROOT +
#                           "\\Membership\\membership_1.png")
#     print(data["Name"])
#     title_font = ImageFont.truetype("arial.ttf", 35)
#     image_editable = ImageDraw.Draw(my_image)
#     image_editable.text(
#         (510, 100), data["village"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (510, 152), data["po"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (510, 203), data["ps"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (510, 252), data["block"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (510, 300), data["district"].title(), (0, 0, 0), font=title_font)
#     image_editable.text(
#         (760, 348), data["pin_code"].title(), (0, 0, 0), font=title_font)
#     # path = os.path.join(settings.MEDIA_ROOT +
#     #                     '\\Membership\\{}\\cards'.format(datetime.now().strftime("%d %m %y")))
#     # if not path:
#     #     os.mkdir(path)
#     my_image.save('{}_1.png'.format(data["Name"]))


def format_num(strn):
    return strn[0:4] + " " + strn[4:8] + " " + strn[8:]


def format_date(date_string):
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    formated_date = date_object.strftime("%d/%m/%Y")
    return formated_date
