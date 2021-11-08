import csv
import smtplib
import re
import time
from smtplib import SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_data = csv.reader(open(r'E:\Work\ifhepl\ifheplapp\templates\bulkmail\candidate.csv', 'r'))
email_pattern = re.compile("")
lst = []
for row in email_data:
    msg = MIMEMultipart()
    msg['Subject'] = 'Employee Profile Registration | IFHEPL'   # SUBJECT
    msg['From'] = 'hr@ifhepl.in'
    name_list = row[0]

    html = """\
            <!DOCTYPE html
  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Viga&display=swap" rel="stylesheet">
  <title>Mailer</title>

  <style rel="stylesheet" type="text/css">
    @media only screen and (max-width: 600px) {
      table table.table1 {
        width: 95% !important
      }

      table {
        width: 100% !important;
      }

      .column {
        width: 100% !important;
        display: block !important;
        text-align: center
      }
    }
  </style>

</head>

<body>
  <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0" style="background:#fff;">
    <tr>
      <td bgcolor="#261c2c" height="138">
        <table class="table1" width="700" border="0" align="center" cellpadding="0" cellspacing="0"
          style="width:95% !important; padding:10px; ">
          <tr>
            <td align="center"><a href="https://ifhepl.in/" target="_blank"><img
                  src="https://ifhepl.in/static/images/logo/logo-w.png" width="480" style="border:0;height:auto;" /></a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td bgcolor="#FFFEEE">
        <table class="table1" width="700" border="0" align="center" cellpadding="0" cellspacing="0"
          style="width:95% !important;">
          <tr>
            <td height="25">&nbsp;</td>
          </tr>
          <tr>
            <td><strong><span style="font-family:Arial, Helvetica, sans-serif; font-size:16px; color:#2c2a2b">Dear """+ name_list+""",</span></strong></td>
          </tr>
          <tr>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td>
              <span style="font-family:Arial, Helvetica, sans-serif; font-size:14px; line-height:150%; color:#000000">
                Click on the below link and complete your profile. These details are necessary for your identity card, so kindly check again before submission.<br />
                <a href="https://ifhepl.in/api/EmployeeRegistration" style="color:red">Click Here</a>
                <br /><br />
                <strong>Read the instructions given below carefully before filling up the form.</strong><br />
              </span>
              <span style="font-size:13px; line-height:150%; color:#4e4e4e">
                <strong>Username - </strong>Your username is your Employee ID. Don't fill any other letters in the space provided for the username.<br />
                <strong>Password - </strong>Fill in the password section with your Date of Birth. The format of the password must be ddmmyyyy (Do not use . or , or / or - )<br />
                <strong>Email id - </strong>Use the Email ID you have provided to the company.<br />
                <strong>Photo - </strong>Upload your passport size photo.<br />
                <br />
              </span>
            </td>
          </tr>
          <tr>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td><span style="font-family:Arial, Helvetica, sans-serif; font-size:14px;">Thanks and Regards,<br />
                <strong style="font-size: 1.25rem;font-family: 'Viga';letter-spacing: 1px;">IFHE Pvt. Ltd.</strong> <br />
              </span>
              </td>
          </tr>
          <tr>
            <td height="25" align="center" style="padding-bottom: 20px">&nbsp;<hr>
            This is an auto generated mail. Please do not reply to the same.
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td height="138" bgcolor="#261c2c">
        <table width="700" border="0" align="center" cellpadding="0" cellspacing="0">
          <tr>
            <td class="column" align="center" width="100%" style="padding-bottom:10px"><span
                style="font-family:Arial, Helvetica, sans-serif; font-size:16px; color:#fff;width: 100% !important; display: block !important; text-align:center">&copy;
                Copyright <strong>IFHEPL 2021</strong> All Rights Reserved</span></td>
          </tr>
          <tr>
            <td class="column" align="center" width="100%"
              style="width: 100% !important; display: block !important; text-align:center"><a
                href="" target="_blank"><img
                  src="https://ifhepl.in/static/images/icon/fb.png" width="25" height="25"
                  style="border:0" /></a>&nbsp; <a href="" target="_blank"><img
                  src="https://ifhepl.in/static/images/icon/instagram.png" width="25" height="25"
                  style="border:0" /></a>&nbsp; <a
                href=""
                target="_blank"><img src="https://ifhepl.in/static/images/icon/linkedin.png" width="25" height="25"
                  style="border:0" /></a>&nbsp;</td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>&nbsp;</td>
    </tr>
  </table>
</body>

</html>

          """

    txt = MIMEText(html, 'html')
    msg.attach(txt)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('hr@ifhepl.in', 'glfsoumjktqdrzkf')
    email_data = csv.reader(open('candidate.csv', 'r'))
    email_pattern = re.compile("^.+@.+\..+$")
    if(email_pattern.search(row[1])):
        del msg['To']
        msg['To'] = row[1]
        try:
            server.sendmail('hr@ifhepl.in',
                            [row[1]], msg.as_string())
            time.sleep(7)
        except SMTPException:
            print("An error occured. " + row[0])
    server.quit()
