import os
import json
import traceback

import sendgrid
from sendgrid.helpers.mail import Category, Content, Email, Mail, Personalization

from email_func import get_file_content, get_configurations


if __name__ == "__main__":
    mail = Mail()
    mail.from_email = Email("test@example.com", "Rahul Shelke")
    mail.subject = "This is test email from sendgrid."

    personalization = Personalization()
    personalization.add_to(Email("test1@example.com", "Rahul Shelke"))
    personalization.add_to(Email("test2@example.com", "Rahul Shelke"))
    personalization.add_cc(Email("test3@example.com", "Rahul Shelke"))
    personalization.add_bcc(Email("test4@example.com", "Rahul Shelke"))
    mail.add_personalization(personalization)

    html = get_file_content("{template}.html".format(template="email")).decode("utf8")
    text = get_file_content("{template}.txt".format(template="email")).decode("utf8")
    mail.add_content(Content("text/plain", text))
    mail.add_content(Content("text/html", html))

    config = get_configurations()
    try:
        sendgrid_client = sendgrid.SendGridAPIClient(config['SENDGRID']['apikey'])
        response = sendgrid_client.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

