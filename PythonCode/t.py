from calendar import monthrange
from datetime import datetime, timedelta

def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta
d1 = input()
d2 = input()
monthdelta(d1,d2)
