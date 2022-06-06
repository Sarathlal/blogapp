from flask import Blueprint
from flask_restful import Api

# blog_blueprint = Blueprint('job', __name__, url_prefix='/job')
blog_blueprint = Blueprint('blog', __name__)
api = Api(blog_blueprint)

from . import routes