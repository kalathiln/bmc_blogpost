# Flask Blogpost Project Setup

This guide will walk you through the preliminary steps to create a new Flask project for a blog post application.

## Project Structure

1. **Create a "templates" folder**:
    - This folder will contain all your HTML files and templates.

2. **Create a "static" folder**:
    - Within this folder, create a `css` folder to hold your `styles.css`.
    - You can also add other assets like images as required.

## Setting Up Python Environment

### Choosing Python Version

1. **Open the terminal in the main project folder**.
2. **Set the local Python version**:
    ```bash
    pyenv local 3.9.0
    ```
    - This command creates a `.python-version` file containing `3.9.0`, informing the interpreter to use Python 3.9.0 locally.

3. **If Python 3.9.0 is not installed**:
    ```bash
    pyenv install 3.9.0
    ```

### Creating a Virtual Environment

1. **Start the virtual environment using pyenv**:
    ```bash
    pyenv exec python -m venv .venv
    ```

### Installing Flask

1. **Activate the virtual environment**:
    ```bash
    source .venv/bin/activate
    ```
    - You should see the terminal prompt change to indicate that you're now working within the virtual environment (e.g., `.venv`).

2. **Install Flask**:
    ```bash
    pip install flask
    ```

### Setting Up VS Code

- Ensure that the correct Python interpreter is selected in VS Code.
- Typically, you can find the interpreter option in the bottom right corner of the IDE.


### Connecting Flask to MongoDB Using PyMongo

## Step 1: Install Dependencies
Ensure you have `Flask` and `pymongo` installed in your Python environment.

```bash
pip install Flask pymongo
```

## Step 2: Import Modules
In your Flask application file, import the necessary modules.

```python
from flask import Flask, jsonify, request
from pymongo import MongoClient
```

## Step 3: Initialize Flask App and MongoDB Client
Create a Flask app and initialize the MongoDB client.

```python
app = Flask(__name__)

# Replace the URI with your MongoDB deployment's connection string.
client = MongoClient("mongodb://localhost:27017/")  # Default URI for local MongoDB
db = client.your_database_name  # Replace 'your_database_name' with your actual database name
```

## Step 4: Define Routes
Create routes to interact with the MongoDB database. Here’s a basic example with routes to insert and retrieve data.

```python
@app.route('/insert', methods=['POST'])
def insert_document():
    data = request.json
    result = db.your_collection_name.insert_one(data)  # Replace 'your_collection_name' with your actual collection name
    return jsonify({"inserted_id": str(result.inserted_id)}), 201

@app.route('/find', methods=['GET'])
def find_documents():
    documents = list(db.your_collection_name.find())
    for doc in documents:
        doc["_id"] = str(doc["_id"])
    return jsonify(documents), 200

if __name__ == '__main__':
    app.run(debug=True)
```

## Step 5: Run the Flask App
Run your Flask application.

```bash
python your_flask_app.py
```

## Step 6: Testing the Application
- To insert a document, make a POST request to `/insert` with a JSON payload.
- To retrieve documents, make a GET request to `/find`.

### Example Request
**Insert Document**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "age": 30}' http://localhost:5000/insert
```

**Find Documents**

```bash
curl -X GET http://localhost:5000/find
```

This is a basic setup. Depending on your use case, you might want to add error handling, validation, and more sophisticated querying.
```

With these steps completed, you have a basic Flask project structure ready for development. Happy coding!
