from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime
# MongoCLient is used in order to create a client side db session
# to connect with the Mongodb Atlas/ Compass

# We are using the Python App factory mechanism :
# 1. We should avoid having the db connection and storing in the same main file.
# 2. This will result in complicated code which will not be scalable and secure.
# 3. During deployment of this file, maybe this app will be called multiple times, 
#       therby creating multiple instances of the database clients.
#       Using the app factory mechanism, we can avoid it, 
#       by enabling the deployment mechanism to be smart enough to run only one instance of the app,
#        even though it has been called multiple times. 
def create_app():
    app = Flask(__name__)

    # Make the connection using the connection string
    client = MongoClient("mongodb+srv://nikhkk:bdat9LopGNOCwILJ@bmcblogpostazcluster01.isvkrcw.mongodb.net/")
    # create a db session now using this connection
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        # List comprehension
        print([e for e in app.db.entries.find({})])

        if request.method == "POST":
            # Flask lets you access the request form, and get information, 
            # in this case the content[name of the textArea on the html file] of the blogpost.  
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
            app.db.entries.insert_one({"content" : entry_content, "date" : formatted_date})

        # Reformat the date and add it as additional formatting: 
        # Forgot why we are doing this, but remember it being a big deal.
        entries_with_date = [
            (
                entry ["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%d-%m-%Y").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]

        #  **kwargs is a special syntax that allows us to pass a variable length of keyword arguments to the function.
        #   - It means : Keyword Arguments
        kwargs = {
            "entries" : entries_with_date
        }
        return render_template("home.html", **kwargs)
    return app
