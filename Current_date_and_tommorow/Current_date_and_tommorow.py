""" Finding Today's Tomorrow's and Yesterday's Date"""

from datetime import datetime,timedelta
date_time_now = datetime.now()

tommorow_time = date_time_now + timedelta(days=1)
yesterday_time = date_time_now - timedelta(days=1)

print(f" Today's date is {date_time_now.strftime('%d-%m-%Y')}, Tommorow's date is {tommorow_time.strftime('%d-%m-%Y')} and Yesterday's date is {yesterday_time.strftime('%d-%m-%Y')}")