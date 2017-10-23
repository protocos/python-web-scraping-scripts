import sys
sys.path.append('..')
import reusables

soup = reusables.scrape("http://www.mustang6g.com/")

for item in soup.find_all("div", {"class":"entry"}):
    paragraphs = item.find_all("p")
    description = paragraphs[0].getText()
    a = paragraphs[1].find("a")
    href = a.get("href")

    reusables.check_href_and_send_notification("Mustang6G:", description, href)