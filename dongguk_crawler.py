import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import json
import re
import os
import smtplib
from email.mime.text import MIMEText
import warnings
import time
import datetime
warnings.filterwarnings('ignore')

load_dotenv()

ALL_ROW_NUM = 25
COLUMN_NUM = 7
TITLE_COLUMN = 1
DATE_COLUMN = 3


def preprocess_text(text):
    text = re.sub('<.+?>', '', text, 0)
    text = re.compile('\[[A-za-z가-힣 ]+\]').sub('',
                                               text).replace(',', '').strip()
    return text


def send_mail(receivers, subject, content):

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('park.boong.u@gmail.com', os.getenv('MAIL_PASSWORD'))

    for receiver in receivers:
        msg = MIMEText(content)
        msg['Subject'] = subject
        s.sendmail('park.boong.u@gmail.com', receiver, msg.as_string())

    s.quit()


with open("url.json", encoding="utf-8") as json_file:
    urls = json.load(json_file)

while True:
    print(datetime.datetime.now(), "탐색을 시작합니다. ")

    send_data = []
    time.time()

    for info in urls:
        # data 가져오기 
        id = str(list(info.keys())[0])
        page = requests.get(info[id]["url"], verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        cleaned_results = []

        # data 정제
        if id in ["일반공지", "학사공지", "장학공지"]:

            results = soup.find_all("td")

            for ROW in range(ALL_ROW_NUM):
                title = str(results[ROW * COLUMN_NUM + TITLE_COLUMN])
                date = str(results[ROW * COLUMN_NUM + DATE_COLUMN])

                title = preprocess_text(title)
                date = preprocess_text(date)

                cleaned_results.append([title, date])

        elif id in ["공과대학공지", "정보통신공학과공지", "근로장학공고게시판"]:

            titles = soup.find_all(info[id]["title"]["tag"], {
                                "class": info[id]["title"]["class"]})
            dates = soup.find_all(info[id]["date"]["tag"], {
                                "class": info[id]["date"]["class"]})

            for title, date in zip(titles, dates):
                title = preprocess_text(str(title))
                date = preprocess_text(str(date))

                cleaned_results.append([title, date])

        # 기존 data 가져오기
        pre_data = []
        file_name = 'data/'+id+".tsv"
        with open(file_name, "r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                pre_data.append(line.split("\t"))

        pre_data.reverse()

        # data 비교하기

        for [title, date] in cleaned_results:

            isExist = False
            for pre in pre_data:
                if str(title) == str(pre[0]):
                    isExist = True
                    break

            if not isExist:

                print(title+"이 존재하지 않습니다.")

                send_data.append([id,title,date])

                with open('data/'+id+".tsv", "a") as f:
                    f.write(title + "\t" + date + "\n")
        
    # 메일로 보낼 내용 만들기
    send_string = ""
    for data in send_data:
        send_string += "위치 : {noti} , title: {title} , date: {date} \n".format(noti=data[0] , title=data[1], date=data[2])

    # 메일 보내기
    if send_string:
        print("메일을 보냅니다.")
        send_mail(["madogisa12@naver.com"],"제목",send_string)

    time.sleep(3600)
