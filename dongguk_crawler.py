import requests
from bs4 import BeautifulSoup

import json 
import re

with open("url.json", encoding="utf-8") as json_file:
    urls = json.load(json_file)

for info in urls:
    id = str(list(info.keys())[0])
    # print(info)

    if id in ["일반공지","학사공지","장학공지"]:
        page = requests.get(info[id]["url"])
        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find_all("td")

        cleaned_results = []

        for i in range(25):
            title = str(results[i*7 + 1])
            date = str(results[i*7 + 3])

            # remove html tag
            title = re.sub('<.+?>', '', title, 0)
            date = re.sub('<.+?>', '', date, 0)

            # remove etc words
            title = re.compile('\[[A-za-z가-힣 ]+\]').sub('', title).replace(',','').strip()
            date = re.compile('\[[A-za-z가-힣 ]+\]').sub('', date).replace(',','').strip()

            cleaned_results.append([title,date])

        for i in cleaned_results:
            print(i)

    elif id in ["공과대학공지","정보통신공학과공지","근로장학공고게시판"]:
        page = requests.get(info[id]["url"],verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        titles = soup.find_all(info[id]["title"]["tag"],{"class" : info[id]["title"]["class"]})
        dates = soup.find_all(info[id]["date"]["tag"],{"class" : info[id]["date"]["class"]})

        cleaned_results = []

        for title, date in zip(titles,dates):
            title = str(title)
            date = str(date)

            # remove html tag
            title = re.sub('<.+?>', '', title, 0)
            date = re.sub('<.+?>', '', date, 0)

            # remove etc words
            title = re.compile('\[[A-za-z가-힣 ]+\]').sub('', title).replace(',','').strip()
            date = re.compile('\[[A-za-z가-힣 ]+\]').sub('', date).replace(',','').strip()

            cleaned_results.append([title,date])

        for i in cleaned_results:
            print(i)

