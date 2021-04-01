from flask import Flask, render_template,redirect, url_for, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
