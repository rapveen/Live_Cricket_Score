import requests
from bs4 import BeautifulSoup
from lxml import html
from twilio.rest import Client
from time import sleep
##def sendmessage(title, message):
##    pynotify.init("Test")
##    notice = pynotify.Notification(title, message)
##    notice.show()
##    return
def sendscore(body):
    #Your account_sid goes here
    account_sid = "AC82e55ea2ab6d69fbb46220358786ac3d"
    #Your authorization token goes here
    auth_token = "a298a5ea1f3f7ecaeeca8d59d24ec45d"
    client = Client(account_sid, auth_token)
    #to = "number to which SMS should be sent",from_="your twilio number"
    message = client.messages.create(body=body,to="+918539871060",from_="+1 256-906-5590")
    print(message.body)
url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    data = soup.find_all("description")
    score = data[0].text
    #data = "our friends, our world-our only world.#friends4life-our friends for life!Join the big celebratioin & wear your friendship-check www.friends4life.in"
    #print score
    sendscore(score)
    #break
    sleep(60)
