from flask import Flask, render_template, redirect, request, url_for
from flask.templating import Environment
from livereload import Server

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/user<int:user>')
def user(user):
    return f'You are user {user}'


ButtonPressed = 0


@app.route('/quiz', methods=["GET", "POST"])
def button():
    if request.method == "POST":

        return render_template("quiz.html", ButtonPressed='goodbye')
        # I think you want to increment, that case ButtonPressed will be plus 1.
    return render_template("quiz.html", ButtonPressed='hello')


if __name__ == '__main__':
    app.run(debug=True)
