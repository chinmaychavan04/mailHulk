
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template



def sendMail(request, mail_list):
    template = render_to_string('ac/emailT.html')
    subject = 'Welcome to The Gadgets Zone'

    email = EmailMessage(
        subject,
        template,
        settings.EMAIL_HOST_USER,
        mail_list,
    )

    email.fail_silently = False
    email.content_subtype = 'html'
    email.send()
