from flask import Flask, render_template


app = Flask(__name__, template_folder="template", static_folder="data/static")


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    context = {
        "pizza_1": "Пеперонька",
        "pizza_2": "Акційна",
        "pizza_3": "4 сири"
    }
    return render_template("menu.html", **context)


@app.get("/menu_2/")
def menu_2():
    pizzas = [
        "Пепероні",
        "Класична",
        "Моцарела"
    ]
    return render_template("menu_2.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True)