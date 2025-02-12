from com.okyunsu.grade.grade_modle import GradeModel
from com.okyunsu.grade.grade_service import GradeService


class GradeController:
    def __init__(self, **kwrgs):
        self.name = kwrgs.get("name")
        self.korean = kwrgs.get("korean")
        self.english = kwrgs.get("english")
        self.math = kwrgs.get("math")
        self.society = kwrgs.get("society")
        self.science = kwrgs.get("science")

    def GetResult(self, grade: GradeModel):
        service = GradeService()
        grade.name = self.name
        grade.korean = self.korean
        grade.english = self.english
        grade.math = self.math
        grade.society = self.society
        grade.science = self.science
        

        return service.excute(grade)