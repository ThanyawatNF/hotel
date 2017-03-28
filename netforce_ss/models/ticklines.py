from netforce.model import Model, fields

class Prolines(Model):
    _name = "ticklines"
    _name_field = "tick_frome"
    _fields = {
        "tick_id": fields.Many2One("ticket", "id"),
        "tick_from": fields.Many2One("province", "From", required=True),
        "tick_to": fields.Many2One("province", "To", required=True),
        "tick_time": fields.Many2One("round", "Round", required=True),
        "tick_seat": fields.Many2One("seat", "Seat", required=True),
        "tick_price": fields.Many2One("ticket", "Price", required=True),
   }




Prolines.register()
