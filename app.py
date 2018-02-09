from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/about')
def about():
    pass

@app.route('/gallery')
def gallery():
    pass

@app.route('/product')
def product():
    pass

@app.route('/profile')
def profile():
    pass

@app.route('/contact')
def contact():
    pass

@app.route('/clients')
def clients():
    pass

app.run(port=5000, debug=True)
