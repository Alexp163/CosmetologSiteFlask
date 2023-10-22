from app import app
from flask import render_template
from db_run import CosmetologyService


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/our_service')
def our_service():
    cosmetolog = CosmetologyService.query.all()
    return render_template('our_service.html', cosmetolog=cosmetolog)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/procedur/1')
def one_procedur():
    return render_template('one_procedur.html')
