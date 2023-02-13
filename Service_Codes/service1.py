
# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This service is service1.'
@app.route('/service1')
def service1():
    return 'Hello. I\'m service1.'

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
