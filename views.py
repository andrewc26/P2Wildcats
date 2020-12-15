from flask import Flask, request, render_template
from db_functions import *
import sys

#views from the top

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/catalog')
def catalog():
    cats = get_cats()
    print(cats, file=sys.stderr)

    return render_template("catalog.html", cats=cats)

# @app.route('/search')
# def search_bar():
#     search_query = "travis andrew"
#     x = search(search_query)

if __name__ == "__main__":
	app.run(debug=True) #to visit site, go to http://0.0.0.0:5000
