from flask import Flask, redirect, url_for
from flask_login import LoginManager
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes after app initialization to avoid circular imports
from auth import auth as auth_blueprint
from main import main as main_blueprint
from courses import courses as courses_blueprint
from students import students as students_blueprint
from results import results as results_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(main_blueprint)
app.register_blueprint(courses_blueprint, url_prefix='/courses')
app.register_blueprint(students_blueprint, url_prefix='/students')
app.register_blueprint(results_blueprint, url_prefix='/results')

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
