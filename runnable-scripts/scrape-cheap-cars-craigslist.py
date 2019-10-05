import reusables
import sys
sys.path.append('..')


def scrape(soup, car_type):
    for item in soup.find_all("li", {"class": "result-row"}):
        a = item.find_all("a")[0]
        href = a.get("href")

        reusables.check_href_and_send_notification("New "+car_type+" Found!", href, href)


def price_str(min_price, max_price):
    return "&min_price="+str(min_price)+"&max_price="+str(max_price)


price_min = 1300
price_max = 7500
scrapTerms = "+-Credit+-Wheels+-Tires+-Engine+-Motor+-Special+-Low+-Down+-Finance+-Buy"
searchQuery = scrapTerms+"&sort=rel&srchType=T&hasPic=1&postedToday=1&bundleDuplicates=1"
price = "&min_price="+str(price_min)+"&max_price="+str(price_max)

Camry2011 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2011+Camry"+searchQuery+price)
scrape(Camry2011, "2011 Camry")

Corolla2012 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2012+Corolla"+searchQuery+price)
scrape(Corolla2012, "2012 Corolla")

Fusion2012 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2012+Fusion"+searchQuery+price)
scrape(Fusion2012, "2012 Fusion")

Civic2013 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2013+Civic"+searchQuery+price)
scrape(Civic2013, "2013 Civic")

Accord2012 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2012+Accord"+searchQuery+price)
scrape(Accord2012, "2012 Accord")
