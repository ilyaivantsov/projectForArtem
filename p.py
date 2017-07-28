# coding: utf-8
from datetime import date

class Batch(object):
  # Объект партия
  """docstring for Batch"""

  num=0
  def __init__(self,date,total):
    self.date=date   # Дата прихода
    self.total=total # Остаток 
    self.hist=[] # Локальный журнал сделок

  def toString(self):
    return 'Batch '+str(self.num)+' Date:'+self.date.strftime("%d %B %Y")+' Total:'+str(self.total)

class Range(object):  
  # Объект номенклатура
  """docstring for Range"""

  name='Noname'
  items=[]
  flag=0 # Позиция самой свежей партии в массиве items
  def __init__(self, name):
    self.name=name
    
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

  def get(self,nominal,date):
    if (self.flag > self.amount()-1):
      item=self.items[-1]
      item.hist.append((-nominal,date))
      return 0
    item=self.items[self.flag]
    if (nominal <= item.total):
      item.total-=nominal
      item.hist.append((nominal,date))
      return 1
    if (item.total < nominal):
      val=nominal-item.total
      item.hist.append((item.total,date))
      item.total=0
      self.flag+=1
      return self.get(val,date)


 
a=Batch(date(2017,7,25),100)
b=Batch(date(2017,7,26),50)
c=Batch(date(2017,7,29),100)
dt1=date(2017,7,28)
dt2=date(2017,7,30)
dt3=date(2017,8,1)
store=Range('oil')
store.push(a)
store.push(b)
store.push(c)
print(store.journal())