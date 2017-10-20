import sys
sys.path.append('..')
import reusables

soup = reusables.scrape("https://houston.craigslist.org/search/sss?query=ipad+5th+gen&sort=rel&hasPic=1&search_distance=30&postal=77081&min_price=100&max_price=240")

for item in soup.find_all("li", {"class":"result-row"}):
    a = item.find_all("a")[0]
    href = a.get("href")

    reusables.check_href_and_send_notification("New iPad Match!", href)