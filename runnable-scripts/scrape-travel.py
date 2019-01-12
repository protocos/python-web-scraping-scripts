import sys
sys.path.append('..')
import reusables

soup = reusables.scrape("https://www.reddit.com/r/travel/top/")

links = soup.find_all("a")

print (links)

# items = soup.find_all("a", {"class":"SQnoC3ObvgnGjWt90zD9Z"})
#
# if len(items) > 0:
#     item = items[0]
#
#     a = item.find("h2")
#     title = a.getText()
#     href = a.get("href")
#
#     reusables.check_href_and_send_notification("Guess where?", title, href)