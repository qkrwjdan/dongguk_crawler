from dotenv import load_dotenv

load_dotenv()
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

style = """
      /* style */
      .title {
          text-align: center;
      }

      .detail {
          text-align: center;
      }

      .content-theme {
        text-align: center;
      }

      .date-time {
          text-align: center;
      }

      .content-title {
        text-decoration: none;
      }
      a:visited {text-decoration: none; color: black;}
      
      .contact {
        text-align: center;
      }
"""

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
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><!--[if IE]><html xmlns="http://www.w3.org/1999/xhtml" class="ie"><![endif]--><!--[if !IE]><!--><html style="margin: 0;padding: 0;" xmlns="http://www.w3.org/1999/xhtml"><!--<![endif]--><head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title></title>
            <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge" /><!--<![endif]-->
            <meta name="viewport" content="width=device-width" />
            <meta name="robots" content="noindex,nofollow" />
            <meta property="og:title" content="My First Campaign" />
            <meta name="x-apple-disable-message-reformatting" />
            <style type="text/css">{style}</style>
            </head>
            <body>
                <h1 class="title" style = "text-align: center;">
                    Dongguk 알리미
                </h1>

                <div class="detail" style = "text-align: center;">
                    새 글을 정리해드릴게요.
                </div>
            <br>
            <div class="date-time" style = "text-align: center;" > {date} - {time} </div>
            <hr>""".format(style=style, date = date, time = time)
        self.template += block
        return block

    def theme_block(self, theme):
        block = """
            <h2 class="content-theme" style = "text-align: center;">{theme}</h2>
            """.format(theme = theme)
        self.template += block
        return block

    def content_block(self,post):
        block = """
            <a href = {link} style = "text-decoration: none;" visited:"text-decoration:none; color: black;">
                <h3>{title}</h3>
            </a>
            <p>{content}</p>
            <hr>
            """.format(title = post.title,content = post.content,link = post.link)
        self.template += block
        return block
    
    def end_block(self):
        block = """
        <div class = "contact" style = "text-align: center;">문의사항은 park.boong.u@gmail.com으로 메일주세요 :)</div>
        </body>
        </html>
        """
        self.template += block
        return block