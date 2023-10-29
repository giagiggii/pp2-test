import datetime
x = datetime.datetime.now()
print(x.day-5)    #первый вариант решения


x1 = datetime.datetime.now()
mu = x1 -(x1 - x1.replace(day=x1.day - 5))
print(mu.strftime("%Y-%m-%d"))  #второй вариант решения


