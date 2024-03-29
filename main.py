import uservariables
from os import path
import requests
from time import sleep

TOKEN = uservariables.botToken
chat_id = uservariables.chatID
find = uservariables.path
message0 = "Hard Drive is down"
message1 = "Hard Drive is up"
check = None
sent = None

sleep(60) # this sleep is probably a little too long but at least it doesnt fail as a service on reboot anymore
while True:
    if not path.exists(find):
        check = 0
        if not sent == 0:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message0}"
            print(requests.get(url).json())  # this sends the message
            sent = 0
    elif path.exists(find):
        check = 1
        if not sent == 1:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message1}"
            print(requests.get(url).json())  # this sends the message
            sent = 1
