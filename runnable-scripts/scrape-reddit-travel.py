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


subreddit = reddit.subreddit('travel')
for submission in subreddit.top(limit=10, time_filter='month'):
    if submission.url.endswith('.jpg'):
        reusables.check_key_and_send_notification('guess_where', submission.url, "Guess where? :: "+submission.title, "%23[Original Post](https://www.reddit.com/r/travel/comments/"+submission.id+")\n\n---\n\n%23%23%23[IFTTT Recipe](https://ifttt.com/applets/105126139d/edit)", submission.url)
