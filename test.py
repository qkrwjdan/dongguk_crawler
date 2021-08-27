import requests 

import requests
from bs4 import BeautifulSoup
import pandas

from w3lib.html import remove_tags

import json
import re
import csv

url = "https://www.dongguk.edu/mbs/kr/jsp/board/view.jsp?spage=1&boardId=3662&boardSeq=26738454&id=kr_010804000000&column=&search=&categoryDepth=&mcategoryId=0"
print("get")
page = requests.get(url)
print(page)
content = remove_tags(page.content)
cont = BeautifulSoup(content,'html.parser')
print(cont)