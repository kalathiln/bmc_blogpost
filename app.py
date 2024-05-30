from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime
# MongoCLient is used in order to create a client side db session
# to connect with the Mongodb Atlas/ Compass



app = Flask(__name__)

# Make the connection using the connection string
client = MongoClient("mongodb+srv://nikhkk:bdat9LopGNOCwILJ@bmcblogpostazcluster01.isvkrcw.mongodb.net/")
# create a db session now using this connection
app.db = client.microblog

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    # List comprehension
    print([e for e in app.db.entries.find({})])

    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
        # print(entry_content, formatted_date)
        entries.append((entry_content, formatted_date))
        app.db.entries.insert_one({"content" : entry_content, "date" : formatted_date})

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
