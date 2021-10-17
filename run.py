from logging import debug
from market import app

#This will make sure that run.py file has executed directly and not imported
if __name__ == "__main__":
    app.run(debug=True)