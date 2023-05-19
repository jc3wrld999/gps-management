from flask import Flask

app = Flask(__name__)

@app.route('/gps-management')
def hello_py():
    return 'hello py!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')