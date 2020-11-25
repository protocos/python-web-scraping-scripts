import sys
sys.path.append('..')
import reusables
import requests

url = ""
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
        reusables.add_href(house_listing_url)
        requests.post("https://en1wwvea98k42yd.m.pipedream.net/", {
            "boardName": "House Buying",
            "listName": "New Listings",
            "cardName": card_name,
            "cardDescription": card_description,
            "attachmentUrl": house_image_url
        }, timeout=30)