import sys
sys.path.append('..')
import reusables
import requests
import json

base_url = "https://www.producthunt.com"
search_url = "https://www.producthunt.com/search?postedDate=30%3Adays"
soup = reusables.scrape(base_url)

threshold = 100


def get_post_link(div):
    post = "Post" + div.get("data-test").lstrip("post-item-")
    script = soup.find_all("script")[6].get_text() \
        .lstrip("window.__APOLLO_STATE__ = ") \
        .rstrip(";")
    script_object = json.loads(script)
    thumbnail_id = script_object.get(post).get("thumbnail").get("id")
    image_uuid = script_object.get(thumbnail_id).get("image_uuid")
    image_link = "https://ph-files.imgix.net/" + image_uuid
    return image_link


blacklist = []  # requests.get("https://ent7ghk7utpt6zj.m.pipedream.net").json().get("blacklist")


for item in soup.find_all("li"):
    for div in item.find_all("div", {"class": "item_54fdd"}):
        a = item.find("a")
        href = a.get("href")
        link = base_url + href
        split_link = link.split("?", 1)
        link_with_no_querystring = split_link[0]
        if link_with_no_querystring not in reusables.get_hrefs():
            try:
                voteButton = item.find("div", {"class": "voteButtonWrap_4c515"})
                voteNumber = int(item.find("span").find("span").get_text())
                if voteNumber > threshold and href.startswith('/'):
                    scrapeLink = reusables.scrape(link)
                    categories = scrapeLink.find_all("div", {"class":"item_994c1"})
                    categoriesArray = []
                    for category in categories:
                        categoriesArray.append(category.find("a").get_text())
                    categoriesString = ", ".join(categoriesArray)

                    productName = div.find("h3").get_text()
                    productDescription = div.find("p").get_text()

                    cardName = productName + " :: " + productDescription + "[in "+categoriesString+"]"

                    skip_this_one = False
                    for blacklist_term in blacklist:
                        if blacklist_term.lower() in cardName.lower():
                            print('Skipping \''+productName+'\' because of '+blacklist_term)
                            skip_this_one = True
                    if skip_this_one:
                        reusables.add_href(link)
                        continue

                    imageLink = get_post_link(div)
                    cardDescription = ("#["+productName+"]("+link+")"
                                       "\n\n"
                                       "["+categoriesString+"]")

                    requests.post("https://en1wwvea98k42yd.m.pipedream.net/", {
                        "boardName": "Reading Material 📕",
                        "listName": "Product Hunt",
                        "cardName": cardName,
                        "cardDescription": cardDescription,
                        "attachmentUrl": imageLink
                    }, timeout=30)
                    reusables.add_href(link)
            except Exception as inst:
                print(type(inst))
                print(inst.args)
                print(inst)
                print("An exception occurred")
