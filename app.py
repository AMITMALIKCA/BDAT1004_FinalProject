from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, This is Amit Malik'

@app.route('/dashboard')
def products():
    return 'dashboard'

if __name__=="__main__":
    app.run(debug=True, port=5000)