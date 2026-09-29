import datetime
import hashlib
import hmac
first_date = datetime.datetime(1970, 1, 1)
time_since = datetime.datetime.now() - first_date
seconds = int(time_since.total_seconds())
"""print(seconds)"""
#print(hash(seconds))
"""Lets see if this logins into as a gitstreak."""
secret = b"my-secret-key"
message = b"amount=100&user=alice"

signature = hmac.new(
    secret,
    message,
    hashlib.sha256
).hexdigest()
print(signature)