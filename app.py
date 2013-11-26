from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
app.debug=True

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    # fetch patients from https://patients.apiary.io/patients
    return render_template('index.html')

@app.route('/send/mail', methods=['POST'])
def send_mail():
    if request.method == 'POST':
        message = request.form['message']
    return message

if __name__ == '__main__':
    app.run()
