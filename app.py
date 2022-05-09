import os
import flask
import urllib
import numpy as np
from flask import Flask, render_template, redirect, url_for, Response, request, session

app = Flask(__name__)


def isOperand(x):
	return ((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'))

# Get Infix for a given postfix
# expression
def getInfix(exp) :
    s = []
    for i in exp:	
        # Push operands
        if (isOperand(i)) :		
            s.insert(0, i)
			
		# We assume that input is a
		# valid postfix and expect
		# an operator.
        else:
            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i + op1 + ")")
			
	# There must be a single element in
	# stack now which is the required
	# infix.
    return s[0]



@app.route('/')
def home():
        return render_template("home.html")

@app.route('/convert_p' ,methods=["GET", "POST"])
def convert_p():
    string = request.form.get("post-in", False)
    output = getInfix(string.strip())

    return render_template('potoi_res.html', converted_text='{}'.format(output))

@app.route('/potoi')
def potoi():
        return render_template("potoi.html")

if __name__ == "__main__":
    app.run(debug=True)




