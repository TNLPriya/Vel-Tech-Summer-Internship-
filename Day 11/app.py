from flask import Flask, render_template

app = Flask(__name__)

# Dummy student data
students = [
    {"name": "Rahul", "course": "B.Tech", "email": "rahul@gmail.com"},
    {"name": "Priya", "course": "BCA", "email": "priya@gmail.com"},
    {"name": "Ravi", "course": "MBA", "email": "ravi@gmail.com"}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/students')
def student_list():
    return render_template('students.html', students=students)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)