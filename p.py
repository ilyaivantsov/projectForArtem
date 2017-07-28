# coding: utf-8
from datetime import date

class Batch(object):
  # Объект партия
  """docstring for Batch"""
  __num=0
  def __init__(self,date,total):
    Batch.__num +=1
    self.num=Batch.__num
    self.date=date   # Дата прихода
    self.total=total # Остаток 

  def num(self):
    return Batch.__num
    
  def toString(self):
    return 'Batch '+str(self.num)+' Date:'+self.date.strftime("%d %B %Y")+' Total:'+str(self.total)

class Range(object):  # Объект номенклатура
  """docstring for Range""" 
  name='Noname'
  items=[]
  flag=0
  def __init__(self, name):
    self.name=name
    
  def amountBatch(self): # Кол-во партий 
    return len(self.items)

  def journal(self):
    st=''
    for item in self.items:
      st+=item.toString()+'\n'
    return st	

  def push(self,batch):
    self.items.append(batch)
	
  def get(self,nominal):
    if (self.flag > self.amountBatch()-1):
      return nominal
    item=self.items[self.flag]
    if (nominal < item.total):
      item.total-=nominal
      return self.flag
    if (item.total < nominal):
      val=nominal-item.total
      item.total=0
      self.flag+=1
      return self.get(val)

def f(a):
  if (a==1):
    return 1
  return a*f(a-1)

 
a=Batch(date(2017,7,25),100)
b=Batch(date(2017,7,26),50)
c=Batch(date(2017,7,29),100)
store=Range('oil')
store.push(a)
store.push(b)
store.push(c)