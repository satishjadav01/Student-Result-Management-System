from flask import Blueprint, render_template, request
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/dashboard')
@login_required
def dashboard():
    from models import Student, Course, Result
    total_students = Student.query.count()
    total_courses = Course.query.count()
    total_results = Result.query.count()
    login_success = request.args.get('login_success') == '1'
    return render_template('dashboard.html',
                         total_students=total_students,
                         total_courses=total_courses,
                         total_results=total_results,
                         login_success=login_success)
