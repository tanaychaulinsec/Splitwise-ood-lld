class Bill(object):
    def __init__(self):
        self.id=None
        self.name=None
        self.amount=None
        self.contribution={}
        self.paidBy={}
    
    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name

    def  setId(self,id):
        self.i=id
    
    def getId(self):
        return self.id

    def setAmount(self,amount):
        self.amount=amount
    
    def getAmount(self):
        return self.amount

    def setContribution(self,contribution):
        self.contribution=contribution

    def getContribution(self):
        return self.contribution

    def setPaidBy(self,paidBy):
        self.paidBy=paidBy

    def getPaidBy(self):
        return self.paidBy

c=Bill()
c.setAmount(200)
print(c.getAmount())

