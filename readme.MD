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

With these steps completed, you have a basic Flask project structure ready for development. Happy coding!
