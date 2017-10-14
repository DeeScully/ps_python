#from . import app
from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    return 'Home Page'

@app.route('/2')
def second_pg():
    return '2nd page'

if __name__ == '__main__':
    app.run()
