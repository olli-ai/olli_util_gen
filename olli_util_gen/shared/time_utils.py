from datetime import time as dtime
from datetime import datetime, timedelta


def seconds_until_hour(at_hour):
    now = datetime.now()
    current_hour = now.hour
    if current_hour < at_hour:
        to_time = datetime.combine(now + timedelta(days=0), dtime(hour=at_hour))
    else:
        to_time = datetime.combine(now + timedelta(days=1), dtime(hour=at_hour))
    delta = to_time - now
    seconds = delta.total_seconds()

    return seconds