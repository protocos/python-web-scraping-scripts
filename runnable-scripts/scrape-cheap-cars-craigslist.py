import sys
sys.path.append('..')
import reusables

def scrape(soup, carType):
    for item in soup.find_all("li", {"class": "result-row"}):
        a = item.find_all("a")[0]
        href = a.get("href")

        reusables.check_href_and_send_notification("New "+carType+" Found!", href, href)

price_min = 1300
price_max = 10000
scrapTerms = "+-Credit+-Wheels+-Tires+-Engine+-Motor+-Special+-Low+-Down+-Finance+-Buy"
searchQuery = scrapTerms+"&sort=rel&srchType=T&hasPic=1&postedToday=1&bundleDuplicates=1&min_price="+str(price_min)+"&max_price="+str(price_max)

Camry2011 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2011+Camry"+searchQuery)
scrape(Camry2011, "2011 Camry");

Corolla2012 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2012+Corolla"+searchQuery)
scrape(Corolla2012, "2012 Corolla");

Fusion2012 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2012+Fusion"+searchQuery)
scrape(Fusion2012, "2012 Fusion");

Civic2013 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2013+Civic"+searchQuery)
scrape(Civic2013, "2013 Civic");

Accord2012 = reusables.scrape("https://houston.craigslist.org/search/sss?query=2012+Accord"+searchQuery)
scrape(Accord2012, "2012 Accord");
