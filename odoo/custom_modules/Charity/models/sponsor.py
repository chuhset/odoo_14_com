from odoo import models, fields, api, _

class sponsor(models.Model):
    _name = "sponsor"
    _inherits = {'res.partner': 'partner_id'}

    surname = fields.Char("Surname")
    address = fields.Char("Address")
    email_address_1 = fields.Char("Email Address 1")
    email_address_2 = fields.Char("Email Address 2")
    sponsorships = fields.One2many("sponsorship","sponsor_id","Sponsorship(s)")
