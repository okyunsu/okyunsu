from com.okyunsu.auth.login_model import LoginModel
from com.okyunsu.auth.login_service import LoginService


class LoginController:
    def __init__(self):
        pass

    def getResult(self, login:LoginModel) -> LoginModel: 
        service = LoginService()
        return service.login(login)