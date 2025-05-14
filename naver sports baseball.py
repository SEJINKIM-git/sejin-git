import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/kbaseball/index"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# 결과 확인 (예: 제목 출력)
print(soup.title.text)
