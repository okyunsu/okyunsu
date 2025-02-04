from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def auth(): 
    return render_template("auth/login.html") 

@app.route('/home')
def home(): 
    return render_template("index.html") 
    print("!홈페이지로 이동")

@app.route('/minus')
def minus():
    print("➖빼기 연산") 
    return render_template("calculator/minus.html")  
  #  print("!@홈페이지로 이동")

@app.route('/plus')
def plus(): 
    print("➕더하기 연산")
    return render_template("calculator/plus.html")

@app.route('/mulitiple')
def mulitiple(): 
    print("✖️곱하기 연산")
    return render_template("calculator/mulitiple.html")

@app.route('/divide')
def divide():
    print("➗나누기 연산") 
    return render_template("calculator/divide.html")


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

 


@app.route('/login', methods=["post"])
def login(): 
    print("😊로그인 알고리즘")
    userid = request.form.get('userid')
    password = request.form.get('password')
    print("username:", userid)
    print("password:", password)
    if userid == "hong" and password == '1234':    
        print("😀로그인 성공")
        return redirect(url_for('home')) 
    else: 
        print("😒로그인 실패") 
        return render_template("auth/logout.html")
    

    #form태그 사용
    
@app.route('/plus', methods=['POST'])
def plus_anwse():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')


    num1, num2 = int(num1), int(num2)
    result = num1 + num2 
    return render_template('answer/plus.html', num1=num1, num2=num2, result=result)

@app.route('/minus', methods=['POST'])
def minus_answer():

    num1 = request.form.get('num1')
    num2 = request.form.get('num2')


    num1, num2 = int(num1), int(num2)
    result = num1 - num2  

    return render_template('answer/minus.html', num1=num1, num2=num2, result=result)


@app.route("/divide", methods = ['POST'])
def divide_anwser():
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")            


    num1, num2 = int(num1), int(num2)
    result = num1 / num2
        
    return render_template("answer/divide.html", num1=num1, num2=num2, result=result)

 


@app.route("/mulitiple", methods = ['POST'])
def mulitiple_anwser():
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")
    print("num1", num1)
    print("num2", num2) 

    num1, num2 = int(num1), int(num2)
    result = num1 * num2

    return render_template("answer/mulitiple.html", num1=num1, num2=num2, result=result)


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True