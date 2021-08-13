from dotenv import load_dotenv

load_dotenv()
import os
import smtplib
from email.mime.text import MIMEText

def send_mail(receivers, subject, content):

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('park.boong.u@gmail.com',os.getenv('MAIL_PASSWORD'))

    for receiver in receivers:
        msg = MIMEText(content)
        msg['Subject'] = subject
        s.sendmail('park.boong.u@gmail.com', receiver, msg.as_string())

    s.quit()
    
