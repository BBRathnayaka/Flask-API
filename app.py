from flask import Flask, redirect, url_for, render_template, request
import requests
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
    github_html = requests.get(f'https://github.com/{site}').text
    soup = BeautifulSoup(github_html, "html.parser")
    repos = soup.find('span',class_="Counter").text
     
    # return result
    return f"Created site - {repos}"

if __name__ == "__main__":
    app.run(debug=True)
