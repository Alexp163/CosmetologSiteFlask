from app import app
from db import db
from models import CosmetologyService

with app.app_context():
    db.drop_all()
    db.create_all()


with app.app_context():
    cosmetolog = CosmetologyService(chapter="Инъекционная косметология", name_service="биоревитализация",
    medical_indications="сухая кожа", contraindications="беременность",
    medication="belotero hydro", price ="10000.00")
    db.session.add(cosmetolog)
    cosmetolog1 = CosmetologyService(chapter="Инъекционная косметология", name_service = "мезотерапия",
    medical_indications = "облысение", contraindications = "беременность",
    medication = "Hair plus", price = "15000.00")
    db.session.add(cosmetolog1)
    db.session.commit()

with app.app_context():
    cosmetolog = CosmetologyService.query.all()
    for c in cosmetolog:
        print(c.name_service, c.price)