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
            return render_template("marketplace.html", user=session['data']['cname'])
        else:
            return render_template("marketplace.html", user=session['data']['bname'])
    return render_template("marketplace.html", msg=msg)


@app.route("/signup")
def show_signuppage():
    return render_template('signup.html')

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
            
            return redirect(url_for('.login',msg =msg))

        if login_result['code'] == 200:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['acctType'] = account_type
            session['data'] = login_result['data']
            # print(login_result, file=sys.stderr)
            # print(session, file=sys.stderr)

            # Redirect to home page
            msg = 'Logged in successfully!'
            
            return redirect(url_for('.home',msg =msg))
            

        msg = 'Incorrect username/password!'
        return redirect(url_for('.login',msg =msg))
    
    
@app.route("/signup", methods=['POST'])
def configure_signup():
    msg = ''
    account_type = request.form['acctType']
    print(request.form)
    if  'email' in request.form :

        email = request.form['email']
        password = hashlib.md5(
            request.form['password'].encode('utf-8')).hexdigest()

        if (account_type == "customer"):
            result = invoke_http(
                cuslogin_URL+'/'+email, method='GET', json={"email": email})
            desc = ''
        elif(account_type == "business"):
            result = invoke_http(
                bizlogin_URL+'/'+email, method='GET', json={"email": email})
            desc = request.form['description'],
        
        

        if result['code'] == 400:
            # Redirect to home page
            mydict = {
                'name':request.form['name'],
                'email':email,
                'password':password,
                'paypal':request.form['paypalemail'],
                'address':request.form['address'],
                'description': desc,
            }
            if (account_type == "customer"):
                registerresult = invoke_http(cuslogin_URL, method='POST', json=mydict)
            elif(account_type == "business"):
                registerresult = invoke_http(bizlogin_URL, method='POST', json=mydict)
        else:
            return  redirect(url_for('.signup',msg ='Customer exists'))
        



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
