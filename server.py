import random
import datetime

from flask import Flask, render_template, request, redirect, make_response, session
from config import KEY_CSRF
from registrationform import RegistrationForm
from data import db_session
from data.students import Student
from data.ways import Way
from flask_login import LoginManager, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY_CSRF
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Student).get(user_id)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/students', methods=['GET'])
def students():
    session = db_session.create_session()
    students = session.query(Student).all()
    return render_template("students.html", students=students)


@app.route('/post', methods=['POST', 'GET'])
def post():
    form = RegistrationForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(Student).filter(Student.name_student == form.name_student.data).first():
            return render_template("registration.html", form=form, message="Такой ученик уже существует")
        user = Student(name_student=form.name_student.data, name_parent=form.name_parent.data,
                       birthday=form.birthday.data, PFDO=form.PFDO.data,
                       pasport_number=form.pasport_number.data, pasport_series=form.pasport_series.data,
                       school=form.school.data, parent_phone=form.parent_phone.data,
                       student_phone=form.student_phone.data, school_class=form.school_class.data,
                       adres_of_living=form.school.data)
        session.add(user)
        session.commit()
        return redirect("/post")
    return render_template("registration.html", form=form)


if __name__ == '__main__':
    db_session.global_init("db/reg_form.db")
    app.run(port=8080, host='127.0.0.1')
