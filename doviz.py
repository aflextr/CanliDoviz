import time
import requests
import os
from bs4 import BeautifulSoup



class Doviz(object):
    try:
        def dolar():
            r = requests.get("https://piyasa.paratic.com/doviz/dolar/")
            Soup = BeautifulSoup(r.content,"html.parser")
            sonuc = Soup.find("span",attrs={"data-code":"USD/TRL"}).text
            print("Dolar : "+sonuc+"\n")
            r.close()
            pass
        def euro():
            r = requests.get("https://piyasa.paratic.com/doviz/euro/")
            Soup = BeautifulSoup(r.content,"html.parser")
            sonuc =Soup.find("span",attrs={"data-code":"EUR/TRL"}).text
            print("Euro : "+sonuc+"\n")
            r.close()
            pass
        def sterlin():
            r = requests.get("https://piyasa.paratic.com/doviz/sterlin/")
            Soup = BeautifulSoup(r.content,"html.parser")
            sonuc = Soup.find("span",attrs={"data-code":"GBP/TRL"}).text
            print("Sterlin : "+sonuc+"\n")
            r.close()
            pass
        def cinyuan():
            r = requests.get("https://piyasa.paratic.com/doviz/cin-yuani/")
            Soup = BeautifulSoup(r.content,"html.parser")
            sonuc = Soup.find("span",attrs={"data-code":"SCNY"}).text
            print("Çin Yuanı : "+sonuc+"\n")
            r.close()
            pass
        def isvicre():
            r = requests.get("https://piyasa.paratic.com/doviz/isvicre-frangi/")
            Soup = BeautifulSoup(r.content,"html.parser")
            sonuc = Soup.find("span",attrs={"data-code":"SCHF"}).text
            print("İsviçre Frangı : "+sonuc+"\n")
            r.close()
            pass
        pass
    except:
        print("İnternet Erişimi gitti veyahut teknik bir hata oluştu.")
        pass
    pass

