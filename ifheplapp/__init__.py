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
