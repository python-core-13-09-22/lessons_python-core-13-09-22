# * створити сторінку для перегляду списку завдань (табличка з кнопками біля кожного завдання виконано/редагувати/видалити)
# * створити сторінку для можливості створення завдання
#   * назва
#   * опис
#   * крайній термін
# * створити сторінку для можливості редагувати завдання

# це мінімальний функціонал, можна розширяти його як хочете :)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date

HOST = "localhost"
PORT = 5432
LOGIN = "postgres"
PASSWORD = "qwerty"
DB_NAME = "Challenges"
SECRET_KEY = "HKGVIvhjV%^&^*t6%*gbJHVivUYv"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{LOGIN}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = SECRET_KEY

# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey


# engine = create_engine(f'postgresql://{LOGIN}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}', echo=True)

# metadata = MetaData()
# challenges_table = Table('challenges',
#                         metadata,
#                         Column('id', Integer, primary_key=True),
#                         Column('name', String),
#                         Column('description', String),
#                         Column('deadline', Date))

db = SQLAlchemy(app)

class Challenge(db.Model):
    __tablename__ = 'challenges'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    deadline = Column(Date)

    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline

    def __repr__(self):
        return self.name



@app.route("/")
def home():
    
    return render_template("home.html")

@app.route("/list")
def list():
    challenge = db.session.query(Challenge).all()
    data = {
        "challenges": challenge
    }
    print(data)
    return render_template("list.html", data=data)

@app.route("/challenge/<int:id>")
def challenge_info(id):
    challenge = db.session.query(Challenge).get(id)
    return render_template("challenge_info.html", challenge=challenge)

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        name = request.form["Name of Challenge"]
        description = request.form["Description"]
        deadline = request.form["Deadline"]
        challenge= Challenge(name=name,description=description, deadline=deadline)
        if name == '' or deadline == '':
            flash("Whoops! You didn't fill all the lines")
            return redirect(url_for("add"))
        else:
            db.session.add(challenge)
            db.session.commit()
            flash("Challenge created successfully!")
            return redirect(url_for("list"))
        



@app.route('/update/<int:id>', methods = ['POST', 'GET'])
def update(id):
    challenge_to_update = Challenge.query.get_or_404(id)
    if request.method == 'POST':
        challenge_to_update.name = request.form['Name of Challenge']
        challenge_to_update.description = request.form['Description']
        challenge_to_update.date = request.form['Deadline']
        try:
            if challenge_to_update.name =='' or challenge_to_update.date == '':
                redirect (url_for("update"))
            else:
                db.session.commit()
                flash("Updated Successfully!")
                return redirect(url_for("list"))
        except:
            flash("Error! Looks like there was a problem, try again")
            return render_template('update.html',
                        challenge_to_update=challenge_to_update )

    else:
        return render_template('update.html',
                        challenge_to_update=challenge_to_update )




@app.route('/delete/<int:id>')
def delete(id):
    challenge_to_delete = Challenge.query.get_or_404(id)
        
    db.session.delete(challenge_to_delete)
    db.session.commit()
    flash("Deleted succesfully")
    challenge = db.session.query(Challenge).all()
    data = {
        "challenges": challenge
    }
    print(data)
    return render_template("list.html", data=data)


    



if __name__ == "__main__":
    # metadata.create_all(engine)
    app.run(debug=True)