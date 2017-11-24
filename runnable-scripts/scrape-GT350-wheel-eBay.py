import sys
sys.path.append('..')
import reusables

soup = reusables.scrape("https://www.ebay.com/sch/i.html?_odkw=gt350+wheel+stock+oem+factory+10053&_udhi=340&_mPrRngCbx=1&LH_BIN=1&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xgt350+wheel+stock+oem+factory+10053+-lexus.TRS0&_nkw=gt350+wheel+stock+oem+factory+10053+-lexus&_sacat=0")

for item in soup.find_all("li", {"class":"sresult"}):
    a = item.find_all("a")[0]
    href = a.get("href")

    reusables.check_href_and_send_notification("New GT350 Wheel Match!", "", href)
