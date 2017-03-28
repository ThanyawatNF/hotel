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


class Car(Model):
    _name = "car"
    _string = "Car ride"
    _name_field = "from_id"
    #_audit_log = True
    #_export_field = "name"
    #_key = ["code"]
    _fields = {
        "from_id": fields.Many2One("province","From",required=True, search=True),
        "from_place": fields.Many2One("provincelines","From place",required=True, search=True),
    
        "to_id": fields.Many2One("province","To",required=True, search=True),
        "pricing": fields.Decimal("Price",required=True),
        "lines": fields.One2Many("sale.order.line", "order_id", "Lines")
        #"roundd": fields.Many2One("round","Round", required=True),
        #"lines": fields.One2Many("round","d","Round", search=True),
        #"tex": fields.Char("Date"),
}
    def Place (self,context={}):
        p = context['data']
        #import pdb;pdb.set_trace()
        fplace = context['data']["from_id"]
        if fplace :
            for frpl in get_model("provincelines").search_browse([["province_place","=",fplace]]):
                from_place = frpl.province_place
        p ["from_place"] = from_place
        return p

Car.register()
