
from com.okyunsu.calc.calc_model import CalcModel
from com.okyunsu.calc.calc_service import Calc_Service


class CalcController:
    def __init__(self):
        pass

    def getResult(self, calc: CalcModel):
        service = Calc_Service()
        return service.excute(calc)