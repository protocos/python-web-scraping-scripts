import sys
import re
sys.path.append('..')
import reusables

soup = reusables.scrape("https://escapehouston.com/")

for item in soup.find_all("div", {"class":"post"}):
    a = item.find("h2", {"class":"excerpt-title"}).find("a")
    title = a.getText()
    href = a.get("href")

    p = item.find("div", {"class":"excerpt-content"}).find("article").find('p')
    desc = p.getText()
    pattern = '(.+) (has|have) (.+) flights from (.+?) to (.+) for (\$.+?),? (.+)\. Flights (.+?)\. (.+)'
    matches = re.search(pattern, desc)
    # print('Description:',desc)
    # print('Matches:')
    if matches:
        # for group in matches.groups():
        #     print(group)
        airline = matches.group(1)
        type_of_flight = matches.group(3)
        origin = matches.group(4)
        destination = matches.group(5)
        cost = matches.group(6)
        connection = matches.group(7)
        timeframe = matches.group(8)
        additional_info_separated_by_sentences = matches.group(9)

        cardTitle = 'Flight :: ' + destination + ' for ' + cost + ' ' + timeframe
        cardDescription = ("Origin: "+origin+"\n"
                           "Destination: "+destination+"\n"
                           "Cost: "+cost+"\n"
                           "Type: "+type_of_flight+", "+connection+"\n"
                           "Timeframe: "+timeframe+"\n"
                           "\n"
                           ""+additional_info_separated_by_sentences+"\n")
        print("cardTitle",cardTitle)
        print("cardDescription",cardDescription)
    else:
        print(desc)
    reusables.check_href_and_send_notification("New Flight Deal!", desc, href)