from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from db import db
from forms import LoginForm, RegisterForm
from models import CosmetologyService, ServiceGroup, Service, User


@app.route('/')
def index():
    service_groups = ServiceGroup.query.all()
    return render_template('index.html', service_groups=service_groups)


@app.route('/our_service')
@login_required
def our_service():
    cosmetolog = CosmetologyService.query.all()
    return render_template('our_service.html', cosmetolog=cosmetolog)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Кнопка нажата!!!")
        flash("Кнопка нажата")
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Авторизация успешна!")
        else:
            flash("Не верный логин или пароль!!!")
    return render_template('login.html', form=form)


@app.route('/registration', methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if request.method=='POST' and form.validate():
        print("Кнопка нажата!!!")
        flash("Кнопка нажата")
        email = form.email.data
        pass_1 = form.password_1.data
        pass_2 = form.password_2.data
        if pass_1 == pass_2:
            if len(User.query.filter_by(email=email).all())==0:
                user = User(email=email, password_hash=generate_password_hash(pass_1))
                db.session.add(user)
                db.session.commit()
                flash("Регистрация прошла успешно!!!")
            else:
                flash("Вы уже проходили регистрацию!")
        else:
            flash("Пароли не совпадают!")
    return render_template('registration.html', form=form)


@app.route('/procedur/<int:cosmetology_service_id>')
@login_required
def one_procedur(cosmetology_service_id):
    cosmetology_service = CosmetologyService.query.get(cosmetology_service_id)
    return render_template('one_procedur.html', cosmetology_service=cosmetology_service)


@app.route('/service_group/<int:service_group_id>')
@login_required
def service_group(service_group_id):
    service_group = ServiceGroup.query.get(service_group_id)
    service_groups = ServiceGroup.query.all()
    service = Service.query.filter_by(service_group_id=service_group_id).all()
    return render_template("service_group.html", service_group=service_group,
                           service=service, service_groups=service_groups)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.errorhandler(401)
def custom_401(error):
    return render_template('error401.html')


@app.errorhandler(404)
def custom_404(error):
    return render_template('error404.html')


@app.errorhandler(500)
def custom_500(error):
    return render_template('error500.html')
