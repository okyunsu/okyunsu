from dataclasses import dataclass

@dataclass
class CalcModel:
    num1 : int
    num2 : int
    result : str
    opcode : str


    @property
    def num1(self) -> int:
        return self._num1
    
    @num1.setter
    def num1(self, num1):
        self._num1 = num1 


    @property
    def num2(self) -> int:
        return self._num2
    
    @num2.setter
    def num2(self, num2):
        self._num2 = num2

    @property
    def result(self) -> str:
        return self._result
    
    @result.setter
    def result(self, result):
        self._result = result


    @property
    def opcode(self) -> str:
        return self._opcode
    
    @opcode.setter
    def opcode(self, opcode):
        self._opcode = opcode



