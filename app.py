import flask
from flask import render_template
import time

app = flask.Flask(__name__,)
app._static_folder = 'static'


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/output')
def predict():
    from bmodel import a, score
    return render_template("output.html", score = score, subjects = a )

@app.route('/describe')
def describe():
    return render_template('describe.html')

@app.route('/confidence')
def conf():
    return render_template('confidence.html')

@app.route('/hypothesis')
def hypothesis():
    from results import result_string
    return render_template('hypothesis.html', hypothesis = result_string)

if __name__ == "__main__":
    app.run(debug=True)

app.run()
