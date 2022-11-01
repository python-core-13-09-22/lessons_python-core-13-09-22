from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.templating import render_template

my_app = Flask(__name__)


class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


USERS = [User("test", "test@test.ua", 25)]


@my_app.route('/')
def hello_world():
    return render_template('base.html')


@my_app.route('/test')
def hello_test():
    return 'Hello, Test!'


@my_app.route('/add/<a>/<int:b>')
def add_a_b(a, b):
    response = f"a:{a} type:{str(type(a))[1:-1]}<br>"
    response += f"b:{b} type:{str(type(b))[1:-1]}<br>"
    response += f"a+b = {int(a) + b}"
    return response


@my_app.route('/operation/<a>/<int:b>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def oper_a_b(a, b):
    response = f"a:{a} type:{str(type(a))[1:-1]}<br>"
    response += f"b:{b} type:{str(type(b))[1:-1]}<br>"
    a = int(a)
    if request.method == "GET":
        response += f"a+b = {a + b}"
    if request.method == "POST":
        response += f"a*b = {a * b}"
    if request.method == "PUT":
        response += f"a-b = {a - b}"
    if request.method == "DELETE":
        response += f"a/b = {a / b}"

    return response


@my_app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == "GET":
        return render_template('user_list.html', my_data=USERS)


@my_app.route('/user_create', methods=['GET', 'POST'])
def user_create():
    if request.method == "GET":
        return render_template('user_create.html')
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        user = User(name, email, age)
        USERS.append(user)
        return redirect(url_for("user"))


if __name__ == '__main__':
    my_app.run()
