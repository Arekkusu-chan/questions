from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods = ['POST'])
def signup():
    user = request.form['user_name']
    print("The email address is '" + user + "'")
    return render_template('question_page.html')