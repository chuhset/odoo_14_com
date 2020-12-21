from odoo import models, fields, api, _
import base64
from odoo.exceptions import ValidationError,AccessError,Warning,RedirectWarning,MissingError

class sponsorshipTypeTemplate(models.Model):
    _name = "sponsorship.type"
    _rec_name = "type"

    type = fields.Char("Type")


    def unlink(self):
        for type in self:
            if(type.type):
                sponsorship = self.env["sponsorship"].search([("type",'=',self.type)])
                if(sponsorship):
                    raise ValidationError("You cannot delete this type because you have relation with sponsorship.")
        return super(sponsorshipTypeTemplate, self).unlink()