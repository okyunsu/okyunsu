from flask import Flask, render_template, request, redirect, url_for
from com.okyunsu.auth.login_controller import LoginController
from com.okyunsu.auth.login_model import LoginModel
from com.okyunsu.calc.calc_controller import CalcController
from com.okyunsu.calc.calc_model import CalcModel
from com.okyunsu.calc.discount_controller import DiscountController
from com.okyunsu.grade.grade_controller import GradeController
app = Flask(__name__)



@app.route( '/' , methods= ["POST", "GET"])
def login(): 
    print("😊로그인 알고리즘")
    if request.method == "POST":   
        userid = request.form.get('userid')
        password = request.form.get('password')
        print("username:", userid)
        print("password:", password)


        login = LoginModel()
        login.userid = userid
        login.password = password
        print(userid, password)

        controller = LoginController()
        resp: LoginModel = controller.getResult(login)

        return redirect(url_for(resp.result)) 

        
    else:
        return render_template("auth/login.html")
            


@app.route('/fail')
def fail(): 
    return render_template("auth/logout.html") 


@app.route('/home')
def home(): 
    return render_template("index.html") 



# 📌 재무 분석 및 보고 챗봇 개발발
@app.route('/finance_visualizer')
def finance_visualizer():
    return render_template('esg/chatbot/finance_visualizer.html')

@app.route('/report_review')
def report_review():
    return render_template('esg/chatbot/report_review.html')

@app.route('/retail_analysis')
def retail_analysis():
    return render_template('esg/chatbot/retail_analysis.html')

# 📌 ESG 데이터 자동 분석 플랫폼 구축
@app.route('/energy_data_collector')
def energy_data_collector():
    return render_template('esg/financial/energy_data_collector.html')

@app.route('/esg_analysis_tool')
def esg_analysis_tool():
    return render_template('esg/financial/esg_analysis_tool.html')

@app.route('/report_generator')
def report_generator():
    return render_template('esg/financial/report_generator.html')

# 📌 ESG 데이터 기반 재무 영향 자동화 시스템 개발
@app.route('/retail_data_collector')
def retail_data_collector():
    return render_template('esg/analytics/retail_data_collector.html')

@app.route('/healthcare_chatbot_backend')
def healthcare_chatbot_backend():
    return render_template('esg/analytics/healthcare_chatbot_backend.html')

@app.route('/construction_report_generator')
def construction_report_generator():
    return render_template('esg/analytics/construction_report_generator.html')

 

@app.route("/calc", methods = ['POST', 'GET'])
def calc():
    print("전송된 데이터 방식 :", request.method)

    if request.method == "POST":      
        print("post로 진입")         
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")            
        opcode = request.form.get("opcode")
        print("num1:",num1)
        print("num2:",num2)
        print("opcode:",opcode)
        num1, num2 = int(num1), int(num2) 
        
        calc = CalcModel()
        calc.num1 = int(num1)
        calc.num2 = int(num2)
        calc.opcode = opcode

        controller = CalcController()
        resp: CalcModel = controller.getResult(calc)

        print(f"{resp.num1} {resp.opcode} {resp.num2} = {resp.result}")

        return render_template("calculator/calc.html", 
                            num1=resp.num1, num2=resp.num2, opcode=resp.opcode, result = resp.result )

    

    else:
        print("get 방식으로 진입")
        return render_template("calculator/calc.html")



@app.route("/discount", methods =["GET", "POST"])
def discount():

    if request.method == "POST":   
        amount = request.form.get("amount")
        print("🐈amount:", amount)

        controller = DiscountController(amount = amount)
        
        

        return render_template("calculator/discount.html", amount = amount)

    else:
        return render_template("calculator/discount.html")


@app.route("/gugudan", methods =["GET", "POST"])
def gugudan():

    if request.method == "POST":   
        number = request.form.get("number")
        print("number", number)
  
        return render_template("calculator/gugudan.html")
 
    else:
        return render_template("calculator/gugudan.html")
        

@app.route("/grade", methods = ["GET", "POST"])
def grade():

    if request.method == "POST":
        name = request.form.get("name")
        korean = request.form.get("korean")
        english = request.form.get("english")
        math = request.form.get("math")
        society = request.form.get("society")
        science = request.form.get("science")

        controller = GradeController(name = name, korean = korean, english = english, 
                               math = math, society = society, science = science)

        resp = controller.GetResult(grade)
     
        render_html = '<h3>결과보기</h3>'
        render_html += f"{resp.name}님의 성적은 {resp.result}입니다.</by>"
        print(f"🥹 결과", resp.result)

        return render_template("grade/grade.html", render_html = render_html)

    else:
        return render_template("grade/grade.html")




if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True  