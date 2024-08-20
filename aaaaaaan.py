import requests
import time
from bs4 import BeautifulSoup

while True:
    username = input("ユーザー名")
    time.sleep(1)
    url = "https://scratch.mit.edu/users/"+username+"/"
    #print(url)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    #title = soup.find("h1").text
    #print(html)
    #print('404'in html)
    if '404'in html:
            print("存在しません")
            print("/")
    else:
            print("存在します:"+url)
            print("/")


