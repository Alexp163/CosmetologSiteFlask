from app import app
from db import db
from models import CosmetologyService, Service, ServiceGroup

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
    group1 = ServiceGroup(name="Дерматология",
                          description="здесь будет описана группа")
    group2 = ServiceGroup(name="Инъекционная косметология",
                          description="здесь будет описана группа")
    group3 = ServiceGroup(name="Аппаратная косметология",
                          description="здесь будет описана группа")
    group4 = ServiceGroup(name="Пластическая хирургия",
                          description="здесь будет описана группа")
    db.session.add(group1)
    db.session.add(group2)
    db.session.add(group3)
    db.session.add(group4)
    db.session.commit()
    service = Service(name_service="Дерматология",
                      description="консультация врача-дерматолога",
                      executor="врач-дерматолог Петров А.В.", price="2500.00",
                      service_group = group1)
    db.session.add(service)
    service1 = Service(name_service="Инъекционная косметология",
                      description="мезотерапия кожи лица",
                      executor="врач-косметолог Сизова М.Н", price="7500.00",
                      service_group = group2)
    db.session.add(service1)
    service2 = Service(name_service="Аппаратная косметология",
                      description="Лазерная эпиляция",
                      executor="врач-дерматолог Иванова А.В.", price="5500.00",
                      service_group = group3)
    db.session.add(service2)
    service3 = Service(name_service="Пластическая хирургия",
                      description="Круговая подтяжка лица",
                      executor="врач-пластический хирург Забоев В.Л.", price="82500.00",
                      service_group = group4)
    db.session.add(service3)
    db.session.commit()
    
