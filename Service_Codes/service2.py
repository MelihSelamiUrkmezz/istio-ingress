
# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This service is service2.'
@app.route('/service2')
def service2():
    return 'Hello. I\'m service2.'

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
