import sys
sys.path.append('..')
import reusables
import json
import requests

base_url = "https://www.autotrader.com"
url = "https://www.autotrader.com/cars-for-sale/Used+Cars/cars+under+6500/Lexus/LS+430/Houston+TX-77081?makeCodeList=LEXUS&searchRadius=500&modelCodeList=LS430&zip=77081&marketExtension=include&maxPrice=6500&listingTypes=USED&startYear=2004&isNewSearch=true&sortBy=relevance&numRecords=25&firstRecord=0"
soup = reusables.scrape_with_selenium(url)

for item in soup.find_all("script", {"data-cmp": "lstgSchema"}):
    carListing = json.loads(item.get_text())
    name = carListing.get("name")
    link = carListing.get("url")
    price = carListing.get("offers").get("price")
    price_formatted = '${:,.2f}'.format(price)
    color = carListing.get("color")
    year = carListing.get("productionDate")
    year_formatted = str(year)
    model = carListing.get("model")
    odometer = carListing.get("mileageFromOdometer").get("value")
    description = carListing.get("description")
    image_url = carListing.get("image")

    card_name = price_formatted + " -- " + color + " " + year_formatted + " " + model + " with " + odometer + " miles "
    card_description = (""+description+""
                        "\n\n#[Original Post](" + link + ")")

    if link not in reusables.get_hrefs():
        requests.post("https://en1wwvea98k42yd.m.pipedream.net/", {
            # "boardName": "Reading Material 📕",
            # "listName": "News",
            "boardName": "GTD Home",
            "listName": "Collection Bucket",
            "cardName": card_name,
            "cardDescription": card_description,
            "attachmentUrl": image_url
        }, timeout=30)
        reusables.add_href(link)



# for item in soup.find_all("div", {"class":"inventory-listing"}):
#     listing_id = item.get("id")
#     print(listing_id)
#     title = item.find("h2").get_text()
#     mileage = item.find("div", {"class":"item-card-specifications"}).find("span", {"class":"text-bold"}).get_text()
#     # is_great_price = item.find("div", {"class":"ribbon-content-right"}).get_text()
#     price = item.find("span", {"class":"first-price"}).get_text()
#     link = base_url + item.find("a").get("href")
#
#     cardName = "$" + price + " - " + title + " with " + mileage + " "
#     cardDescription = ("#[Original Post](" + link + ")")
#
#     if link not in reusables.get_hrefs():
#         requests.post("https://en1wwvea98k42yd.m.pipedream.net/", {
#             # "boardName": "Reading Material 📕",
#             # "listName": "News",
#             "boardName": "GTD Home",
#             "listName": "News",
#             "cardName": cardName,
#             "cardDescription": cardDescription
#         }, timeout=30)
#         reusables.add_href(link)