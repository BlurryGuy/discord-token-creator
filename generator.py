import requests as rq
from capmonster_python import HCaptchaTask
import json
import os
import string
import random
import sys
import time
import base64
from colorama import *
from threading import Thread
os.system("color a")
init()
import random

def getRandomFile(path):
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  return files[index]

file = open("tokenz.txt", "a")
def rc(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
def printy(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.010)
printy("Whats your capmonster.cloud API Key ? : ")
key = input("")
names = rq.get("https://api.namefake.com/").json().get("name")
print(names)
def generate():
 the_name = getRandomFile("pfps")
 hacking = open("pfps/"+the_name, "rb")

 name = rc(10)
 password = rc(14) + "A$1"
 usernametho = names
 lines = open('proxies.txt').read().splitlines()
 f = True
 encoded = base64.b64encode(hacking.read())
 PROXY = random.choice(lines)
 proxies = {'http': f"{PROXY}",'https': f"{PROXY}",}
 finger = rq.get("https://discordapp.com/api/v9/experiments")
 if f == True :
  jsonz=finger.json()
  print(finger.status_code)
  print(finger.reason)
  fingerprint = jsonz.get('fingerprint')
 
  header = {
                        "accept": "*/*",
                        'accept-encoding': 'gzip, deflate, br',
                        "accept-language": "en-GB",
                        "content-length": "90",
                        "content-type": "application/json",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        }

  capmonster = HCaptchaTask(key)
  task_id = capmonster.create_task("https://discord.com/register", "4c672d35-0701-42b2-88c3-78380b0db560")
  responsez = capmonster.join_task_result(task_id)
  responsen = responsez.get("gRecaptchaResponse")
  print(Fore.BLUE + "----------------------")
  print(Fore.GREEN + "[+] - Solved 1 Captcha")
  print(Fore.BLUE + "----------------------")
  datas = json.dumps({
            "fingerprint": fingerprint,
            "promotional_email_opt_in": "false",
            "email": name+"@gmail.com",
            "username": usernametho,
            "password": password,
            "consent": True,
            "gift_code_sku_id": "null",
            "date_of_birth": "2000-03-01",
            "captcha_service": "hcaptcha",
            "captcha_key": responsen
  })
  create = rq.post('https://discord.com/api/v9/auth/register', headers=header, data=datas)
  print(create.reason)
  print(create.status_code)
  print(create.text)
  gett=create.json()
  tokenz = gett.get('token')
  token = tokenz[:-5] + "*****"
  print(Fore.BLUE + "----------------------")
  print(Fore.GREEN + f"[+] Created {Fore.YELLOW} - {Fore.WHITE} {token} - {name}@gmail.com:{password}")
  print(Fore.BLUE + "----------------------")
  cool = json.dumps({
  "avatar": f"data:image/png;base64,${encoded}"
  })
  yez = {
                        "accept": "*/*",
                        'accept-encoding': 'gzip, deflate, br',
                        "accept-language": "en-GB",
                        "content-type": "application/json",
                        "authorization": tokenz,
       }
  set_pfp = rq.patch("https://discord.com/api/v9/users/@me", headers=yez, data=cool)
  print(set_pfp.status_code)
  print(set_pfp.reason)
  print(set_pfp.text)
  j = set_pfp.json()
  user = j.get("username")
  dis = j.get("discriminator")
  print(Fore.BLUE + "----------------------")
  print(Fore.GREEN + f"[+] {Fore.YELLOW} {Fore.WHITE} - Set Random Avatar to {user}#{dis}")
  print(Fore.BLUE + "----------------------")
  file.write("\n" + tokenz)
generate()
#while True:
     # try:
       #time.sleep(1)
       #runy = Thread(target=generate, args=())
      # runy.run()
      #except:
      # print("Proxy could not connect! Retrying")