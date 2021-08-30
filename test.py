import datetime

from mailer import BaseTemplate, send_mail
from poster import Post

template = BaseTemplate()
now = datetime.datetime.now()

template.header_block(now.strftime("%m/%d/%Y"), now.strftime("%H:%M:%S"))

title = "[일반공지] 동국가족 8월 고인추모기도 봉행 및 9월 고인추모기도 신청"
content = "[HI-SW봉사단] 비전공자 대상 프로그래밍 언어 튜터링 수요조사 안내 코딩을 처음 접하시는 학생, SW 강좌를 수강하며 어려움 또는 호기심이 있는 학생..."
date = "2021-08-12"
link = "https://www.dongguk.edu/mbs/kr/jsp/board/view.jsp?spage=1&boardId=3646&boardSeq=26738830&id=kr_010802000000&column=&search=&categoryDepth=&mcategoryId=0"

post = Post("일반공지",title,content,link,date)

template.theme_block("일반공지")

template.content_block(post)
template.content_block(post)
template.content_block(post)

template.end_block()

print(template.template)

send_mail(["madogisa12@naver.com"],"hi",template.template)