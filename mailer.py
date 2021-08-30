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

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org" 
html = """
<html>
<head></head>
<body>
<h1 id="-dongguk-" style='text-align: center;'"><strong>Dongguk 알리미.</strong></h1>
<pre><code>              새 글을 정리해드릴게요.

                    2021<span class="hljs-selector-class">.08</span><span class="hljs-selector-class">.16</span>     13<span class="hljs-selector-pseudo">:32</span>
</code></pre><hr>
<p>일반 공지</p>
<h2 id="-2021-4-"><strong>신규 입주기업 모집 공고(2021년 4차... (제목 전부 나오면 좋겠다.)</strong></h2>
<p>내용 일부 …</p>
<p>링크</p>
<h2 id="-2021-4-"><strong>신규 입주기업 모집 공고(2021년 4차...</strong></h2>
<p>내용 일부 …</p>
<p>링크</p>
<hr>
<p>학사 공지</p>
<h2 id="-2021-4-"><strong>신규 입주기업 모집 공고(2021년 4차...</strong></h2>
<p>내용 일부 …</p>
<p>링크</p>
<h2 id="-2021-4-"><strong>신규 입주기업 모집 공고(2021년 4차...</strong></h2>
<p>내용 일부 …</p>
<p>링크</p>
</body>
</html>
"""