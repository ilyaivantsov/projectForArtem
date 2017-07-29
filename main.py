# coding: utf-8
import csv

FILENAME='users.csv'

with open(FILENAME, "w", newline="") as file:
  columns=["name","age"]
  writer=csv.DictWriter(file,fieldnames=columns)
  writer.writeheader()
  user=[{"name":"Ilya","age":41}]
  writer.writerows(user)