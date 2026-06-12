Student Registration System – Day 12

**Project Overview**

The Student Registration System is a web-based application developed using Flask and SQLite. This project allows users to register student information through a form and store the data in a database. The registered student details are displayed dynamically on the Students page.

**Technologies Used**

- Python
- Flask
- SQLite
- HTML
- CSS

**Features**

- Student Registration Form
- SQLite Database Integration
- Dynamic Data Storage
- Dynamic Data Display
- Flask Routing
- HTML Templates
- CSS Styling
- Navigation Between Pages

Functional Requirements Implemented

**Student Registration Page**

The registration form collects the following details:

- Student Name
- Roll Number
- Department
- Year
- Email
- Phone Number
- Gender
- Address

**Students List Page**

- Displays all registered student details
- Fetches data dynamically from SQLite database
- Shows student records in a table format

**Flask Backend**

- Database connection using SQLite
- Students table creation
- Data insertion
- Data retrieval
- Route handling
- Form processing using POST method

**Project Structure**

student_registration_system/

│── app.py
│── student.db

├── templates/
│   ├── home.html
│   ├── about.html
│   ├── register.html
│   ├── students.html

├── static/
│   ├── css/
│   │   ├── style.css
│   ├── images/

**How to Run the Project**

1. Open the project folder in VS Code.

2. Open terminal.

3. Install Flask:
   py -m pip install flask

4. Run the application:
   py app.py

5. Open browser and visit:
   http://127.0.0.1:5000

**Testing**

- Registered at least 10 students
- Verified student data storage in SQLite database
- Verified student data display on Students page
- Tested page navigation
- Ensured no insertion or retrieval errors

**Outcome**

Successfully converted the Student Registration System from a frontend prototype into a fully functional Flask and SQLite web application.
