from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import pymysql

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'your_secret_key'

# Create the uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Database connection
db = pymysql.connect(
    host='localhost',
    user='root',
    password='Atg@105pa',
    database='jobapp'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'portfolio_file' not in request.files:
        flash('No file uploaded', 'error')
        return redirect(request.url)

    file = request.files['portfolio_file']

    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    name = request.form['name']
    email = request.form['email']
    position = request.form['position']
    experience = request.form['experience']

    if not name or not email or not position or not experience:
        flash('Please fill in all the required fields', 'error')
        return redirect(request.url)

    # Insert data into the database
    insert_data(name, email, position, experience, filename)

    flash('Application submitted successfully!', 'success')
    return redirect(url_for('home'))

def insert_data(name, email, position, experience, portfolio_file):
    cursor = db.cursor()
    sql = "INSERT INTO job_applications (name, email, position, experience, portfolio_file) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, position, experience, portfolio_file)
    try:
        cursor.execute(sql, values)
        db.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        db.rollback()
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)