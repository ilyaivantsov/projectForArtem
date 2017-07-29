# coding: utf-8
from datetime import date

class Batch(object):
  # Объект партия
  """docstring for Batch"""

  num=0                # Номер партии
  def __init__(self,date,total):
    self.date=date     # Дата прихода
    self.total=total   # Остаток 
    self.nominal=total # Номинал партии
    self.hist=[]       # Локальный журнал сделок по партии

  def toString(self):
    return 'Batch '+str(self.num)+' Date:'+self.date.strftime("%d %B %Y")+' Total:'+str(self.total)

class Range(object):  
  # Объект номенклатура
  """docstring for Range"""

  name='Noname'
  def __init__(self, name):
    self.name=name
    self.items=[]
    self.hist=[] # Локальный журнал сделок по номенклатуре
    self.flag=0  # Позиция самой свежей партии в массиве items
    self.key=0   # Ключ сделки(текущий номер сделки по данной номенклатуре)

  def amount(self): # Кол-во партий 
    return len(self.items)

  def journal(self):
    st=''
    for item in self.items:
      st+=item.toString()+'\n'
    return st	

  def push(self,batch):
    self.items.append(batch)
    batch.num=self.amount()
    if((len(self.items) > 1) and (self.items[-2].date > batch.date)):
      self.items.sort(key=lambda x: x.date)
      for item in self.items:       # Очищаем локальные журналы сделок по партиям
        item.total=item.nominal
        item.hist=[]
        self.flag=0                 # Возвращаем самую свежую партию
        self.key=0                  # Возарвщаем ключ сделки 
      for deal in self.hist:        # Перезаключаем сделки
        self.key+=1
        self.get(deal[0],deal[1],0) 
      
  def get(self,nominal,date,fl):    # Флаг  False - не заносим слелку в журнал, True - заносим
    if (fl):
      self.hist.append((nominal,date))
      self.key+=1
    if (self.flag > self.amount()-1):
      item=self.items[-1]
      item.hist.append((self.key,item.total-nominal,date))
      item.total=0
      return 0
    item=self.items[self.flag]
    if (nominal <= item.total):
      item.total-=nominal
      item.hist.append((self.key,nominal,date))
      return 1
    if (item.total < nominal):
      val=nominal-item.total
      item.hist.append((self.key,item.total,date))
      item.total=0
      self.flag+=1
      return self.get(val,date,0)


a=Batch(date(2017,1,25),100)
b=Batch(date(2017,1,26),50)
c=Batch(date(2017,2,2),60)
d=Batch(date(2017,1,24),65)
dt1=date(2017,7,28)
dt2=date(2017,7,30)
dt3=date(2017,8,1)
store=Range('oil')
store.push(a)
store.push(b)
store.push(c)

print(store.journal())