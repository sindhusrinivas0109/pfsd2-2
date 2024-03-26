from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/a')
def hello1():
    return 'Welcome to PFSD - S11 Section'
@app.route('/emp/<int:emp1>')
def show(emp1):
    return 'EMP ID Number %d' %emp1

@app.route('/emp/<float:emp1>')
def show1(emp1):
    return 'EMP ID Number %f' %emp1

@app.route('/ex1')
def index():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)