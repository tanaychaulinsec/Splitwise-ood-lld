class BillController(object):
    def __init__(self, billServices):
        self.billServices = billServices

    def addBill(self, id, groupId, amount, contribution, paidBy):
        return self.billServices.addBill(id, groupId, amount, contribution, paidBy)

    def getUserBalance(self, userId):
        balance = 0
        for bilId in self.billServices.billDetails:
            bill = self.billServices.billDetails.get(bilId)
            if userId in bill.getContribution():
                balance -= bill.getContribution().get(userId)
            if userId in bill.getPaidby():
                balance+=bill.getPaidby().get(userId)
        if balance<0:
            status= " owe:"+str(abs(balance))

        elif balance>0:
            status= " owes:"+str(balance )

        else: status= " settle-up all balance"
        return status
