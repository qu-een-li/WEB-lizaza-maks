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
from data.search_stud import SearchForm


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


@app.route('/search', methods=['POST', 'GET'])
def search():
    form = SearchForm()
    if request.method == "POST":
        session = db_session.create_session()
        query = session.query(Student)
        if form.name_student.data:
            query = query.filter(Student.name_student.ilike(f'%{form.name_student.data}%'))
        if form.name_parent.data:
            query = query.filter(Student.name_parent.ilike(f'%{form.name_parent.data}%'))
        if form.birthday.data:
            query = query.filter(Student.birthday == form.birthday.data)
        if form.document.data:
            query = query.filter(Student.document.ilike(f'%{form.document.data}%'))
        if form.region.data:
            city_title = next((city["title"] for city in get_cities_data(int(form.region.data))
                               if str(city["id"]) == form.city.data), "")
            query = query.filter(Student.city == city_title)
        if form.school.data:
            school_title = next((school["title"] for school in get_schools_data(int(form.city.data))
                                 if str(school["id"]) == form.school.data), "")
            query = query.filter(Student.school == school_title)
        if form.PFDO.data:
            query = query.filter(Student.PFDO == form.PFDO.data)
        if form.parent_phone.data:
            query = query.filter(Student.parent_phone.ilike(f'%{form.parent_phone.data}%'))
        if form.student_phone.data:
            query = query.filter(Student.student_phone.ilike(f'%{form.student_phone.data}%'))
        if form.school_class.data:
            query = query.filter(Student.school_class == form.school_class.data)
        if form.adres_of_living.data:
            query = query.filter(Student.adres_of_living.ilike(f'%{form.adres_of_living.data}%'))
        students = query.all()
        return render_template("students.html", students=students)
    return render_template("search.html", form=form)


if __name__ == '__main__':
    db_session.global_init("db/reg_form.db")
    app.run(port=8080, host='127.0.0.1')
