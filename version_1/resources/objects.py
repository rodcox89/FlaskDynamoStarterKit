import datetime as dt
import uuid

class Toe(object):
    def __init__(self,short_name, formal_name, toe_netblocks, industry, seed_hostnames):
        self.short_name = str(short_name)
        self.formal_name = str(formal_name)
        self.toe_netblocks = toe_netblocks
        self.industry = str(industry)
        self.date_created = str(dt.datetime.now())
        self.toe_id = str(uuid.uuid4())
        self.seed_hostnames = seed_hostnames
    def __repr__(self):
        return '<Toe(short_name={self.short_name!r})>'.format(self=self)

class ToeNetblock(object):
    def __init__(self, registrant_org, country, cidr, start_ip, end_ip ):
        self.registrant_org = str(registrant_org)
        self.country = str(country)
        self.cidr = str(cidr)
        self.start_ip = str(start_ip)
        self.end_ip = str(end_ip)
