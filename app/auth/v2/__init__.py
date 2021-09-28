from flask import Blueprint
from flask_restful import Api
from .views.user_views import UserRegister

version_2_auth = Blueprint('auth_v2', __name__, url_prefix='/auth/v2')

api = Api(version_2_auth)

api.add_resource(UserRegister, '/signup')