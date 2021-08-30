from dotenv import load_dotenv

load_dotenv()
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(receivers, subject, content):

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('park.boong.u@gmail.com',os.getenv('MAIL_PASSWORD'))

    msg = MIMEMultipart('alternative')

    for receiver in receivers:
        part = MIMEText(content,"html")
        msg.attach(part)
        msg['Subject'] = subject
        s.sendmail('park.boong.u@gmail.com', receiver, msg.as_string())

    s.quit()

class BaseTemplate():

    def __init__(self):
        self.template = ""

    def get_template(self, blocks):
        
        template = ""
        for block in blocks:
            template += block

        self.template = template

        return template

    def header_block(self, date, time):
        return """
            <html>
            <head></head>
            <body>
            <h1 id="-dongguk-" style='text-align: center;'"><strong>Dongguk 알리미.</strong></h1>
            <pre><code>              새 글을 정리해드릴게요.
            </code></pre>
            <br>
            <span> {date} - {time} </span>
            <hr>""".format(date = date, time = time)


    def theme_block(self, theme):
        return """
            <h2>{theme}</h2>
            """.format(theme = theme)

    def content_block(self, title, content, link):
        return """
            <h3 id="-2021-4-"><strong>{title}</strong></h3>
            <p>{content}</p>
            <p>{link}</p>
            <hr>
            """.format(title = title,content = content,link = link)
    
    def end_block(self):
        return """
        </body>
        </html>
        """