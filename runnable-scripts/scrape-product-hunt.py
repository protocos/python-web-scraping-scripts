import sys
sys.path.append('..')
import reusables
import requests
import json

base_url = "https://www.producthunt.com"
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


blacklist = requests.get("https://ent7ghk7utpt6zj.m.pipedream.net").json().get("blacklist")


for item in soup.find_all("li"):
    for div in item.find_all("div", {"class": "item_54fdd"}):
        a = item.find("a")
        href = a.get("href")
        try:
            voteButton = item.find("div", {"class": "voteButtonWrap_4c515"})
            voteNumber = int(item.find("span").find("span").get_text())
            if voteNumber > threshold and href.startswith('/'):
                link = base_url + href

                productName = div.find("h3").get_text()
                productDescription = div.find("p").get_text()

                skip_this_one = False
                for blacklist_term in blacklist:
                    if blacklist_term.lower() in productName.lower() or blacklist_term.lower() in productDescription.lower():
                        print('Skipping \''+productName+'\' because of '+blacklist_term)
                        skip_this_one = True
                if skip_this_one:
                    continue

                # topics = div.find_all("a", {"class": "postTopicLink_a090c"})
                # print(topics)
                # print(len(topics))
                # topic = ""
                # if len(topics) > 0:
                #     topic += topics[0]
                # print(topic)

                cardName = productName + " :: " + productDescription
                imageLink = get_post_link(div)
                cardDescription = ("#["+productName+"]("+link+")")

                if link not in reusables.get_hrefs():
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
