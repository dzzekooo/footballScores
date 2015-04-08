import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
url = "http://www.livescore.com/soccer/spain/primera-division/atletico-madrid-vs-real-sociedad/1-1778324/"

while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text)
    scores = soup.findAll("div", { "class" :"sco"})
    score = scores[0].text
    times = soup.findAll("div", { "class" :"min"})
    time=times[0].text
	
    teams = soup.findAll("div", { "class" :"ply"})
    home=teams[0].text  
    away=teams[1].text

    msg= "Time" + time + "    "+ home + " " + score + " " + away
    sendmessage("Score", msg)
    sleep(60)                  
