from flask import Flask
from flask import render_template


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sms')
def sms():
    return render_template('sms.html')


@app.route('/bamburi')
def bamburi():
    return '<h1>We are now in bamburi !!</h1>'

@app.route('/town/<name>')
def town(name):
    return f'<h1>I am in {name} </h1>'

@app.route('/latin/<name>')
def latin(name):
    if name[len(name)-1]!='y':
        name=name+'y'
    else:
        name=name[:len(name)-1]
        name=name+'iful'
    return '<h1>Your latin is %s </h1>'%name




if __name__ == '__main__':
    app.run(debug=True)
