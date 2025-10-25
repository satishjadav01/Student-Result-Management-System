from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from models import db, Student
from forms import StudentForm

students = Blueprint('students', __name__)

@students.route('/')
@login_required
def list_students():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    if search:
        students_list = Student.query.filter(
            (Student.student_id.contains(search)) |
            (Student.first_name.contains(search)) |
            (Student.last_name.contains(search)) |
            (Student.email.contains(search))
        ).paginate(page=page, per_page=10)
    else:
        students_list = Student.query.paginate(page=page, per_page=10)
    return render_template('students/list.html', students=students_list, search=search)

@students.route('/add', methods=['GET', 'POST'])
@login_required
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            student_id=form.student_id.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            date_of_birth=form.date_of_birth.data
        )
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully!')
        return redirect(url_for('students.list_students'))
    return render_template('students/add.html', title='Add Student', form=form)

@students.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.student_id = form.student_id.data
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.email = form.email.data
        student.phone = form.phone.data
        student.address = form.address.data
        student.date_of_birth = form.date_of_birth.data
        db.session.commit()
        flash('Student updated successfully!')
        return redirect(url_for('students.list_students'))
    return render_template('students/edit.html', title='Edit Student', form=form, student=student)

@students.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully!')
    return redirect(url_for('students.list_students'))
