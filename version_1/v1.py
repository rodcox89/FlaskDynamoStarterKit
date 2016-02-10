from flask import Blueprint, render_template, abort, jsonify
from flask.ext import restful
from jinja2 import TemplateNotFound
from version_1.resources.toes import Toe, Toes
from config import dynamodb

print('dynamodb')
print(dynamodb)

v1 = Blueprint('v1', __name__)


api = restful.Api()

api.init_app(v1)
print(Foo)

@v1.route('/')
def show():
    try:
        return 'hello'
    except TemplateNotFound:
        abort(404)


api.add_resource(Foo, '/foo')
api.add_resource(Analyses, '/analyses')
api.add_resource(Toe, '/toe')
# api.add_resorce(Toes, '/toes')
