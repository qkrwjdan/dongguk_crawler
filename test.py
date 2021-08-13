import requests 

import requests
from bs4 import BeautifulSoup
import pandas

import json
import re
import csv

with open("url.json", encoding="utf-8") as json_file:
    urls = json.load(json_file)

print(list(urls[0].keys())[0])