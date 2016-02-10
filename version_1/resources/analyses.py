from flask import jsonify
from flask_restful import Resource
from config import dynamodb
import json


class Analyses(Resource):
    def get(self):
        table = dynamodb.Table('poc-export-analyses-test-000001')
        response = table.scan()
        analyses = response['Items']
        for i in analyses:
            for x in i.keys():
                i[x] = str(i[x])
        analyses = [analysis for analysis in analyses]
        print('returning')
        return jsonify(analyses=analyses)
    def post(self):
        pass
