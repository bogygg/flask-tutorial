from random import choice

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # переменные phrases и text на данном этапе не используются
    phrases = (
        "Добро пожаловать!",
        "Добрый день!",
        "Приветствуем Вас!",
        "Здравствуйте!",
        "Рады Вас видеть!",
    )

    text = choice(phrases)

    return render_template("index.html")


@app.route("/about")
def about():
    return "Наша компания основана в 2022-м году"


app.run()
