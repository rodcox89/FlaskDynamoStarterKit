import boto3
from boto3.dynamodb.conditions import Key, Attr
import boto.dynamodb2
from boto.dynamodb2.fields import HashKey,RangeKey, GlobalAllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.items import Item
from boto.dynamodb2.results import ResultSet
import boto.sqs
from boto.sqs.message import Message
from boto import connect_dynamodb
from secrets import secret_key, access_id


dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

AWS_REGION = 'us-west-2'
DEFAULT_REGION = 'us-west-2'
AWS_ACCESS_KEY_ID = secret_key
AWS_SECRET_ACCESS_KEY = access_id
APP_DEFAULT_REGION = connect_dynamodb('us-west-2')
DYNAMO_TABLES = [
Table('poc-export-entities-test-000001', schema=[HashKey('entity_id')], connection=boto.dynamodb2.connect_to_region('us-west-2')),
Table('mvp-findings-test-000001', schema=[HashKey('analysis_id')], connection=boto.dynamodb2.connect_to_region('us-west-2')),
Table('findings-staging', schema=[HashKey('analysis_id')], connection=boto.dynamodb2.connect_to_region('us-west-2')),
Table('staging-export-netblocks', schema=[HashKey('analysis_id')], connection=boto.dynamodb2.connect_to_region('us-west-2')),
Table('toes', schema=[HashKey('toe_id')], connection=boto.dynamodb2.connect_to_region('us-west-2')),
]

ToeTable = dynamodb.Table('toe')
