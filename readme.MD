# Preliminary steps in order to create a new Flask project for Blogpost.
# 1. Create a "templates" folder where in you add all your html files and templates.
# 2. create a "static" folder where you add in the css folder containing styles.css
# 3. and other images as required.


# After doing this oppen the terminal on the main folder and chose the pyenv version

# for that : 

    % pyenv local 3.9.0  // This creates a file .python-version and it will contain 3.9.0 in it. The interpreter now knows that locally we will be using python 3.9.0
        # If you encounter something like 3.9.0 not installed. Install pyenv 3.9.0 and proceed
    % pyenv install 3.9.0   
    # After this you need to start the virtual environment using pyenv.
    % pyenv exec python -m venv .venv


# After this we need to install Flask on to the venv.
# How you do this is by first activating the environment using 
    
    % source .venv/bin/Activate // Now you can see that the terminal control has moved into (.venv)
    # Now we can install Flask using the following command
    % pip install flask

    +++++++ Check if the correct interpreter is also chosen in VS Code. Usuall you can find it on the bottom right corner of the IDE

    ++++ Connecting to the database ===== ==== +++++ delete this shit
    # 


