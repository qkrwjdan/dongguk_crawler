import requests
from bs4 import BeautifulSoup

import json 
import re

with open("url.json", encoding="utf-8") as json_file:
    urls = json.load(json_file)

page = requests.get(urls["근로장학공고게시판"]["url"],verify=False)
soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.find_all(urls["근로장학공고게시판"]["title"]["tag"],{"class" : urls["근로장학공고게시판"]["title"]["class"]})
dates = soup.find_all(urls["근로장학공고게시판"]["date"]["tag"],{"class" : urls["근로장학공고게시판"]["date"]["class"]})

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
