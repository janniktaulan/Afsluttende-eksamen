from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, hashlib

app = Flask(__name__)
app.secret_key = "hemmelig_nøgle"

def hash_kode(kode):
    return hashlib.sha256(kode.encode()).hexdigest()

@app.route("/")
def index():
    if "brugernavn" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT tid, temperatur, latitude, longitude FROM målinger ORDER BY tid DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()

    return render_template("index.html", data=data, rolle=session.get("rolle"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        brugernavn = request.form["brugernavn"]
        kode = hash_kode(request.form["kode"])

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rolle FROM brugere WHERE brugernavn = ? AND kode = ?", (brugernavn, kode))
        result = cursor.fetchone()
        conn.close()

        if result:
            session["brugernavn"] = brugernavn
            session["rolle"] = result[0]
            return redirect(url_for("index"))
        else:
            return render_template("login.html", fejl="Forkert login")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))