# import time as datetime
from datetime import datetime

datetime_str = input("Enter the date in the format dd/mm/yyyy")

try:
    datetime_object = (datetime.strptime(datetime_str, "%d/%m/%Y")).strftime("%d/%m/%Y")
except ValueError as e:
    print("ValueError Raised:", e)
else:
    print(datetime_object)

# time_str = '25::55::26'

# try:
#     time_object = datetime.strptime(time_str, '%H::%M::%S')
# except ValueError as e:
#     print('ValueError:', e)
