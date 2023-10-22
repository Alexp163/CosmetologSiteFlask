from db import db

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

    id = db.Column(db.Integer(), primary_key=True) # идентификационный номер
    chapter = db.Column(db.String(20))
    name_service = db.Column(db.Text()) # наименование услуги косметолога

    medical_indications = db.Column(db.Text()) # показания для применения услуги
    contraindications = db.Column(db.Text()) # противопоказания

    medication = db.Column(db.Text()) # препараты для выполнения
    price = db.Column(db.Float()) # цена продукта
