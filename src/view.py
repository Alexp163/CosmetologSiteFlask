from app import app
from flask import render_template
from db_run import CosmetologyService, ServiceGroup, Service


@app.route('/')
def index():
    service_groups = ServiceGroup.query.all()
    return render_template('index.html', service_groups=service_groups)


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


@app.route('/procedur/<int:cosmetology_service_id>')
def one_procedur(cosmetology_service_id):
    cosmetology_service = CosmetologyService.query.get(cosmetology_service_id)
    return render_template('one_procedur.html', cosmetology_service=cosmetology_service)


@app.route('/service_group/<int:service_group_id>')
def service_group(service_group_id):
    service_group = ServiceGroup.query.get(service_group_id)
    service_groups = ServiceGroup.query.all()
    service = Service.query.filter_by(service_group_id=service_group_id).all()
    return render_template("service_group.html", service_group=service_group,
                           service=service, service_groups=service_groups)
