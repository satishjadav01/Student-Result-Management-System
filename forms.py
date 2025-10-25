from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, FloatField, DateField, SelectField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class CourseForm(FlaskForm):
    course_code = StringField('Course Code', validators=[DataRequired(), Length(max=20)])
    course_name = StringField('Course Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description')
    credits = IntegerField('Credits', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Save')

class StudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired(), Length(max=20)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[Length(max=20)])
    address = TextAreaField('Address')
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    submit = SubmitField('Save')

class ResultForm(FlaskForm):
    student_id = SelectField('Student', coerce=int, validators=[DataRequired()])
    course_id = SelectField('Course', coerce=int, validators=[DataRequired()])
    grade = SelectField('Grade', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], validators=[DataRequired()])
    score = FloatField('Score', validators=[DataRequired(), NumberRange(min=0, max=100)])
    semester = StringField('Semester', validators=[DataRequired(), Length(max=20)])
    academic_year = StringField('Academic Year', validators=[DataRequired(), Length(max=10)])
    exam_date = DateField('Exam Date', validators=[DataRequired()])
    submit = SubmitField('Save')
