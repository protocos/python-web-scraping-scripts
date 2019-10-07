import sys
sys.path.append('..')
import reusables


def scrape(soup, car_type):
    for item in soup.find_all("li", {"class": "result-row"}):
        a = item.find_all("a")[0]
        href = a.get("href")

        reusables.check_href_and_send_notification("New "+car_type+" Found!", href, href)


def parameters(min_price, max_price, max_miles, year, make, model):
    return "&min_price="+str(min_price)+"&max_price="+str(max_price)+"&min_auto_year="+str(year)+"&max_auto_year="+str(year)+"&min_auto_miles="+str(1000)+"&max_auto_miles="+str(max_miles)+"&max_auto_miles="+str(max_miles)+"&auto_make_model="+str(make)+"+"+str(model)


base_query = "https://houston.craigslist.org/search/sss?query=-Credit+-Wheels+-Tires+-Engine+-Motor+-Special+-Low+-Down+-Finance+-Buy&sort=rel&srchType=T&hasPic=1&bundleDuplicates=1&postedToday=1"
min_price = 1300
max_price = 7500
max_mileage = 150000


Camry2011 = reusables.scrape(base_query+parameters(min_price, max_price, max_mileage, 2011, "Toyota", "Camry"))
scrape(Camry2011, "2011 Camry")

Corolla2012 = reusables.scrape(base_query+parameters(min_price, max_price, max_mileage, 2012, "Toyota", "Corolla"))
scrape(Corolla2012, "2012 Corolla")

Fusion2012 = reusables.scrape(base_query+parameters(min_price, max_price, max_mileage, 2012, "Ford", "Fusion"))
scrape(Fusion2012, "2012 Fusion")

Civic2013 = reusables.scrape(base_query+parameters(min_price, max_price, max_mileage, 2013, "Honda", "Civic"))
scrape(Civic2013, "2013 Civic")

Accord2012 = reusables.scrape(base_query+parameters(min_price, max_price, max_mileage, 2012, "Honda", "Accord"))
scrape(Accord2012, "2012 Accord")
