import datetime

today = datetime.date.today()
t1 = today.strftime("%d/%m/%y")
print("t1=", t1)
now = datetime.datetime.now()
print("now =", now)
