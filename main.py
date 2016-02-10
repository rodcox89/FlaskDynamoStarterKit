import os
import uuid
from flask import Flask, jsonify, request
import json
from datetime import date
from marshmallow import Schema, fields, pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr
from config import AWS_REGION, DEFAULT_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, APP_DEFAULT_REGION, DYNAMO_TABLES
from flask.ext.dynamo import Dynamo
from flask.ext.cors import CORS
from flask.ext import restful

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = restful.Api()
api.init_app(app)


os.environ['AWS_REGION'] = AWS_REGION
os.environ['DEFAULT_REGION'] = DEFAULT_REGION
os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY
app.config['DEFAULT_REGION'] = APP_DEFAULT_REGION
app.config['DYNAMO_TABLES'] = DYNAMO_TABLES
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')


@app.route('/', methods=['POST'])
def post():
    # access the json data
    data = request.json
    # specify the table that you want to access
    table = dynamodb.Table('rodneystesttable')
    # generate an id
    id = str(uuid.uuid4())
    # add the item to the table
    table.put_item(
        Item={
            'id': id,
            'unique_key': str(uuid.uuid4()),
            'artist': data['artist'],
            'song': data['song'],
            'year': data['year']
        }
    )
    return id

@app.route('/<query_key>', methods=['Get'])
def get(query_key):
    # specify the table you want to access
    table = dynamodb.Table('rodneystesttable')
    # qquery table
    response = table.query(
        KeyConditionExpression=Key('id').eq(query_key)
    )
    # album will be the literal object
    album = response['Items']
    return jsonify(album = album)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
