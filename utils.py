import re
import requests
from bs4 import BeautifulSoup


def preprocess_text(text):
    text = re.sub('<.+?>', '', text, 0)
    text = re.compile('\[[A-za-z가-힣 ]+\]').sub('',
                                               text).replace(',', '').replace("\r\n", "").replace("\r","").strip()
    return text


def get_title_content_link(url):
    page = requests.get(url)
    raw = page.content
    raw = raw.decode("utf-8").replace("[data-hwpjson]","")
    soup = BeautifulSoup(raw,'html.parser')

    title = soup.find("th").text.strip().replace("\n","").replace("\t","")
    content = soup.find(class_="memo").text.strip()[:50]
    link = url

    return title, content, link

def get_title_content_link_with_info(url, info):
    page = requests.get(url,verify=False)
    raw = page.content
    soup = BeautifulSoup(raw,'html.parser')

    title = soup.find(info["detail_title"]["tag"], {info["detail_title"]["attr"]:info["detail_title"]["value"]})
    content = soup.find(info["detail_content"]["tag"], {info["detail_content"]["attr"]:info["detail_content"]["value"]})

    tit = title.text.strip().replace("\t","")
    cont = content.text.strip().replace("\t","")[:50]
    link = url

    return tit, cont, link

def get_pre_data(id):
    # 기존 data 가져오기
    pre_data = []
    file_name = 'data/'+id+".tsv"
    with open(file_name, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            pre_data.append(line.split("\t"))

    pre_data.reverse()
    return pre_data

def check_exist(pre_data, post):
    for data in pre_data:
        title = data[0]
        # print(title+"vs"+post.title)
        if title == post.title:
            return True

    return False
