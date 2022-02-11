from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/play')
def playground1():
    return render_template('level_1.html')

@app.route('/play/<int:x>')
def playground2(x):
    return render_template('level_2.html', x = x)

@app.route('/play/<int:x>/<string:color>')
def playground3(x, color):
    return render_template('level_3.html', x = x, color = color)

if __name__=="__main__":
    app.run(debug=True)