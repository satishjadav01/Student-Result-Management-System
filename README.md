# Student Result Management System

A comprehensive web application built with Flask for managing student information, courses, and academic results. This system provides a user-friendly interface for administrators to handle student data, course details, and result tracking in an educational institution.

## Features

- **User Authentication**: Secure login and signup system with Flask-Login
- **Student Management**: Add, edit, view, and delete student records
- **Course Management**: Manage course information including codes, names, descriptions, and credits
- **Result Management**: Record and track student grades, scores, and academic performance
- **Dashboard**: Overview of system statistics and quick access to main functions
- **Responsive Design**: Clean, modern UI using Bootstrap and custom CSS
- **Data Validation**: Form validation using WTForms
- **Database Integration**: SQLite database with SQLAlchemy ORM

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF with WTForms
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Templating**: Jinja2

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/student-result-management-system.git
   cd student-result-management-system
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Environment Variables (Optional):**
   - Set `SECRET_KEY` environment variable for enhanced security
   - Set `DATABASE_URL` if using a different database (default: SQLite)

2. **Database Initialization:**
   The application will automatically create the database and tables when first run.

## Usage

1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:5000`

3. **First Time Setup:**
   - Visit the signup page to create an admin account
   - Login with your credentials

4. **Main Features:**
   - **Dashboard**: View system overview and statistics
   - **Students**: Manage student records (add, edit, view, delete)
   - **Courses**: Manage course information
   - **Results**: Record and manage student results

## Database Schema

The application uses the following main entities:

- **User**: Authentication and user management
- **Student**: Student personal and academic information
- **Course**: Course details and metadata
- **Result**: Academic results linking students to courses

## Project Structure

```
student-result-management-system/
├── app.py                 # Main application file
├── config.py              # Configuration settings
├── models.py              # Database models
├── forms.py               # WTForms definitions
├── auth.py                # Authentication blueprint
├── main.py                # Main routes blueprint
├── courses.py             # Course management blueprint
├── students.py            # Student management blueprint
├── results.py             # Result management blueprint
├── requirements.txt       # Python dependencies
├── instance/              # Database files
├── static/                # Static files (CSS, JS)
│   ├── style.css
│   └── script.js
└── templates/             # Jinja2 templates
    ├── base.html
    ├── dashboard.html
    ├── login.html
    ├── signup.html
    ├── courses/
    ├── students/
    └── results/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Screenshots

*Add screenshots of your application here*

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

## Acknowledgments

- Flask documentation and community
- Bootstrap for UI components
- SQLAlchemy for database operations
# Student-Result-Management-System
