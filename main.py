from flask import Flask, render_template, redirect, url_for, request, jsonify, session
import requests
import sys
import hashlib

from flask_cors import CORS

import os
import sys
from os import environ

import requests
from invokes import invoke_http


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
app.secret_key = 'esdT6thebest'


cuslogin_URL = environ.get('cuslogin_URL') or "http://localhost:5003/customer"
bizlogin_URL = environ.get('bizlogin_URL') or "http://localhost:5004/business"


@app.route("/")
def home():
    msg = ''
    if 'acctType' in session:
        if session['acctType'] == 'customer':
            return render_template("index1.html", user=session['data']['cname'])
        else:
            return render_template("index1.html", user=session['data']['bname'])
    return render_template("index1.html", msg=msg)


@app.route("/signup")
def show_signuppage():
    return render_template('signup.html')


@app.route("/market")
def show_marketplace():
    return render_template('marketplace.html')


@app.route("/login")
def login():
    msg = ''
    return render_template('Loginpage.html', msg=msg)


@app.route("/login", methods=['POST'])
def configure_login():
    msg = ''
    account_type = request.form['acctType']
    print(request.form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:

        email = request.form['email']
        password = hashlib.md5(
            request.form['password'].encode('utf-8')).hexdigest()

        if (account_type == "customer"):
            login_result = invoke_http(
                cuslogin_URL+'/'+email, method='POST', json={"email": email, "password": password})
        elif(account_type == "business"):
            login_result = invoke_http(
                bizlogin_URL+'/'+email, method='POST', json={"email": email, "password": password})
        else:
            msg = 'Please select a account type!'
            return render_template('Loginpage.html', msg=msg)

        if login_result['code'] == 200:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['acctType'] = account_type
            session['data'] = login_result['data']
            # print(login_result, file=sys.stderr)
            # print(session, file=sys.stderr)

            # Redirect to home page
            msg = 'Logged in successfully!'
            
            if (account_type == "customer"):
                return render_template("index1.html", user=session['data']['cname'])
            else:
                return render_template("index1.html", user=session['data']['bname'])

        msg = 'Incorrect username/password!'
        return render_template('Loginpage.html', msg=msg)


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('acctType', None)
   session.pop('data', None)
   # Redirect to login page
   return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
