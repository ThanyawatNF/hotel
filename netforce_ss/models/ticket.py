# Copyright (c) 2012-2015 Netforce Co. Ltd.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

from netforce.model import Model, fields, get_model
#from netforce.access import get_active_company
#from netforce import utils


class Ticket(Model):
    _name = "ticket"
    _string = "Ticket"
    _name_field = "from_id"
    _fields = {
        "fname": fields.Char("Name", required=True, search=True),
        "coding": fields.Char("Code"),
        "tell": fields.Char("Phone", required=True, search=True),
        "email": fields.Char("Email"),
        "from_id": fields.Many2One("province","From", required=True),
        "to_id": fields.Many2One("province","To", required=True),
        "time_id": fields.Many2One("round","Round", required=True),
        "seat_id": fields.Many2One("seat","Seat", required=True, search=True),
        "price": fields.Char("Price", required=True),
        "lines": fields.One2Many("ticklines", "tick_id", "Lines"),
    }
    def carr(self,context={}):
        carr={}
        carr = context["data"]

        sourcing = context["data"]["from_id"]
        if sourcing:
            ta = get_model("car").browse(sourcing)
            tabl = ta.source

        dest = context["data"]["to_id"]
        if dest:
            destinat = get_model("car").browse(dest)
            desti = destinat.destination

        carr["ca"] = tabl + desti

        return carr

    def pricing(self,context={}):
        p_id = {}
        #import pdb;pdb.set_trace()
        #pri = context.get('data') or None
        p_id = context['data']

        price = 0

        from_id = context['data']['from_id']
        to_id = context['data']['to_id']
        if from_id and to_id:
            for t in get_model("car").search_browse([["from_id","=",from_id],["to_id","=",to_id]]):
                price = t.pricing
            #price += t.province_price
    
        p_id["price"] = price
        return p_id

    def copy(self, ids, context):
        obj = self.browse(ids)[0]
        vals = {
            "fname": obj.fname,
            "coding": obj.coding,
            "tell": obj.tell,
            "email": obj.email,
            "from_id": obj.from_id.id,
            "to_id": obj.to_id.id,
            "time_id": obj.time_id.id,
            "seat_id": obj.seat_id.id,
            "price": obj.price,
            "lines": [],
        }
        new_id = self.create(vals)
        new_obj = self.browse(new_id)
        return {
            "next": {
                "name": "ticket",
                "mode": "form",
                "active_id": new_id,
            },
            "flash": "oi;erg;oirjgori",
        }
Ticket.register()
