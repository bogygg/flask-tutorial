from random import choice

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    phrases = (
        "Добро пожаловать!",
        "Добрый день!",
        "Приветствуем Вас!",
        "Здравствуйте!",
        "Рады Вас видеть!",
    )

    text = choice(phrases)

    return f"<h1>{text}</h1>"


@app.route("/about")
def about():
    return "Наша компания основана в 2022-м году"


app.run()
