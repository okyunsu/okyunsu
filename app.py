from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def login(): 
    return render_template("auth/login.html") 

@app.route('/home')
def home(): 
    return render_template("index.html") 

@app.route('/minus')
def minus(): 
    return render_template("calculator/minus.html")  

@app.route('/plus')
def plus(): 
    return render_template("calculator/plus.html")

@app.route('/mulitiple')
def mulitiple(): 
    return render_template("calculator/mulitiple.html")

@app.route('/divide')
def divide(): 
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

 



if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True