from dataclasses import dataclass

@dataclass
class LoginModel:
    userid : str
    password : str
    result : str


    @property
    def userid(self) -> str:
        return self._userid
    
    @userid.setter
    def userid(self, userid):
        self._userid = userid 


    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password

    @property
    def result(self) -> str:
        return self._result
    
    @result.setter
    def result(self, result):
        self._result = result

