"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask , render_template , request , redirect 
import joblib as joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

# Make the WSGI interface available at the top level so wfastcgi can get it.



@app.route('/')
def hello():
    """Renders a sample page."""
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def marks():
    if request.method == 'POST':
        hours = float(request.form['hours'])
        marks = str(model.predict([[hours]]))

    return render_template("index.html", your_marks = marks)


if __name__ == '__main__':
    import os
    
    app.run(debug = True)