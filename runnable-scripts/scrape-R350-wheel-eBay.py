import sys
sys.path.append('..')
import reusables

soup = reusables.scrape("https://www.ebay.com/sch/i.html?_mPrRngCbx=1&LH_BIN=1&_from=R40&_sacat=0&_fosrp=1&_nkw=SVE%20R350%20-mercedes&_dcat=6030&rt=nc&_udlo=100&_udhi=500")

for item in soup.find_all("li", {"class":"sresult"}):
    a = item.find_all("a")[0]
    href = a.get("href")

    reusables.check_href_and_send_notification("New R350 Wheel Match!", "", href)
