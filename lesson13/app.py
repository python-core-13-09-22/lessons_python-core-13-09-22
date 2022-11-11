from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

HOST = "localhost"
PORT = 5432
LOGIN = "postgres"
PASSWORD = "root"
DB_NAME = "core111122"
SECRET_KEY = "HKGVIvhjV%^&^*t6%*gbJHVivUYv"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{LOGIN}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = SECRET_KEY

db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship(Author, backref=db.backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return f"<{self.id}; {self.title}; {self.description}>"


@app.route("/")
def home():
    authors = db.session.query(Author).all()
    books = db.session.query(Book).all()
    data = {
        "authors": authors,
        "books": books
    }
    print(data)
    return render_template("home.html", data=data)


@app.route("/author/<int:id>")
def author_info(id):
    author = db.session.query(Author).get(id)
    return render_template("author/author_info.html", author=author)


@app.route("/author", methods=["GET", "POST"])
def author_create():
    if request.method == "GET":
        return render_template("author/author_create.html")
    if request.method == "POST":
        name = request.form["author_name"]
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()

        return redirect(url_for("author_info", id=author.id))


if __name__ == "__main__":
    app.run()
