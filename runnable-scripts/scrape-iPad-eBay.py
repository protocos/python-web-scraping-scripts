import sys
sys.path.append('..')
import reusables

#soup = reusables.scrape("https://www.ebay.com/sch/i.html?_udlo=100&_udhi=240&LH_BIN=1&_mPrRngCbx=1&_from=R40&_sacat=0&_nkw=ipad%205th%20generation%20-mini%20-broken%20-air%20space%20gray%20-dent&rt=nc")
#soup = reusables.scrape("https://www.ebay.com/sch/i.html?_udlo=100&_udhi=190&LH_BIN=1&_mPrRngCbx=1&_from=R40&_sacat=0&_nkw=ipad%20air%202%20new%20-mini%20-case%20-screen%20-keyboard%20-cover%20-hardcase%20-stand%20-sleeve%20-adapter%20-battery%20-frame&rt=nc")
soup = reusables.scrape("https://www.ebay.com/sch/i.html?_odkw=ipad+5th+generation+-aXtion+-keyboard+-mount+-digitizer+-replacement+-screen+-broken&_udlo=116&_udhi=200&LH_BIN=1&_mPrRngCbx=1&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xipad+5th+generation+-aXtion+-keyboard+-mount+-digitizer+-replacement+-screen+-b.TRS0&_nkw=ipad+5th+generation+-aXtion+-keyboard+-mount+-digitizer+-replacement+-screen+-broken+-case&_sacat=0")

for item in soup.find_all("li", {"class":"sresult"}):
    a = item.find_all("a")[0]
    href = a.get("href")

    reusables.check_href_and_send_notification("New iPad eBay Match!", href, href)
