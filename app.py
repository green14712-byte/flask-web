from flask import Flask, render_template, request

app = Flask(__name__)

# Home 페이지
@app.route('/')
def home():
    return render_template('home.html')

# 구구단 페이지
@app.route('/gugudan', methods=['GET', 'POST'])
def gugudan():
    result = []
    if request.method == 'POST':
        try:
            dan = int(request.form['dan'])
            result = [f'{dan} x {i} = {dan * i}' for i in range(1, 10)]
        except ValueError:
            result = ['숫자를 입력하세요.']
    return render_template('gugudan.html', result=result)

# 계산기 페이지
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            expression = request.form['expression']
            result = f"{expression} = {eval(expression)}"
        except Exception as e:
            result = f"오류: {e}"
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
