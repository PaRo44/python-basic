from flask import Blueprint

users_blueprint = Blueprint('users', __name__)

from users import routes
