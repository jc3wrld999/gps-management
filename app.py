from flask import Flask

app = Flask(__name__)

@app.route('/gps-management')
def hello_py():
    return 'hello py!'

if __name__ == '__main__':
    app.run(host='localhost', port='5001')