import requests
import time
from bs4 import BeautifulSoup

while True:
    username = input("ユーザー名")
    time.sleep(1)
    url = "https://scratch.mit.edu/users/"+username+"/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    if '404'in html:
            print("存在しません")
            print("/")
    else:
            print("存在します:"+url)
            print("/")


