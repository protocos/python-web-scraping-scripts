import time
import pickledb

minute = 60
def sleep(sleep_duration = 15 * minute):
    time.sleep(sleep_duration)

def get_hrefs():
    db = pickledb.load('storage.db', False)
    hrefs = db.get('hrefs')
    return hrefs

def add_href(href):
    db = pickledb.load('storage.db', False)
    hrefs = db.get('hrefs')
    if hrefs is None:
        hrefs = []
    if href.startswith("http://") or href.startswith("https://"):
        if href not in hrefs:
            hrefs.append(href)
    db.set('hrefs', hrefs)
    db.dump()

def clear_hrefs():
    db = pickledb.load('storage.db', False)
    hrefs = []
    db.set('hrefs', hrefs)
    db.dump()