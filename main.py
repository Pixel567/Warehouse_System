from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/check_login", methods=["POST"])
def check_login():

    username = request.form['username']
    password = request.form['password']

    database = sqlite3.connect(r"C:\Users\Eryk Tamm\Desktop\Projekty\warehouse_system.db")
    cur = database.cursor()
    exists = cur.execute("SELECT * FROM users WHERE username = ? and password = ?", (username, password)).fetchone()
    print(cur)
    print(exists)
    if exists:
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run(debug=True)