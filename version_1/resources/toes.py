from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields
from config import dynamodb, ToeTable
from collections import OrderedDict
from pprint import pprint
import datetime
import json
import uuid


from schema import ToeSchema
import objects




class Toe(Resource):
    def post(self):
        table = ToeTable
        data = request.json
        print(data['seed_hostnames'])
        schema = ToeSchema()
        result = schema.load(data)
        response = schema.dump(result.data)
        data = response.data
        table.put_item(
            Item = {
                'toe_id': data['toe_id'],
                'date_created': data['date_created'],
                'short_name': data[u'short_name'],
                'formal_name': data[u'formal_name'],
                'industry': data[u'industry'],
                'date_created': data[u'date_created'],
                'toe_id': data[u'toe_id'],
                'toe_netblocks': data[u'toe_netblocks'],
                'seed_hostnames': data[u'seed_hostnames']
            }
        )
        return data , 201
    def get(self):
        print('get worked')

        return 'get', 201

class Toes(Resource):
    def get(self):
        table = ToeTable
        print(table)
        response = table.scan()

        return  response, 201


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
