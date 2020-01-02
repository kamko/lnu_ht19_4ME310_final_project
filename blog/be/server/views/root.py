from flask import Blueprint

blueprint = Blueprint('root', __name__)


@blueprint.route('/')
def root():
    return '4M310-final-project-blog-be'
