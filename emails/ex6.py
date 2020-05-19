import os
import json
import traceback

import sendgrid
from sendgrid.helpers.mail import Category, Content, Email, Mail, Personalization

from email_func import get_file_content, get_configurations

config = get_configurations()
os.environ["SENDGRID_API_KEY"] = config['SENDGRID']['apikey']
sg = sendgrid.SendGridAPIClient(api_key=config['SENDGRID']['apikey'])


class EmailNotifications(object):

    def __init__(self, **kwargs):
        super(EmailNotifications, self).__init__(**kwargs)

    def get_templates(self, template_name):
        """
        Get html and text templates for emails
        """
        html = get_file_content("{template}.html".format(template=template_name)).decode("utf8")
        text = get_file_content("{template}.txt".format(template=template_name)).decode("utf8")
        return html, text

    def create_personalization(self, **kwargs):
        """Build personalization instance from a dict

        :param kwargs: Dictionary containing personalized params
        :return: personalization object
        """
        EMAIL_KEYS = ["from_email", "to", "cc", "bcc"]
        PERSONALIZATION_KEYS = ["to", "cc", "bcc", "header", "substitution", "custom_arg", "send_at", "subject"]
        personalization = Personalization()
        _diff = set(PERSONALIZATION_KEYS).intersection(set(kwargs.keys()))
        if _diff:
            for key in _diff:
                item = kwargs.get(key)
                if item:
                    if key in EMAIL_KEYS and not isinstance(item, list):
                        item = item.split(',')
                    if isinstance(item, list):
                        for _addr in item:
                            if not isinstance(_addr, Email):
                                _addr = Email(_addr)
                            func = getattr(personalization, "add_{0}".format(key))
                            if func:
                                func(_addr)
                    else:
                        func = getattr(personalization, "{0}".format(key))
                        if func:
                            func(item)

        return personalization

    def get_message(self, **kwargs):
        """
        Get message object for email
        """
        config = get_configurations()
        message = Mail()
        if "from_email" in kwargs:
            sender = Email()
            message_content = kwargs.get("message_content", "")
            sender.name = kwargs.get("sender", config['SENDGRID']['sender'])
            sender.email = kwargs.get("from_email", config['SENDGRID']['fromemail'])
            message.from_email = sender
        if "subject" in kwargs:
            message.subject = kwargs.get("subject", "")
        if "text" in kwargs:
            content = Content("text/plain", kwargs.get("text", ""))
            message.add_content(content)
        if "html" in kwargs:
            content = Content("text/html", kwargs.get("html", ""))
            message.add_content(content)
        if "category" in kwargs:
            category = Category(kwargs.get("category", ""))
            message.add_category(category)

        personalization = self.create_personalization(**kwargs)
        if personalization:
            message.add_personalization(personalization)

        return message.get()

    def send_message(self, message):
        """
        Send message to receiver via gateway
        """
        try:
            sg.client.mail.send.post(request_body=message)
        except Exception as e:
            traceback.print_exc()

    def message_notifier(self, **kwargs):
        """
        Message notifier helper to send message
        """
        template_name = "email"
        html, text = self.get_templates(template_name=template_name)
        message = self.get_message(html=html, text=text, **kwargs)
        self.send_message(message)


if __name__ == "__main__":
    email = EmailNotifications()
    kwargs = {
        "sender": "Rahul Shelke",
        "from_email": "test@mco.in",
        "to": ["test@example.com", "test2@example.com"],
        "cc": ["test3@example.com"],
        "bcc": ["test4@example.com"],
        "subject": "This is test email from sendgrid.",
        "category": "Testing"
    }
    email.message_notifier(**kwargs)
