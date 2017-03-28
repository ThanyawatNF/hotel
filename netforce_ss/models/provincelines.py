from netforce.model import Model, fields

class Prolines(Model):
    _name = "provincelines"
    _name_field = "province_place"
    _fields = {
        "province_id": fields.Many2One("province", "id"),
        "province_place": fields.Char("", required=True),
   }




Prolines.register()

