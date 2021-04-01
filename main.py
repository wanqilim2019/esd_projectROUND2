from flask import Flask, render_template, redirect, url_for, request
import requests


app = Flask(__name__)
app.config["DEBUG"] = True
# auto reload


@app.route("/")
def show_landing_page():
    return render_template("index1.html")


@app.route("/signup")
def show_signuppage():
    return render_template('signup.html')


@app.route("/login", methods=['GET', 'POST'])
def show_login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM customer WHERE email = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['cid'] = account['cid']
            session['email'] = account['email']
            session['cname'] = account['cname']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template("login.html", msg=msg)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
