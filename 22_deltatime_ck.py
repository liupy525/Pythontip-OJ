import datetime,time
def dateDiffInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days*24*3600 + timedelta.seconds

date1 = datetime.datetime(2006,02,17,15,30,00)
date2 = datetime.datetime(2006,05,18,11,01,00)

print dateDiffInSeconds(date1, date2)