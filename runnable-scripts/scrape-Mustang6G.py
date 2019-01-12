import sys

import requests

sys.path.append('..')
import reusables

soup = reusables.scrape("http://www.mustang6g.com/")

for post in soup.find_all("li", {"class":"post"}):
    title = post.find_all("h2")[0].find_all("a")[0].getText()
    description = post.find_all("div", {"class":"entry"})[0].find_all("p")[0].getText()
    title_description = title + " | " + description

    link = post.find_all("a")[0].get("href")
    image = post.find_all("a")[2].find_all("img")[0].get("src")
    if link not in reusables.get_hrefs():
        requests.get("https://maker.ifttt.com/trigger/mustang6g/with/key/VzmWoFF515H4lf0MNNVyo?value1=" + title_description + "&value2=" + link + "&value3=" + image, timeout=30)
        reusables.add_href(link)