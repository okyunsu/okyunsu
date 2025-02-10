
from com.okyunsu.auth.login_model import LoginModel


class LoginService:
    def __init__(self):
        pass

    def login(self, login: LoginModel) -> LoginModel: 
        userid = login.userid
        password = login.password

        if userid == "hong" and password == '1234':    
            print("😀로그인 성공")
            result = "home"
        
        else: 
            print("😒로그인 실패") 
            result = "fail"

        login.result = result

        return login