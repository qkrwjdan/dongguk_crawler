from mailer import BaseTemplate, send_mail
from poster import Post
import datetime

test_title = "[일반공지] [연구등록(B)] 2021학년도 2학기 연구등록(B) 등록 안내"
test_contents = "안녕하십니까? 일반대학원 수료생의 연구과제 참여를 위하여 2021학년도 2학기 연구등록(B) 제도를 운영하고 있습니다"
test_date = "2021-09-02"
test_time = "13:58:02"
test_link = "https://www.dongguk.edu/mbs/kr/jsp/board/view.jsp?spage=1&boardId=3646&boardSeq=26738970&id=kr_010802000000&column=&search=&categoryDepth=&mcategoryId=0"


test_posts = [ 
    Post("학사공지",test_title,test_contents,test_link,test_date),

    Post("일반공지",test_title,test_contents,test_link,test_date),

    Post("장학공지",test_title,test_contents,test_link,test_date),
    
    Post("정보통신공학과공지",test_title,test_contents,test_link,test_date),
    
    Post("공과대학공지",test_title,test_contents,test_link,test_date),
    
    Post("근로장학공고게시판",test_title,test_contents,test_link,test_date),
    ]

now = datetime.datetime.now()

test_subject = now.strftime("%Y/%m/%d - %H") + "시의 공지를 알려드려요."
print(test_subject)

template = BaseTemplate()
template.header_block(now.strftime("%m/%d/%Y"), now.strftime("%H:%M:%S"))

for post in test_posts:
    template.theme_block(post.theme)
    template.content_block(post)
    
template.end_block()
print(template.template)
send_mail(["madogisa12@naver.com"],test_subject,template.template)