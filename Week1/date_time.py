import datetime as dt
import time as tm

# handy datetime attributes
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second

# time returns the current time in seconds since the Epoch. (January 1st, 1970)
tm.time()

# convert the timestamp to datetime
dtnow = dt.datetime.fromtimestamp(tm.time())

# create a timedelta of 100 days
delta = dt.timedelta(days = 100)

# date.today returns the current local date
today = dt.date.today()

# the date 100 days ago
hundred_days_ago = today - delta
