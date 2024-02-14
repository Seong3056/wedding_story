import requests

from bs4 import BeautifulSoup
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.common.by import By

import private_file.key as key


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

def search(address1, address2, keyword):
    params = {
    "query" : f"{address1} {address2} {keyword}",    
    }
    data_list = requests.get(url, params=params, headers=headers).json()["documents"]
    a_url = data_list[0]["place_url"]
    page = urlopen(a_url)
    soup = BeautifulSoup(page, "lxml")
    # data = requests.get(a_url).json()
    print(soup.prettify())
    
    return data_list

