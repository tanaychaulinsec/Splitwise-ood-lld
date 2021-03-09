from controlers.user_controller import UserController
from controlers.group_controller import GroupController
from controlers.bill_controller import BillController

from services.bill_services import BillService
from services.user_services import UserService
from services.group_services import GroupService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())


user1 = userController.addUser('user1','tanay')
user2 = userController.addUser('user2','sombit')
user3 = userController.addUser('user3','rohit')
user4 = userController.addUser('user4','sumit')
user5 = userController.addUser('user5','manoj')

members = [user1,user2,user3,user4,user5]
group1 = groupController.addGroup('g001','megapolis',members)

#print (group1.getMembers())
paidBy={'user1':50,'user2':250,'user3':200,'user4':300,'user5':100}
contribution={'user1':500,'user2':100,'user3':100,'user4':100,'user5':100}

bill = billController.addBill('bill1','group1',900,contribution,paidBy)
invoice={}
for user in contribution.keys():
    balance= billController.getUserBalance(user)
    invoice[user]=balance
print("Expense of this month is\n")
for userName , status in invoice.items():
    print ( userName+":" + status)
print("\n")
