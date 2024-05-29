from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
        print(entry_content, formatted_date)
        entries.append((entry_content, formatted_date))

        # Now here we need to reformat the date and add it as additional formatting
        entries_with_date = [
            (
                entry [0],
                entry[1],
                datetime.datetime.strptime(entry[1], "%d-%m-%Y").strftime("%b %d")
            )
            for entry in entries
        ]


        kwargs = {
            "entries" : entries_with_date
        }
    return render_template("home.html", **kwargs)
