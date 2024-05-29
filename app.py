from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%M-%D")
        print(entry_content, formatted_date)
    return render_template("home.html")
