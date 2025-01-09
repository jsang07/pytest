import requests
import json
from bs4 import BeautifulSoup as bs
import random

url = 'http://localhost:3000/save-data'

head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
req = requests.get("https://news.naver.com/breakingnews/section/105/230", headers=head)
html = req.text
soup = bs(html, "lxml")

articles = soup.select("#newsct > div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META > div > ul > li")

for article in articles:
    a = article.select_one("div > div > div.sa_text > a")
    title = article.select_one("div > div > div.sa_text > a > strong")
    try:
        response = requests.post(url, json={
            "link" : a['href'],
            "title" : title.text,
            "like" : random.randint(0, 50)
        })  

        if response.status_code == 200:
            print("데이터가 성공적으로 저장되었습니다.")
        else:
            print("오류 발생:", response.text)
    except Exception as e:
        print("요청 중 오류 발생:", str(e))
    


# try:
#     response = requests.get(url, json={})  

#     if response.status_code == 200:
#         print("데이터가 성공적으로 저장되었습니다.")
#     else:
#         print("오류 발생:", response.text)
# except Exception as e:
#     print("요청 중 오류 발생:", str(e))
