from odoo import models, fields, api, _

class menu(models.Model):
    _name = "charity.menu"

    sponsor_id = fields.Many2one("sponsor",string="Sponsor",required=True)
    child_id = fields.Many2one("custom.child", string="Child",required=True)
    profile = fields.Binary()
    progress = fields.Text()
    amount = fields.Char("Monthly amount")
    started_date = fields.Date("Start Date")
    dateofbirth = fields.Date("Birth Date")