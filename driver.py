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

print (group1.getMembers())
paidBy = {'user1':150,'user2':100,'user3':100,'user4':50,'user5':100}
contribution = {'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}

bill1 = billController.addBill('bill1','group1',500,contribution,paidBy)

balance = billController.getUserBalance('user1')
# print (balance)