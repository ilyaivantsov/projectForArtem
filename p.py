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

  def journal(self):
    st=''
    for item in self.items:
      st+=item.toString()+'\n'
    return st	

  def push(self,batch):
    self.items.append(batch)
    batch.num=len(self.items)
    if((len(self.items) > 1) and (self.items[-2].date > batch.date)):
      self.items.sort(key=lambda x: x.date)             # Сортируем по датам
      index=self.items.index(batch)                     # Индекс вставленной партии
      if(self.items[index+1].hist != []):               # Проверяем есть ли сделки по следующей партии
        self.key=self.items[index+1].hist[0][0]         # Возвращаем ключ текущей сделки
        self.flag=index
        for i in range(0,index):
          item=self.items[self.flag-1]
          if (len(item.hist) == 1 and item.hist[-1][0] == self.key):
            h=item.hist.pop()
            item.total+=h[1]
            self.flag-=1
          elif ( item.hist[-1][0] == self.key ):
            h=item.hist.pop()
            item.total+=h[1]
            self.flag-=1
            break
          else:
            break

        for item in self.items[index+1:]:          # Очищаем локальные журналы сделок по партиям
          item.total=item.nominal
          item.hist=[]
        index=self.key-1
        for deal in self.hist[index:]:             # Перезаключаем сделки
          self.get(deal[0],deal[1],0)
          self.key+=1 
        self.key-=1

  def get(self,nominal,date,fl):    # Флаг fl: False - не заносим слелку в локальный журнал партии, True - заносим
    if (fl):
      self.hist.append((nominal,date))
      self.key+=1
    if (self.flag > len(self.items)-1):
      item=self.items[-1]
      item.hist.append((self.key,item.total-nominal,date))
      item.total=0
      return 0
    item=self.items[self.flag]
    if (item.total > nominal):
      item.total-=nominal
      item.hist.append((self.key,nominal,date))
      return 1
    if (item.total < nominal):
      val=nominal-item.total
      item.hist.append((self.key,item.total,date))
      item.total=0
      self.flag+=1
      return self.get(val,date,0)
    if (nominal == item.total):
      item.total=0
      item.hist.append((self.key,nominal,date))
      self.flag+=1
      return 2

class Store(object):
  # Объект склад
  """docstring for Store"""
  def __init__(self, num):
    self.rangeBook={}        # Словарь номенклатур
    self.num=num             # Номер склада
    
  def approach(self,nameRange,dateCome,nominal):
    try:
      rng=self.rangeBook[nameRange]      # Получаем объект номенклатура
      rng.push(Batch(dateCome,nominal))  # Вставляем партию
    except KeyError:
      self.rangeBook[nameRange]=rng=Range(nameRange)
      rng.push(Batch(dateCome,nominal))

  def transaction(self,nameRange,dateOut,nominal):
    try:
      rng=self.rangeBook[nameRange]
      rng.get(nominal,dateOut,1)
    except KeyError:
      print(u'Нет данной номенклатуры: '+nameRange)

  def journal(self,nameRange):
    rng=self.rangeBook[nameRange]
    print(rng.journal())

s=Store(1)

a=Batch(date(2017,1,25),100)
b=Batch(date(2017,1,26),50)
c=Batch(date(2017,2,2),60)
d=Batch(date(2017,1,24),65)
k=Batch(date(2017,1,25),100)
dt1=date(2017,1,28)
dt2=date(2017,7,30)
dt3=date(2017,8,1)
store=Range('oil')
store.push(a)
store.push(b)
store.push(c)
store.push(d)

print(store.journal())