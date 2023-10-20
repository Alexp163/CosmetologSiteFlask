from db import db

# id - число
# name_service - наименование услуги
# medical_indications - показания для назначения услуги
# contraindications - противопоказания для выполнения услуги
# medication - препараты для выполнения услуги
# price - стоимость feedback_doctors - обратная связь с доктором
# _____________________________________________________
# db.Strings(50) - текстовое поле заданной длины
# db.Integer() - числовое поле
# db.Column() - создание колонки (дополнительные поля: nullable - не может быть
# пустой, unique - уникальна, primary_key) для id всегда primary_key=True


class CosmetologyService:
    __tablename__ = "cosmetology_service"

    id = db.Column(db.Integer(), primary_key=True) # идентификационный номер
    name_service = db.Column(db.Strings()) # наименование услуги косметолога

    medical_indications = db.Column(db.String()) # показания для применения услуги
    contraindications = db.Column(db.String()) # противопоказания

    medication = db.Column(db.String()) # препараты для выполнения
    price = db.Column(db.String()) # цена продукта
