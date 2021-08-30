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
        
        self.template = ""
        for block in blocks:
            self.template += block

        return self.template

    def add_block(self,block):
        self.template += block

    def header_block(self, date, time):
        block =  """
            <html>
            <head></head>
            <body>
            <h1 id="-dongguk-" style='text-align: center;'"><strong>Dongguk 알리미.</strong></h1>
            <pre><code>              새 글을 정리해드릴게요.
            </code></pre>
            <br>
            <span> {date} - {time} </span>
            <hr>""".format(date = date, time = time)
        self.template += block
        return block

    def theme_block(self, theme):
        block = """
            <h2>{theme}</h2>
            """.format(theme = theme)
        self.template += block
        return block

    def content_block(self,post):
        block = """
            <h3 id="-2021-4-"><strong>{title}</strong></h3>
            <p>{content}</p>
            <p><a href="{link}">이 게시물을 보고싶다면?</p>
            <hr>
            """.format(title = post.title,content = post.content,link = post.link)
        self.template += block
        return block
    
    def end_block(self):
        block = """
        </body>
        </html>
        """
        self.template += block
        return block