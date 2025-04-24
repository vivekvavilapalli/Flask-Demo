from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def name():
    if request.method == "POST":
        user = request.form['usr_name']
        pattern = r"^[A-Z][a-z]+(?:[-'\s][A-Z][a-z]+)*$"
        if re.match(pattern, user):
            return redirect(url_for('phone', username=user))
        else:
            message = "Invalid name. Please enter a valid name (e.g., John, Anne-Marie)"
            return render_template("home.html", message=message)
    return render_template("home.html")

@app.route('/phone', methods=["GET", "POST"])
def phone():
    username = request.args.get('username', '')
    if request.method == "POST":
        number = request.form['phone']
        pattern = r'^\+91\d{10}$'
        if re.match(pattern, number):
            # Pass phone number via query params
            return redirect(url_for('email', username=username, phnnumber=number))
        else:
            message = "Invalid Number. Please enter a valid Phone Number (e.g., +911234567890)"
            return render_template("phone.html", username=username, message=message)
    return render_template("phone.html", username=username)

@app.route('/email', methods=["GET", "POST"])
def email():
    username = request.args.get('username', '')
    phnnumber = request.args.get('phnnumber', '')
    if request.method == "POST":
        Email = request.form['email']
        pattern = r'^[\w\.-]+@(?:gmail\.com|org\.in|hotmail\.com)$'
        if re.match(pattern, Email):
            return render_template("final.html", username=username, phnnumber=phnnumber, Email=Email)
        else:
            message = "Invalid Email. Please enter a valid email (e.g., yourname@gmail.com)"
            return render_template("email.html", username=username, phnnumber=phnnumber, message=message)
    return render_template("email.html", username=username, phnnumber=phnnumber)

if __name__ == '__main__':
    app.run(debug=True)
