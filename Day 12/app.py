from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database table
def create_table():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll_number TEXT,
        department TEXT,
        year TEXT,
        email TEXT,
        phone TEXT,
        gender TEXT,
        address TEXT
    )
    ''')

    conn.commit()
    conn.close()

create_table()


# Home page
@app.route('/')
def home():
    return render_template('home.html')


# About page
@app.route('/about')
def about():
    return render_template('about.html')


# Register page
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        roll_number = request.form['roll_number']
        department = request.form['department']
        year = request.form['year']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        address = request.form['address']

        conn = sqlite3.connect('student.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO students
        (name, roll_number, department, year, email, phone, gender, address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, roll_number, department, year, email, phone, gender, address))

        conn.commit()
        conn.close()

        return redirect('/students')

    return render_template('register.html')


# Students page
@app.route('/students')
def students():

    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    student_data = cursor.fetchall()

    conn.close()

    return render_template('students.html', students=student_data)


if __name__ == '__main__':
    app.run(debug=True)