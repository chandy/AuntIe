# AuntIe
The AI powered helper for your family

Make sure you install the VSCode python extension along with Pylint.  It will probably prompt you to do it once you open main.py.

# commands to run

This will set up your virtual environment where your python deps will get installed

`python -m venv venv`
`source venv/bin/activate`

Then install all dependencies

`pip install -r requirements.txt`

To run the app

`uvicorn main:app --reload`

This will kick off the FastAPI app and you should get a prompt on how to open it in a new browser tab.  Codespaces will pick that for you.

If Pylint complains about unable to find imports, you might need to make sure vscode is using the pylint installed with the virtual environment and not the default one.  To do this:

1. Hit "ctrl" + ","
2. Search for "pylint import"
3. Change dropdpwn to "fromEnvironment"
4. Click on the Codespaces icon in the bottom left and click "Rebuild Container"

