# coding: utf-8
from datetime import date

class Batch(object):  # Объект партия
    """docstring for Batch"""
    __num=0
    '''def __init__(self,date,total):
    	Batch.__num+=1
    	self.num=Batch.__num
	    self.date=date   # Дата прихода
	    self.total=total # Остаток '''

    def num(self):
      return Batch.__num
    
    def toString(self):
      return 'Batch '+str(self.num)+' Date:'+self.date.strftime("%d %B %Y")+' Total:'+str(self.total)

class Range(object):  # Объект номенклатура
	"""docstring for Range""" 
	name='Noname'
	items=[]
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
		

 
a=Batch(date(2017,7,25),100)
b=Batch(date(2017,7,26),50)
c=Batch(date(2017,7,29),100)
