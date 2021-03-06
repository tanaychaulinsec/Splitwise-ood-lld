from services.user_services import UserService
class UserController(object):
    def __init__(self,userServices):
        self.userServices=userServices
    
    def addUser(self,id,name):
        return self.UserService.addUser(id,name)