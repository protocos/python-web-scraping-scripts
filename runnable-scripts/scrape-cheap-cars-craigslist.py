import sys
sys.path.append('..')
import reusables


def scrape(car_type, query):
    soup = reusables.scrape(query)
    for item in soup.find_all("li", {"class": "result-row"}):
        a = item.find_all("a")[0]
        href = a.get("href")
        price = item.find("span", {"class": "result-price"}).text
        post = reusables.scrape(href)
        img = post.find("img")["src"]

        reusables.check_value3_and_send_notification('news_with_image',
                                                     "New "+car_type+" Found for "+price+"!",
                                                     "%23[Original Post]("+href+")\n\n---\n\n%23%23%23[Original Search]("+query+")",
                                                     img)


def parameters(min_price, max_price, max_miles, year, make, model):
    return "&min_price="+str(min_price)+"&max_price="+str(max_price)+"&min_auto_year="+str(year)+"&max_auto_year="+str(year)+"&min_auto_miles="+str(1000)+"&max_auto_miles="+str(max_miles)+"&auto_make_model="+str(make)+"+"+str(model)


base_query = "https://houston.craigslist.org/search/sss?query=-Credit+-Wheels+-Tires+-Engine+-Motor+-Special+-Low+-Down+-Finance+-Buy&sort=rel&srchType=T&hasPic=1&bundleDuplicates=1"
min_price = 1300
max_price = 7500
max_mileage = 150000

scrape("2011 Camry", base_query+parameters(min_price, max_price, max_mileage, 2011, "Toyota", "Camry"))
scrape("2012 Corolla", base_query+parameters(min_price, max_price, max_mileage, 2012, "Toyota", "Corolla"))
scrape("2012 Fusion", base_query+parameters(min_price, max_price, max_mileage, 2012, "Ford", "Fusion"))
scrape("2013 Civic", base_query+parameters(min_price, max_price, max_mileage, 2013, "Honda", "Civic"))
scrape("2012 Accord", base_query+parameters(min_price, max_price, max_mileage, 2012, "Honda", "Accord"))
