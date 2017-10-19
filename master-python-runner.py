import time
import sys

seconds = 60
sleep_duration_minutes = 15

try:
    while True:
        poll_ebay_for_iPad()
        time.sleep(sleep_duration_minutes * seconds)
except KeyboardInterrupt:
    print("Quitting the program.")
except:
    print("Unexpected error: "+sys.exc_info()[0])
    raise