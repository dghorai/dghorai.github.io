# -*- coding: utf-8 -*-
"""
Created on Wed Jun 6 2022

@author: Debabrata Ghorai, Ph.D.

Flask application: 
(1) https://flask.palletsprojects.com/en/2.1.x/quickstart/
"""

from flask import Flask, render_template


app = Flask(__name__)


# '/' - main webpage
@app.route('/')
def home():
    return render_template('home.html')

# '/about/' - about page
@app.route('/about/')
def about():
    return render_template('about.html')

# '/projects/' - projects page
@app.route('/projects/')
def projects():
    return render_template('projects.html')

# '/research/' - research page
@app.route('/research/')
def research():
    return render_template('research.html')


# run flask app 
if __name__ == '__main__':
    app.run(debug=True)
