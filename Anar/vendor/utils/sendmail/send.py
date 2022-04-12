import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import settings

# send email
def send_email(email, body):
    """Send email function(SMTP)"""
    sender = settings['email_sender']
    recipient = email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = 'dot'

    msg.attach(MIMEText(body, 'html'))

    # establish smtp server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # start tls
    server.starttls()
    # login
    server.login(sender, settings['email_password'])
    # message
    text = msg.as_string()
    # send mail
    response = server.sendmail(sender, recipient, text)

    if not response:
        return True
    return False
