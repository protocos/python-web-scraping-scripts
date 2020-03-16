import time
import pickledb
import requests
import platform
from bs4 import BeautifulSoup
from selenium import webdriver
import os

minute = 60


def sleep(sleep_duration = 15 * minute):
    time.sleep(sleep_duration)


def scrape(url):
    print("Scraping url", url)
    return BeautifulSoup(requests.get(url, timeout=30).content, "html.parser")

def scrape_with_selenium(url):
    print("Scraping url with selenium", url)

    base_file_path = str(os.getcwd())
    geckodriver_path = base_file_path + '/geckodriver'

    operating_system = platform.system()
    if operating_system == "Darwin":
        geckodriver_path = base_file_path + '/macOS/geckodriver'
    if operating_system == "Linux":
        geckodriver_path = base_file_path + '/linux/geckodriver'

    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    browser = webdriver.Firefox(executable_path=geckodriver_path, firefox_options=options)
    browser.get(url)
    html = browser.page_source
    browser.quit()
    return BeautifulSoup(html, "html.parser")

def href_has_not_been_logged(href):
    return href not in get_hrefs()


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


def send_notification(value1="New match found!", value2="", value3=""):
    requests.get(notification_endpoint + "?value1=" + value1 + "&value2=" + value2 + "&value3=" + value3, timeout=30)


def check_href_and_send_notification(value1, value2, value3):
    if value3 not in get_hrefs():
        send_notification(value1, value2, value3)
        add_href(value3)


def check_key_and_send_notification(event_name, key, value1, value2, value3):
    if key not in get_hrefs():
        requests.get("https://maker.ifttt.com/trigger/"+event_name+"/with/key/VzmWoFF515H4lf0MNNVyo?value1=" + value1 + "&value2=" + value2 + "&value3=" + value3,
                     timeout=30)
        add_href(key)
