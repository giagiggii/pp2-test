import datetime
x = datetime.datetime.now()
final = x.replace(microsecond=0)
print(final)
