from flask import Flask, render_template


app = Flask(__name__, template_folder="template", static_folder="data/static")

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/menu/")
def menu():
    context = {


}

    return render_template("menu.html", **context")
