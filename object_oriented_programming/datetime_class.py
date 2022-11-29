from datetime import datetime, timedelta

d = datetime.now()
print(d.weekday(), d.hour, d.second, d.microsecond)
d2 = datetime(2021, 5, 27)
diff = d - d2
# print(diff)

t = timedelta(weeks=1)
# print(d + t)
#
# print(d.strftime("%A"))
# print(d.strftime("%b"))
print(d.strftime("%A %d,%B %y"))
# date_from_str = datetime.strftime("02/02/02 16:10:2", "%m/%y%d"c



import collections
c1 = collections.Counter("hellow world")
print(c1)
c2 = collections.Counter("hi you")
print(c2)
c1.subtract(c2)

Person = collections.namedtuple("Person", "name age")

p1 = Person(name= "Adeola", age=16)
print(p1.name)