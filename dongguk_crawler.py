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

from mailer import send_mail
from poster import Post
from utils import preprocess_text, get_title_content_link, get_title_content_link_with_info, get_pre_data, check_exist

load_dotenv()

ALL_ROW_NUM = 25
COLUMN_NUM = 7
TITLE_COLUMN = 1
DATE_COLUMN = 3

if __name__ == "__main__":

    with open("url.json", encoding="utf-8") as json_file:
        urls = json.load(json_file)

    print(datetime.datetime.now(), "탐색을 시작합니다. ")

    send_data = []
    time.time()

    for info in urls:
        # data 가져오기 
        id = str(list(info.keys())[0])
        base_url = info[id]["base_url"]
        page = requests.get(info[id]["url"], verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        cleaned_results = []

        pre_data = get_pre_data(id)

        # data 정제
        if id in ["일반공지", "학사공지", "장학공지"]:
            results = soup.find_all("td")

            for ROW in range(ALL_ROW_NUM):
                title_tag = str(results[ROW * COLUMN_NUM + TITLE_COLUMN])
                date = str(results[ROW * COLUMN_NUM + DATE_COLUMN])

                title_soup = BeautifulSoup(title_tag,'html.parser').select_one('a')

                link = title_soup.attrs['href']
                url = base_url + "/" + link
                title, content, link = get_title_content_link(url)
                date = preprocess_text(date)
                title = preprocess_text(title)

                post = Post(id,title,content,url,date)

                if check_exist(pre_data, post):
                    # 이미 있음
                    pass
                else :
                    # 없음
                    send_data.append(post)

                    with open('data/'+id+".tsv","a",encoding="utf-8" ) as f:
                        t = post.title
                        
                        f.write(t+ "\t" + date +"\n")
                        print(t)

        elif id in ["공과대학공지", "정보통신공학과공지", "근로장학공고게시판"]:

            titles = soup.find_all(info[id]["title"]["tag"], {
                                info[id]["title"]["attr"]: info[id]["title"]["value"]})
            dates = soup.find_all(info[id]["date"]["tag"], {
                                info[id]["date"]["attr"]: info[id]["date"]["value"]})

            for title, date in zip(titles, dates):
                # print(title)
                title_soup = BeautifulSoup(str(title),'html.parser').select_one('a')
                link = title_soup.attrs["href"]
                if not link.startswith("http"):
                    link = base_url + link
                date = preprocess_text(str(date))
                title, content, url = get_title_content_link_with_info(link, info[id])
                content = preprocess_text(content)

                post = Post(id,title,content,url,date)
                
                if check_exist(pre_data, post):
                    # 이미 있음
                    pass
                else :
                    # 없음
                    send_data.append(post)

                    with open('data/'+id+".tsv","a",encoding="utf-8" ) as f:
                        print(post.title)
                        f.write(post.title+ "\t" + date +"\n")

    print("탐색 끝!")
    print(send_data)
            
        # # 메일로 보낼 내용 만들기
        # send_string = ""
        # for data in send_data:
        #     send_string += "위치 : {noti} , title: {title} , date: {date} \n".format(noti=data[0] , title=data[1], date=data[2])

        # # 메일 보내기
        # if send_string:
        #     print("메일을 보냅니다.")
        #     send_mail(["madogisa12@naver.com"],"제목",send_string)

        # time.sleep(3600)
