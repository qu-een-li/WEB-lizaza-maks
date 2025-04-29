import random
import datetime
import requests

from flask import Flask, render_template, request, redirect, make_response, session
from config import KEY_CSRF
from registrationform import RegistrationForm
from data import db_session
from data.students import Student
from data.ways import Way
from flask_login import LoginManager, login_user, logout_user
from flask import jsonify


from api.api_regions import regions_api, get_regions_data
from api.api_cities import cities_api, get_cities_data
from api.api_schools import schools_api, get_schools_data


app = Flask(__name__)
app.config['SECRET_KEY'] = KEY_CSRF

app.register_blueprint(regions_api)
app.register_blueprint(cities_api)
app.register_blueprint(schools_api)


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

    if request.method == "POST":
        if "region" in request.form:
            region_id = request.form["region"]
            cities = get_cities_data(int(region_id))
            form.city.choices = [(str(c["id"]), c["title"]) for c in cities]
            form.school.choices = []

        if "city" in request.form:
            city_id = request.form["city"]
            schools = get_schools_data(int(city_id))
            form.school.choices = [(str(s["id"]), s["title"]) for s in schools]


    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(Student).filter(Student.name_student == form.name_student.data).first():
            return render_template("registration.html", form=form, message="Такой ученик уже существует")

        city_title = next((city["title"] for city in get_cities_data(int(form.region.data))
                           if str(city["id"]) == form.city.data), "")
        school_title = next((school["title"] for school in get_schools_data(int(form.city.data))
                             if str(school["id"]) == form.school.data), "")

        user = Student(name_student=form.name_student.data, name_parent=form.name_parent.data,
                       birthday=form.birthday.data, PFDO=form.PFDO.data,
                       document=form.document.data,
                       city=city_title,
                       school=school_title, parent_phone=form.parent_phone.data,
                       student_phone=form.student_phone.data, school_class=form.school_class.data,
                       adres_of_living=form.adres_of_living.data)
        session.add(user)
        session.commit()
        return redirect("/post")
    return render_template("registration.html", form=form)


if __name__ == '__main__':
    db_session.global_init("db/reg_form.db")
    app.run(port=8080, host='127.0.0.1')
