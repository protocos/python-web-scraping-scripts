import sys
sys.path.append('..')
import reusables

soup = reusables.scrape("https://escapehouston.com/")

for item in soup.find_all("div", {"class":"post"}):
    a = item.find("h2", {"class":"excerpt-title"}).find("a")
    title = a.getText()
    href = a.get("href")

    p = item.find("div", {"class":"excerpt-content"}).find("article").find('p')
    desc = p.getText()

    reusables.check_href_and_send_notification("New Flight Deal!", desc, href)