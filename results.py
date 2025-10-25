from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from models import db, Result, Student, Course
from forms import ResultForm

results = Blueprint('results', __name__)

@results.route('/')
@login_required
def list_results():
    page = request.args.get('page', 1, type=int)
    results_list = Result.query.join(Student).join(Course).paginate(page=page, per_page=10)
    return render_template('results/list.html', results=results_list)

@results.route('/add', methods=['GET', 'POST'])
@login_required
def add_result():
    form = ResultForm()
    form.student_id.choices = [(s.id, f"{s.student_id} - {s.full_name}") for s in Student.query.all()]
    form.course_id.choices = [(c.id, f"{c.course_code} - {c.course_name}") for c in Course.query.all()]

    if form.validate_on_submit():
        result = Result(
            student_id=form.student_id.data,
            course_id=form.course_id.data,
            grade=form.grade.data,
            score=form.score.data,
            semester=form.semester.data,
            academic_year=form.academic_year.data,
            exam_date=form.exam_date.data
        )
        db.session.add(result)
        db.session.commit()
        flash('Result added successfully!')
        return redirect(url_for('results.list_results'))
    return render_template('results/add.html', title='Add Result', form=form)

@results.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_result(id):
    result = Result.query.get_or_404(id)
    db.session.delete(result)
    db.session.commit()
    flash('Result deleted successfully!')
    return redirect(url_for('results.list_results'))
