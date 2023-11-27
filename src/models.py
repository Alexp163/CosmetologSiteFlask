from db import db
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Float
from sqlalchemy.orm import Relationship
from sqlalchemy.sql import func

# id - число
# name_service - наименование услуги
# medical_indications - показания для назначения услуги
# contraindications - противопоказания для выполнения услуги
# medication - препараты для выполнения услуги
# price - стоимость
# feedback_doctors - обратная связь с доктором
# _____________________________________________________
# db.Strings(50) - текстовое поле заданной длины
# db.Integer() - числовое поле
# db.Column() - создание колонки (дополнительные поля: nullable - не может быть
# db.Text() - текстовое поле неограниченной длины
# пустой, unique - уникальна, primary_key) для id всегда primary_key=True


class CosmetologyService(db.Model):
    __tablename__ = "cosmetology_service"

    id = Column(Integer(), primary_key=True) # идентификационный номер
    chapter = Column(String(20)) # раздел
    name_service = Column(Text()) # наименование услуги косметолога

    medical_indications = Column(Text()) # показания для применения услуги
    contraindications = Column(Text()) # противопоказания

    medication = Column(Text()) # препараты для выполнения
    price = Column(Float()) # цена продукта

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Раздел: {self.chapter}, наименование услуги: {self.name_service}, "
                f"показания для применения: {self.medical_indications}, "
                f"противопоказания: {self.contraindications}, препараты выбора: {self.medication} "
                f", цена услуги: {self.price}>")


class Service(db.Model):
    __tablename__ = "service"

    id = Column(Integer(), primary_key=True)

    name_service = Column(String(100))  # наименование услуги
    description = Column(Text())  # описание услуги
    executor = Column(String(50))  # исполнитель
    price = Column(Float())  # цена

    service_group_id = Column(ForeignKey("service_group.id"))  # id группы, к которой относится эта услуга
    service_group = Relationship("ServiceGroup")  # ссылка на группу(id которой указан в вышестоящей строчке)

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Наименование услуги: {self.name_service}, описание услуги: {self.description},"
                f" исполнитель: {self.executor}, цена услуги: {self.price}>")


class ServiceGroup(db.Model):
    __tablename__ = "service_group"
    id = Column(Integer(), primary_key=True)

    name = Column(String(100))
    description = Column(Text())
    # создать руководителя группы

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return f"<Название группы: {self.name}, описание группы: {self.description}>"
