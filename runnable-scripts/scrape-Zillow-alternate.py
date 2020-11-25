import sys
sys.path.append('..')
import reusables
import requests
import json

page_num = 1
url = "https://www.zillow.com/homes/for_sale/house_type/3-_beds/2.0-_baths/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A"+str(page_num)+"%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-95.55223850185983%2C%22east%22%3A-95.35139469082468%2C%22south%22%3A29.672777996777466%2C%22north%22%3A29.807668861865455%7D%2C%22mapZoom%22%3A13%2C%22customRegionId%22%3A%2204dfb5fa9aX1-CR1smkm24933nge_u77s3%22%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A550000%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%2C%22sqft%22%3A%7B%22min%22%3A2000%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22sch%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A1832%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22abo%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
soup = reusables.scrape_with_selenium(url)

script = soup.find("script", {"data-zrr-shared-data-key": "mobileSearchPageStore"})
json = json.loads(script.string.lstrip("<!--").rstrip("-->"))
list_results = json["cat1"]["searchResults"]["listResults"]
for item in list_results:
    detailUrl = item["detailUrl"]
    imgSrc = item["imgSrc"]
    statusText = item["statusText"]
    price = item["price"]
    address = item["address"]
    beds = item["beds"]
    baths = item["baths"]
    area = item["area"]
    latitude = item["latLong"]["latitude"]
    longitude = item["latLong"]["longitude"]

    card_name = str(price) + " | " + str(beds) + " beds, " + str(baths) + " baths, " + str(area) + " sqft" + " | " + str(address)
    card_description = "##["+statusText+"]("+detailUrl+")" + \
                       "\n\nprice: " + str(price) + \
                       "\nbeds: " + str(beds) + \
                       "\nbaths: " + str(baths) + \
                       "\nsize: " + str(area) + \
                       "\naddress: " + str(address) + \
                       "\nlatitude: " + str(latitude) + \
                       "\nlongitude: " + str(longitude)

    if detailUrl not in reusables.get_hrefs():
        reusables.add_href(detailUrl)
        requests.post("https://en1wwvea98k42yd.m.pipedream.net/", {
            "boardName": "House Buying",
            "listName": "New Listings",
            "cardName": card_name,
            "cardDescription": card_description,
            "attachmentUrl": imgSrc
        }, timeout=30)