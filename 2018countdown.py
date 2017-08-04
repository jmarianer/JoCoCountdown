from datetime import date, timedelta

def subtractmonths(date, delta):
    month = date.month
    year = date.year
    while month <= delta:
        delta -= 12
        year -= 1

    return date.replace(year=year, month=month-delta)

liftoff = date(2018,2,18)
day_deltas = [1, 2, 3, 4, 5, 6, 8, 9, 10, 20, 30, 40, 50, 100, 150, 200, 250, 300, 342]
week_deltas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for delta in day_deltas:
    print "%s: %s DAYS! :D" % (liftoff - timedelta(delta), delta)

for delta in week_deltas:
    print "%s: %s WEEKS! :D" % (liftoff - timedelta(delta * 7), delta)

for delta in week_deltas:
    print "%s: %s MONTHS! :D" % (subtractmonths(liftoff, delta), delta)
