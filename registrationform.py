from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    name_parent = StringField('ФИО Родителя', validators=[DataRequired()])
    name_student = StringField('ФИО Ребёнка', validators=[DataRequired()])
    birthday = StringField('Дата Рождения Ребёнка', validators=[DataRequired()])
    pasport_number = IntegerField('Номер Паспорта', validators=[DataRequired()])
    pasport_series = IntegerField('Серия Паспорта', validators=[DataRequired()])
    school = StringField('Школа, местоположение школы', validators=[DataRequired()])
    PFDO = IntegerField('ПФДО', validators=[DataRequired()])
    parent_phone = StringField('Телефон Родителя', validators=[DataRequired()])
    student_phone = StringField('Телефон Ученика', validators=[DataRequired()])
    school_class = IntegerField('Класс обучения ребёнка', validators=[DataRequired()])
    adres_of_living = StringField('Адрес Проживания', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
