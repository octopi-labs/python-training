import os
import imghdr
import smtplib
import configparser

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.encoders import encode_base64

current_dir = os.path.dirname(__file__)

def get_configurations():
     # Read configuration file
    config = configparser.ConfigParser()
    config.read(os.path.join(current_dir, "emails.cfg"))
    return config

def get_file_content(filename):
    # Create the body of the message (a plain-text and an HTML version).
    file = open(os.path.join(current_dir, filename), 'rb')
    content = file.read()
    file.close()
    
    return content

def create_message(subject, sent_from, to, text, html, file_to_attach=None):
    header = 'Content-Disposition', 'attachment; filename="{}"'.format(file_to_attach)
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sent_from
    msg['To'] = ','.join(to)

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Create an attachment
    if file_to_attach:
        file_content = get_file_content(file_to_attach)
        file_type = imghdr.what(os.path.join(current_dir, file_to_attach))
        # Attach an image
        if file_type:
            image = MIMEImage(file_content, name=file_to_attach)
            msg.attach(image)
        else:
            attachment = MIMEBase('application', "octet-stream")
            attachment.set_payload(file_to_attach)
            encode_base64(attachment)
            attachment.add_header(*header)
            msg.attach(attachment)

    return msg

def send_email(sent_from, to, msg):
    config = get_configurations()
    username = config['GMAILSMTP']['username']
    password = config['GMAILSMTP']['password']
    smtpObj = smtplib.SMTP(config['GMAILSMTP']['url'], config['GMAILSMTP']['port'])

    print(smtpObj.ehlo())

    smtpObj.starttls()

    smtpObj.login(username, password)

    smtpObj.sendmail(sent_from, to, msg.as_string())

    smtpObj.quit()