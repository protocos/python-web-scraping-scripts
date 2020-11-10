import sys
sys.path.append('..')
import reusables
import requests


for page_num in range(1, 20):
    url = "https://www.zillow.com/homes/for_sale/house_type/3-_beds/2.0-_baths/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A"+str(page_num)+"%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-95.55223850185983%2C%22east%22%3A-95.35139469082468%2C%22south%22%3A29.672777996777466%2C%22north%22%3A29.807668861865455%7D%2C%22mapZoom%22%3A13%2C%22customRegionId%22%3A%2204dfb5fa9aX1-CR1smkm24933nge_u77s3%22%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A550000%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%2C%22sqft%22%3A%7B%22min%22%3A2000%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22sch%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A1832%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22abo%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
    soup = reusables.scrape_with_selenium(url)

    items = soup.find("div", {"id": "search-page-list-container"}).find_all("li")
    for item in items:
        house_anchor_tag = item.find("a")
        if house_anchor_tag is None:
            # Filter out list items without links inside them
            continue

        house_listing_url = house_anchor_tag['href']
        if "homedetails" not in house_listing_url:
            # Filter out links without "homedetails"
            continue

        house_price = item.find("div", {"class": "list-card-price"}).get_text()
        house_details = item.find("ul", {"class": "list-card-details"}).find_all("li")
        house_details_as_text = ""
        for house_detail in house_details:
            if (house_details_as_text != ""):
                house_details_as_text += ", "
            house_details_as_text += house_detail.get_text()

        house_address = item.find("address").get_text()

        card_name = house_price + " | " + house_details_as_text + " | " + house_address

        card_description = "###["+house_address+"]("+house_listing_url+")"

        house_image_url = item.find("img")['src']

        if house_listing_url not in reusables.get_hrefs():
            requests.post("https://en1wwvea98k42yd.m.pipedream.net/", {
                "boardName": "House Buying",
                "listName": "New Listings",
                "cardName": card_name,
                "cardDescription": card_description,
                "attachmentUrl": house_image_url
            }, timeout=30)
            reusables.add_href(house_listing_url)