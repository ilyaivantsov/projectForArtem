# coding: utf-8
import csv

FILENAME='users.csv'

with open(FILENAME, "w", newline="") as file:
  columns=["name","age"]
  writer=csv.DictWriter(file,fieldnames=columns)
  writer.writeheader()
  user=[{"name":"Ilya","age":41}]
  writer.writerows(user)

  for i in range(1,500000):
  s.approach('Oil',date.today(),i*5)
for i in range(1,500000):
  s.approach('Oil',date(2017,8,1),i*5)

for i in range(1,10000000):
  s.transaction('Oil',date.today(),200)

p=s.rangeBook['Oil']
b=p.items[499998]
a=p.items[499999]