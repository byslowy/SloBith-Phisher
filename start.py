import os
import sys

def self_destruct():
    try:
        os.remove(sys.argv[0])
      
    except Exception as e:
        print(f"Hata olu�tu: {e}")

if __name__ == "__main__":
    print("\033[34mBu dosyay� bir kere kullanman�z yeterlidir!!!")
    time.sleep(1)
    os.system("clear")
    os.system("chmod +x slobit.py")
    os.system("pip install requests")
    os.system("clear")
    print("""\033[32m
    ###############################################################################
    # HER �EY TAMAM! SADECE "python slophis.py" diyerek tool'u �al��t�rabilirsiniz! #
    ###############################################################################
    """)
    self_destruct()