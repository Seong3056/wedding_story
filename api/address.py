import requests

from bs4 import BeautifulSoup
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.common.by import By

import private_file.key as key
import re

url = "https://dapi.kakao.com/v2/local/search/keyword.json"
headers = {
    "Authorization": "KakaoAK "+key.kakao_key,
    "content-type": "application/json;charset=UTF-8"
}
params = {
    "query" : "서울 마포구 웨딩",    
}

data_list = requests.get(url, params=params, headers=headers).json()["documents"]
print(data_list)

# url = data_list["place_url"]
# print(url)
# data = requests.get(url).json()

def search(address1="서울시", address2="마포구", keyword="웨딩홀"):
    data = []
    params = {
    "query" : f"{address1} {address2} {keyword}",    
    }
    data_list = requests.get(url, params=params, headers=headers).json()["documents"]
    for i in data_list:
        a_url = i["place_url"]
        url1 = a_url[:a_url.rindex("/")]
        url2 = a_url[a_url.rindex("/")+1:]
        f_url = f"{url1}/main/v/{url2}"
        res = requests.get(f_url).json()["basicInfo"]
        # img_url = res["mainphotourl"]
        
        d = dict()
        d["place_url"] = i["place_url"]
        d["place_name"] = i["place_name"]
        d["img_url"] = res.get("mainphotourl") if res.get("mainphotourl") != None else "https://png.pngtree.com/png-clipart/20190119/ourmid/pngtree-wedding-marry-newcomer-happy-event-png-image_469605.jpg"
        
        data.append(d)
    
    
# https://place.map.kakao.com/main/v/1282059086
# http://place.map.kakao.com/1282059086
    
    return data

