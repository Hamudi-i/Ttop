import datetime
import hashlib
first_date = datetime.datetime(1970, 1, 1)
time_since = datetime.datetime.now() - first_date
seconds = int(time_since.total_seconds())
"""print(seconds)"""
print(hash("popo"))
