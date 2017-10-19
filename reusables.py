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
    hrefs.append(href)
    db.set('hrefs', hrefs)