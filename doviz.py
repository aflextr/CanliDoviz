import time
import requests
import os
from bs4 import BeautifulSoup

try:
    def dolar():
        r = requests.get("https://piyasa.paratic.com/doviz/dolar/")
        Soup = BeautifulSoup(r.content,"html.parser")
        sonuc = Soup.find("span",attrs={"data-code":"USD/TRL"}).text
        print("Dolar : "+sonuc+"\n")
        r.close()
    def euro():
        r1 = requests.get("https://piyasa.paratic.com/doviz/euro/")
        Soup1 = BeautifulSoup(r1.content,"html.parser")
        sonuc2 =Soup1.find("span",attrs={"data-code":"EUR/TRL"}).text
        print("Euro : "+sonuc2+"\n")
        r1.close()
    def sterlin():
        r2 = requests.get("https://piyasa.paratic.com/doviz/sterlin/")
        Soup2 = BeautifulSoup(r2.content,"html.parser")
        sonuc3 = Soup2.find("span",attrs={"data-code":"GBP/TRL"}).text
        print("Sterlin : "+sonuc3+"\n")
        r2.close()
    def ekranitemizle():
        os.system("clear")
        pass
        

    """
    Kripto paralar üzerinde yakında daha fazla özellik eklenecektir.

    def bitcoin():
        r3 = requests.get("https://piyasa.paratic.com/kripto-coin/bitcoin/")
        Soup3 = BeautifulSoup(r3.content,"html.parser")
        Sonuc4 = Soup3.find("span",attrs={"data-code":"BTCTRY"}).text
        print("Bitcoin :"+Sonuc4)
        r3.close()
    """
    pass
except:
    print("İnternet Erişimi gitti veyahut teknik bir hata oluştu.")
    pass




"""
def yorum():
    Canlı Yorum için çalışmalara yakında başlayacağım.
    link = "https://yorum.altin.in/tum/dolar"
    req = requests.get(link)
    Soupy = BeautifulSoup(req.content,"lxml")
    yorumfind = Soupy.find("span",attrs={"class":"ici"}).text
    print(yorumfind)

"""    

while True:  
    dolar()
    euro()
    sterlin()
    time.sleep(6)
    ekranitemizle()
    pass