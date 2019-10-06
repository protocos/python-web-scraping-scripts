import requests
import sys
sys.path.append('..')
import reusables
import praw


auth_file = open("auth.txt")
auth = []
for x in auth_file:
    auth.append(x.rstrip())


reddit = praw.Reddit(client_id=auth[0],
                     client_secret=auth[1],
                     user_agent=auth[2],
                     username=auth[3],
                     password=auth[4])


def check_href_and_send_notification(value1, value2, value3):
    if value3 not in reusables.get_hrefs():
        requests.get("https://maker.ifttt.com/trigger/guess_where/with/key/VzmWoFF515H4lf0MNNVyo?value1=" + value1 + "&value2=" + value2 + "&value3=" + value3,
                     timeout=30)
        reusables.add_href(value3)


subreddit = reddit.subreddit('travel')
for submission in subreddit.top(limit=10, time_filter='month'):
    if submission.url.endswith('.jpg'):
        check_href_and_send_notification("Guess where?", "%23[Original Post](https://www.reddit.com/r/travel/comments/"+submission.id+")\n\n---\n\n%23%23%23[IFTTT Recipe](https://ifttt.com/applets/105126139d/edit)", submission.url)
