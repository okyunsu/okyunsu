from com.okyunsu.calc.calc_model import CalcModel


class Calc_Service:
    def __init__(self):
        pass

    def excute(self, calc: CalcModel):
        num1 = calc.num1
        num2 = calc.num2
        opcode = calc.opcode
        
        if opcode == "+":
            print("덧셈 실행")
            result = num1 + num2 
        elif opcode == "-":
            print("뺄셈 실행")
            result = num1 - num2          
        elif opcode == "/":
            print("나눗셈 실행")
            result = num1 / num2          
        elif opcode == "*":
            print("곱셈 실행")
            result = num1 * num2            
        else:            
            result = "잘못된 입력입니다"

        calc.result = result

        return calc