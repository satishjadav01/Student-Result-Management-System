from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from models import db, Course
from forms import CourseForm

courses = Blueprint('courses', __name__)

@courses.route('/')
@login_required
def list_courses():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    if search:
        courses_list = Course.query.filter(
            (Course.course_code.contains(search)) |
            (Course.course_name.contains(search))
        ).paginate(page=page, per_page=10)
    else:
        courses_list = Course.query.paginate(page=page, per_page=10)
    return render_template('courses/list.html', courses=courses_list, search=search)

@courses.route('/add', methods=['GET', 'POST'])
@login_required
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(
            course_code=form.course_code.data,
            course_name=form.course_name.data,
            description=form.description.data,
            credits=form.credits.data
        )
        db.session.add(course)
        db.session.commit()
        flash('Course added successfully!')
        return redirect(url_for('courses.list_courses'))
    return render_template('courses/add.html', title='Add Course', form=form)

@courses.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_course(id):
    course = Course.query.get_or_404(id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        course.course_code = form.course_code.data
        course.course_name = form.course_name.data
        course.description = form.description.data
        course.credits = form.credits.data
        db.session.commit()
        flash('Course updated successfully!')
        return redirect(url_for('courses.list_courses'))
    return render_template('courses/edit.html', title='Edit Course', form=form, course=course)

@courses.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash('Course deleted successfully!')
    return redirect(url_for('courses.list_courses'))
