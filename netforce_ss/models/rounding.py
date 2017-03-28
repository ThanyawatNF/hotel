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


class Rd(Model):
    _name = "round"
    _string = "Rounding"
    _name_field="d"
    #_name_field="t"
    _fields = {
        "round_id": fields.Char("Round ID"),
        "day": fields.DateTime("Date", required=True, search=True),
        #"t": fields.Datetime.Tsime("Time", required=True),
        "d": fields.Char("Date"),
    }
    def senddata(self,context={}):
        res = {}
        res = context.get('data') or None
        day = res["day"]
        #import pdb; pdb.set_trace()
        #day = day.split("-")
        res["d"] = day
        return res

Rd.register()
