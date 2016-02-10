import datetime as dt
from marshmallow import Schema, fields,  post_load
from objects import Toe, ToeNetblock

class ToeNetblockSchema(Schema):
    toe_netblock_id = fields.Str()
    registrant_org = fields.Str()
    country = fields.Str()
    cidr = fields.Str()
    start_ip = fields.Str()
    end_ip = fields.Str()
    class Meta:
        fields = ("toe_netblock_id", "registrant_org", "country", "cidr", "start_ip", "end_ip")
        ordered = True
    @post_load
    def make_toenetblock(self, data):
        return ToeNetblock(**data)

class ToeSchema(Schema):
    short_name = fields.Str()
    formal_name = fields.Str()
    toe_netblocks = fields.Nested(ToeNetblockSchema, many=True)
    toe_id = fields.Str()
    date_created = fields.Str()
    industry= fields.Str()
    seed_hostnames = fields.List(fields.Str())
    class Meta:
        fields = ('toe_id', 'short_name', 'formal_name', 'industry', 'date_created', 'toe_netblocks', 'seed_hostnames' )
        ordered = True
    @post_load
    def make_toe(self, data):
        return Toe(**data)
