from models import CosmetologyService, Service, ServiceGroup
from app import app


with app.app_context():
    cosmetolog = CosmetologyService.query.all()
    for c in cosmetolog:
        print(c)


with app.app_context():
    services = Service.query.all()
    for s in services:
        print(s)


with app.app_context():
    service_groups = ServiceGroup.query.all()
    for sg in service_groups:
        print(sg)


with app.app_context():
    servises = Service.query.filter_by(service_group_id=1).all()
    for s in servises:
        print(f"id=1 {s}")

with app.app_context():
    servises = Service.query.filter_by(service_group_id=2).all()
    for s in servises:
        print(f"id=2 {s}")