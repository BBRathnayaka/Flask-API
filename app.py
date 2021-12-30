from flask import Flask, redirect, url_for, render_template, request
import requests
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
       domain = request.form["dname"]
       return redirect(url_for("site", site=domain))
    else:
        return render_template("create.html")

@app.route("/<site>")
def site(site):

    GITLAB_TOKEN = 'glpat-YtoG4jamqJDzMB9xc_67'
    url = f"https://gitlab.com/api/v4/projects/"
    head = {'Authorization': 'Bearer {}'.format(GITLAB_TOKEN)}
    params = {'name': {site}, 'visibility': 'private'}

    r = requests.post(url, headers=head, params=params)
    return json.dumps(r.json())

if __name__ == "__main__":
    app.run(debug=True)
