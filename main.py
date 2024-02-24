from flask import Flask, render_template, url_for, session, request, redirect, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "404 error"
app.permanent_session_lifetime = timedelta(minutes= 1)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/info")
def infopage():
    return

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        Starter_Deposit = request.form["Deposit"]
        Monthly_Saving = request.form["Monthly Saving"]
        Period_Time = request.form["Period of Time"]

        if Starter_Deposit == "" or Starter_Deposit == "0":
            flash("Please fill the form")
            return redirect(url_for("form"))
        elif Monthly_Saving == "" or Monthly_Saving == "0":
            flash("Please fill the form")
            return redirect(url_for("form"))
        elif Period_Time == "" or Period_Time == "0":
            flash("Please fill the form")
            return redirect(url_for("form"))
        else:
            session["Deposit"] = Starter_Deposit
            session["Monthly Saving"] = Monthly_Saving
            session["Period of Time"] = Period_Time
            return redirect(url_for("option"))

    if "Deposit" or "Monthly Saving" or "Period of Time" in session:
        session.pop("Deposit", None)
        session.pop("Monthly Saving", None)
        session.pop("Period of Time", None)

    return render_template("form.html")

@app.route("/option")
def option():

    return render_template("option.html")


if __name__ == "__main__":
    app.run(debug=True)



