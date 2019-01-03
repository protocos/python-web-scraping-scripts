import time
import pickledb
import requests
from bs4 import BeautifulSoup

minute = 60
def sleep(sleep_duration = 15 * minute):
    time.sleep(sleep_duration)

def scrape(url):
    return BeautifulSoup(requests.get(url, timeout=30).content, "html.parser")

def get_hrefs():
    db = pickledb.load('storage.db', False)
    hrefs = db.get('hrefs')
    if hrefs is None:
        hrefs = []
    return hrefs

def add_href(href):
    db = pickledb.load('storage.db', False)
    hrefs = db.get('hrefs')
    if hrefs is None:
        hrefs = []
    if href.startswith("http://") or href.startswith("https://"):
        if href not in hrefs:
            hrefs.append(href)
    db.set('hrefs', hrefs)
    db.dump()

def clear_hrefs():
    db = pickledb.load('storage.db', False)
    hrefs = []
    db.set('hrefs', hrefs)
    db.dump()

notification_endpoint = "https://maker.ifttt.com/trigger/news/with/key/VzmWoFF515H4lf0MNNVyo"
def send_notification(value1 = "New match found!", value2 = "", value3 = ""):
    requests.get(notification_endpoint + "?value1=" + value1 + "&value2=" + value2 + "&value3=" + value3, timeout=30)

def check_href_and_send_notification(value1, value2, value3):
    if value3 not in get_hrefs():
        send_notification(value1, value2, value3)
        add_href(value3)
