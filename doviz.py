import time
import requests
from bs4 import BeautifulSoup

def dolar():
    URL = "https://piyasa.paratic.com/doviz/dolar/"
    r = requests.get(URL)
    Soup = BeautifulSoup(r.content,"lxml")
    sonuc = Soup.find("span",attrs={"data-code":"USD/TRL"}).text
    print("Dolar : "+sonuc,end=" ")
def euro():
    URL1 = "https://piyasa.paratic.com/doviz/euro/"
    r1 = requests.get(URL1)
    Soup1 = BeautifulSoup(r1.content,"lxml")
    sonuc2 =Soup1.find("span",attrs={"data-code":"EUR/TRL"}).text
    print("Euro : "+sonuc2,end=" ")
def sterlin():
    URL2 = "https://piyasa.paratic.com/doviz/sterlin/"
    r2 = requests.get(URL2)
    Soup2 = BeautifulSoup(r2.content,"lxml")
    sonuc3 = Soup2.find("span",attrs={"data-code":"GBP/TRL"}).text
    print("Sterlin : "+sonuc3,end=" ")
def bitcoin():
    URL3 = "https://piyasa.paratic.com/kripto-coin/bitcoin/"
    r3 = requests.get(URL3)
    Soup3 = BeautifulSoup(r3.content,"lxml")
    Sonuc4 = Soup3.find("span",attrs={"data-code":"BTCTRY"}).text
    print("Bitcoin :"+Sonuc4+"\n"+"\n")
"""
def yorum():
    link = "https://yorum.altin.in/tum/dolar"
    req = requests.get(link)
    Soupy = BeautifulSoup(req.content,"lxml")
    yorumfind = Soupy.find("span",attrs={"class":"ici"}).text
    print(yorumfind)

"""
for i in range (9999):
    time.sleep(4)
    dolar()
    euro()
    sterlin()
    bitcoin()

