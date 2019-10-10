import sys
sys.path.append('..')
import reusables
import re


def scrape(car_type, query):
    soup = reusables.scrape(query)
    for item in soup.find_all("li", {"class": "result-row"}):
        a = item.find_all("a")[0]
        href = a.get("href")
        price = item.find("span", {"class": "result-price"}).text
        if reusables.href_has_not_been_logged(href):
            post = reusables.scrape(href)
            attrs = post.find_all("p", {"class": "attrgroup"})
            description = ''
            for attr in attrs:
                no_html_tags = re.sub('<.+?>', '', str(attr))
                no_new_lines = re.sub('\n\n', '\n', no_html_tags)
                description += no_new_lines+"\n"
            img = post.find("img")["src"]
            reusables.check_key_and_send_notification('news_with_image',
                                                      href,
                                                      "New "+car_type+" Found for "+price+"!",
                                                      "%23[Original Post]("+href+")\n\n"+description,
                                                      img)


def parameters(min_price, max_price, max_miles, year, make, model):
    return "&min_price="+str(min_price)+"&max_price="+str(max_price)+"&min_auto_year="+str(year)+"&max_auto_year="+str(year)+"&min_auto_miles="+str(1000)+"&max_auto_miles="+str(max_miles)+"&auto_make_model="+str(make)+"+"+str(model)


base_query = "https://houston.craigslist.org/search/sss?query=-Credit+-Wheels+-Tires+-Engine+-Motor+-Special+-Low+-Down+-Finance+-Buy&sort=rel&srchType=T&hasPic=1&bundleDuplicates=1&auto_title_status=1&postedToday=1"
min_price = 1300
max_price = 7800
max_mileage = 150000

scrape("2011 Camry", base_query+parameters(min_price, max_price, max_mileage, 2011, "Toyota", "Camry"))
scrape("2012 Corolla", base_query+parameters(min_price, max_price, max_mileage, 2012, "Toyota", "Corolla"))
scrape("2012 Fusion", base_query+parameters(min_price, max_price, max_mileage, 2012, "Ford", "Fusion"))
scrape("2013 Civic", base_query+parameters(min_price, max_price, max_mileage, 2013, "Honda", "Civic"))
scrape("2012 Accord", base_query+parameters(min_price, max_price, max_mileage, 2012, "Honda", "Accord"))
