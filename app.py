from flask import Flask, render_template, request
from flask.templating import Environment
from livereload import Server
from werkzeug.useragents import UserAgentParser

app = Flask(__name__)

houses: list[str] = ['hufflepuff',
                     'slytherin', 'gryffindor', 'ravenclaw']
user_number: int = 0


class user:
    id: int
    first_name: str
    last_name: str
    house: str

    def __init__(self, id: int, fname: str, lname: str, house: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.house = house


def find_house(animal: str) -> str:
    if animal == 'eagle':
        return 'ravenclaw'
    elif animal == 'lion':
        return 'gryffindor'
    elif animal == 'badger':
        return 'hufflepuff'
    else:
        return 'slytherin'


users: list[user] = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/results')
def results():
    return render_template('results.html', users=users)


@app.route('/user<usernumber>')
def usernumber(usernumber):
    return render_template('user.html', user=users[int(usernumber)])


@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname = request.form['fname']
        lname = request.form['lname']
        animal = request.form['animal']

        if fname == '' or lname == '':
            return render_template("quiz.html")

        house = find_house(animal)
        new_user = user(user_number, fname, lname, house)

        user_number += 1
        users.append(new_user)

        return render_template("result.html", house=house)
    return render_template("quiz.html")


if __name__ == '__main__':
    app.run(debug=True)
