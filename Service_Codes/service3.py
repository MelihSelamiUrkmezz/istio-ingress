
# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This service is service3.'
@app.route('/service3')
def service3():
    return 'Hello. I\'m service3.'

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
