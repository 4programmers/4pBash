from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Witaj na bashu serwisu 4programmers.net!'

if __name__ == '__main__':
    app.run()
