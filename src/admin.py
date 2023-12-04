from flask_admin import Admin
from app import app
from flask_admin.contrib.sqla import ModelView
from models import CosmetologyService, Service, ServiceGroup, User
from db import db


admin = Admin(app, __name__, template_mode="bootstrap3")

class CosmetologyServiceModelView(ModelView):
    column_list = ('chapter', 'name_service', 'medical_indications', 'contraindications',
                    'medication', 'price')
    form_excluded_columns = ('created_at', 'updated_at')


class ServiceModelView(ModelView):
    column_list = ('name_service', 'description', 'executor', 'price')
    form_excluded_columns = ('created_at', 'updated_at')


class UserModelView(ModelView):
    column_list = ('nick_name', 'email')
    form_excluded_columns=('created_at', 'updated_at', 'password_hash')


admin.add_view(CosmetologyServiceModelView(CosmetologyService, db.session))
admin.add_view(ServiceModelView(Service, db.session))
admin.add_view(ModelView(ServiceGroup, db.session))
admin.add_view(UserModelView(User, db.session))

