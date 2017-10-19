
import requests
from bs4 import BeautifulSoup

scrape_url = "https://www.ebay.com/sch/i.html?_udlo=100&_udhi=270&_mPrRngCbx=1&_from=R40&_sacat=0&_nkw=ipad+5th+generation+-mini+-broken+-air+space+gray&rt=nc&LH_BIN=1"

notification_endpoint = "https://maker.ifttt.com/trigger/notification/with/key/VzmWoFF515H4lf0MNNVyo?value1=New Matched Result!&value2="

minutes = 60
sleep_duration = 15 * minutes
hrefs = []

r = requests.get(scrape_url)
soup = BeautifulSoup(r.content, "html.parser")

print eval('soup.find_all("li", {"class":"sresult"})')
for item in soup.find_all("li", {"class":"sresult"}):
    a = item.find_all("a")[0]
    href = a.get("href")

    if href not in hrefs:
        requests.get(notification_endpoint + href)
        hrefs.append(href)