class Altin(object):
    try:
        def ons():
            r = requests.get("https://piyasa.paratic.com/altin/ons/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            print("ONS : ALIŞ: "+alisduzelt+"         SATIŞ: "+satisduzelt)
            r.close()
            pass
        def gram():
            r = requests.get("https://piyasa.paratic.com/altin/gram/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            print("GRAM : ALIŞ: "+alisduzelt+"         SATIŞ: "+satisduzelt)
            r.close()
            pass
        def ceyrek():
            r = requests.get("https://piyasa.paratic.com/altin/ceyrek/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            print("ÇEYREK : ALIŞ: "+alisduzelt+"         SATIŞ: "+satisduzelt)
            r.close()
            pass
        def cumhuriyet():
            r = requests.get("https://piyasa.paratic.com/altin/cumhuriyet/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            print("CUMHURİYET : ALIŞ: "+alisduzelt+"         SATIŞ: "+satisduzelt)
            r.close()
            pass
        def yarim():
            r = requests.get("https://piyasa.paratic.com/altin/yarim/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            print("YARIM : ALIŞ: "+alisduzelt+"         SATIŞ: "+satisduzelt)
            r.close()
            pass
        pass
    except:
        print("İnternet Erişimi gitti veyahut teknik bir hata oluştu.")
        pass
   
    pass

class Borsa(object):
    try:
        def bist100():
            r = requests.get("https://piyasa.paratic.com/borsa/xu100-bist-100/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("div",attrs={"data-type":"last"}).text
            sonduzelt = str(son).strip()
            print("BİST100 : SON : "+sonduzelt)
            r.close()
            pass
        def bist50():
            r = requests.get("https://piyasa.paratic.com/borsa/xu050-bist-50/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("div",attrs={"data-type":"last"}).text
            sonduzelt = str(son).strip()
            print("BİST50 : SON : "+sonduzelt)
            r.close()
            pass
        def bist30():
            r = requests.get("https://piyasa.paratic.com/borsa/xu030-bist-30/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("div",attrs={"data-type":"last"}).text
            sonduzelt = str(son).strip()
            print("BİST30 : SON : "+sonduzelt)
            r.close()
            pass
        def banka():
            r = requests.get("https://piyasa.paratic.com/borsa/xbank-banka/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("div",attrs={"data-type":"last"}).text
            sonduzelt = str(son).strip()
            print("BANKA : SON : "+sonduzelt)
            r.close()
            pass
        def bilisim():
            r = requests.get("https://piyasa.paratic.com/borsa/xblsm-bilisim/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("div",attrs={"data-type":"last"}).text
            sonduzelt = str(son).strip()
            print("BİLİŞİM : SON : "+sonduzelt)
            r.close()
            pass
        pass
    except:
        print("İnternet Erişimi gitti veyahut teknik bir hata oluştu.")
        pass
    
    pass

class Hisse(object):
    try:
        def akbank():
            r = requests.get("https://piyasa.paratic.com/hisse-senetleri/akbnk/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            hacim = Soup.find("span",attrs={"data-type":"hacimtl"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            hacimduzelt = str(hacim).strip()
            print("AKBANK : ALIŞ: "+alisduzelt+"      SATIŞ: "+satisduzelt + "      HACİM: " +hacimduzelt)
            r.close()
        pass
        def arcelik():
            r = requests.get("https://piyasa.paratic.com/hisse-senetleri/arclk/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            hacim = Soup.find("span",attrs={"data-type":"hacimtl"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            hacimduzelt = str(hacim).strip()
            print("ARÇELİK : ALIŞ: "+alisduzelt+"      SATIŞ: "+satisduzelt + "      HACİM: " +hacimduzelt)
            r.close()
            pass
        def aselsan():
            r = requests.get("https://piyasa.paratic.com/hisse-senetleri/asels/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            hacim = Soup.find("span",attrs={"data-type":"hacimtl"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            hacimduzelt = str(hacim).strip()
            print("ASELSAN : ALIŞ: "+alisduzelt+"      SATIŞ: "+satisduzelt + "      HACİM: " +hacimduzelt)
            r.close()
            pass
        def bim():
            r = requests.get("https://piyasa.paratic.com/hisse-senetleri/bimas/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            hacim = Soup.find("span",attrs={"data-type":"hacimtl"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            hacimduzelt = str(hacim).strip()
            print("BİM : ALIŞ: "+alisduzelt+"      SATIŞ: "+satisduzelt + "      HACİM: " +hacimduzelt)
            r.close()
            pass
        def doganholding():
            r = requests.get("https://piyasa.paratic.com/hisse-senetleri/dohol/")
            Soup = BeautifulSoup(r.content,"html.parser")
            alis = Soup.find("div",attrs={"data-type":"bid"}).text
            satis = Soup.find("div",attrs={"data-type":"ask"}).text
            hacim = Soup.find("span",attrs={"data-type":"hacimtl"}).text
            alisduzelt = str(alis).strip()
            satisduzelt = str(satis).strip()
            hacimduzelt = str(hacim).strip()
            print("DOGAN HOLDİNG : ALIŞ: "+alisduzelt+"      SATIŞ: "+satisduzelt + "      HACİM: " +hacimduzelt)
            r.close()
            pass
        pass
    except:
        print("İnternet Erişimi gitti veyahut teknik bir hata oluştu.")
        pass
    pass

class Kripto(object):
    try:
        def bitcoin():
            r = requests.get("https://piyasa.paratic.com/kripto-coin/bitcoin/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("span",attrs={"data-code":"BTCTRY"}).text
            sonduzelt = str(son).strip()
            print("BİTCOİN : "+sonduzelt)
            r.close()
            pass
        def ethereum():
            r = requests.get("https://piyasa.paratic.com/kripto-coin/ethereum/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("span",attrs={"data-code":"ETHTRY"}).text
            sonduzelt = str(son).strip()
            print("ETHEREUM : "+sonduzelt)
            r.close()
            pass
        def litecoin():
            r = requests.get("https://piyasa.paratic.com/kripto-coin/litecoin/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("span",attrs={"data-code":"LTCTRY"}).text
            sonduzelt = str(son).strip()
            print("LİTECOİN : "+sonduzelt)
            r.close()
            pass
        def ripple():
            r = requests.get("https://piyasa.paratic.com/kripto-coin/ripple/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("span",attrs={"data-code":"XRPTRY"}).text
            sonduzelt = str(son).strip()
            print("RİPPLE : "+sonduzelt)
            r.close()
            pass
        def bitcoincash():
            r = requests.get("https://piyasa.paratic.com/kripto-coin/bitcoin-cash/")
            Soup = BeautifulSoup(r.content,"html.parser")
            son = Soup.find("span",attrs={"data-code":"BCHTRY"}).text
            sonduzelt = str(son).strip()
            print("BİTCOİN CASH : "+sonduzelt)
            r.close()
            pass
        pass
    except:
        print("İnternet Erişimi gitti veyahut teknik bir hata oluştu.")
        pass
    pass


class Yorumlar(object):
    try:
        def dolaryorum():
            req = requests.get("https://piyasa.paratic.com/doviz/dolar/")
            Soupy = BeautifulSoup(req.content,"html.parser")
            yorumatan = Soupy.find("div",attrs={"class":"cb_nick"}).text
            yorumfind = Soupy.find("div",attrs={"class":"cb_content"}).text
            yorumzaman = Soupy.find("div",attrs={"class":"cb_date"}).text
            yorumfindduzelt = str(yorumfind).strip()
            yorumatanduzelt = str(yorumatan).strip()
            print("DOLAR YORUMLARI: \n")
            print("Kullanıcı adı: "+yorumatanduzelt+"\n"+"Zaman: "+yorumzaman+"\n"+"Mesaj:  "+yorumfindduzelt)
            req.close()
            pass
        def altinyorum():
            req = requests.get("https://piyasa.paratic.com/altin/")
            Soupy = BeautifulSoup(req.content,"html.parser")
            yorumatan = Soupy.find("div",attrs={"class":"cb_nick"}).text
            yorumfind = Soupy.find("div",attrs={"class":"cb_content"}).text
            yorumzaman = Soupy.find("div",attrs={"class":"cb_date"}).text
            yorumfindduzelt = str(yorumfind).strip()
            yorumatanduzelt = str(yorumatan).strip()
            print("ALTIN YORUMLARI: \n")
            print("Kullanıcı adı: "+yorumatanduzelt+"\n"+"Zaman: "+yorumzaman+"\n"+"Mesaj:  "+yorumfindduzelt)
            req.close()
            pass
        def borsayorum():
            req = requests.get("https://piyasa.paratic.com/borsa/")
            Soupy = BeautifulSoup(req.content,"html.parser")
            yorumatan = Soupy.find("div",attrs={"class":"cb_nick"}).text
            yorumfind = Soupy.find("div",attrs={"class":"cb_content"}).text
            yorumzaman = Soupy.find("div",attrs={"class":"cb_date"}).text
            yorumfindduzelt = str(yorumfind).strip()
            yorumatanduzelt = str(yorumatan).strip()
            print("BORSA YORUMLARI: \n")
            print("Kullanıcı adı: "+yorumatanduzelt+"\n"+"Zaman: "+yorumzaman+"\n"+"Mesaj:  "+yorumfindduzelt)
            req.close()
            pass
        def hisseyorum():
            req = requests.get("https://piyasa.paratic.com/hisse-senetleri/")
            Soupy = BeautifulSoup(req.content,"html.parser")
            yorumatan = Soupy.find("div",attrs={"class":"cb_nick"}).text
            yorumfind = Soupy.find("div",attrs={"class":"cb_content"}).text
            yorumzaman = Soupy.find("div",attrs={"class":"cb_date"}).text
            yorumfindduzelt = str(yorumfind).strip()
            yorumatanduzelt = str(yorumatan).strip()
            print("HİSSE YORUMLARI: \n")
            print("Kullanıcı adı: "+yorumatanduzelt+"\n"+"Zaman: "+yorumzaman+"\n"+"Mesaj:  "+yorumfindduzelt)
            req.close()
            pass
        def kriptoyorum():
            req = requests.get("https://piyasa.paratic.com/kripto-coin/")
            Soupy = BeautifulSoup(req.content,"html.parser")
            yorumatan = Soupy.find("div",attrs={"class":"cb_nick"}).text
            yorumfind = Soupy.find("div",attrs={"class":"cb_content"}).text
            yorumzaman = Soupy.find("div",attrs={"class":"cb_date"}).text
            yorumfindduzelt = str(yorumfind).strip()
            yorumatanduzelt = str(yorumatan).strip()
            print("KRİPTO YORUMLARI: \n")
            print("Kullanıcı adı: "+yorumatanduzelt+"\n"+"Zaman: "+yorumzaman+"\n"+"Mesaj:  "+yorumfindduzelt)
            req.close()
            pass
        pass
    except:
        print("İnternet Erişimi gitti veyahut teknik bir hata oluştu.")
        pass
    pass

def ekranitemizle():
    os.system("clear")
    pass




class calistir(object):
    def doviz():
        while True:
            Doviz.dolar()
            Doviz.euro()
            Doviz.sterlin()
            Doviz.cinyuan()
            Doviz.isvicre()
            Yorumlar.dolaryorum()
            time.sleep(10)
            ekranitemizle()
            pass
        pass
    def altin():
        while True:
            Altin.ons()
            Altin.cumhuriyet()
            Altin.yarim()
            Altin.ceyrek()
            Altin.gram()
            Yorumlar.altinyorum()
            time.sleep(10)
            ekranitemizle()
            pass
        pass
    def borsa():
        while True:
            Borsa.bist100()
            Borsa.bist50()
            Borsa.bist30()
            Borsa.banka()
            Borsa.bilisim()
            Yorumlar.borsayorum()
            time.sleep(10)
            ekranitemizle()
            pass
        pass
    def hisse():
        while True:
            Hisse.akbank()
            Hisse.arcelik()
            Hisse.bim()
            Hisse.aselsan()
            Hisse.doganholding()
            Yorumlar.hisseyorum()
            time.sleep(10)
            ekranitemizle()
            pass
        pass
    def kripto():
        while True:
            Kripto.bitcoin()
            Kripto.ethereum()
            Kripto.litecoin()
            Kripto.ripple()
            Kripto.bitcoincash()
            Yorumlar.kriptoyorum()
            time.sleep(10)
            ekranitemizle()
            pass
        pass
    pass




def main():
    print("1-DÖVİZ")
    print("2-ALTIN FİYATLARI")
    print("3-BORSA")
    print("4-HİSSE SENETLERİ")
    print("5-KRİPTO PARALAR")
    
    secim = int(input("SEÇİM : "))
    try:
        if secim == 1:
            calistir.doviz()
            pass
        elif secim == 2:
            calistir.altin()
            pass
        elif secim == 3:
            calistir.borsa()
            pass
        elif secim == 4:
            calistir.hisse()
            pass
        elif secim == 5:
            calistir.kripto()
            pass
            pass
        else:
            print("Lütfen uygun değerleri giriniz.")
            pass
        pass
    except:
        print("Bir hata oluştu")
        pass
    

    pass


main()

