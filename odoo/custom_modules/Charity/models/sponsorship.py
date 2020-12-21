from odoo import models, fields, api, _
import base64
from odoo.exceptions import ValidationError,AccessError,Warning,RedirectWarning,MissingError

class sponsorshipTemplate(models.Model):
    _name = "sponsorship"
    _order = "started_date asc"


    sponsor_id = fields.Many2one("sponsor",required=False)
    child_id = fields.Many2one("custom.child",required=False)
    amount = fields.Char("Amount",required=False)
    started_date = fields.Date("Start Date",required=True,default=fields.Date.today())
    payment_frequency = fields.Selection([('monthly',"Monthly"),('yearly','Yearly'),('irregular','Irregular')])
    payment_method = fields.Selection([('bank','Bank'),('paypal','Paypal'),('cash','Cash')])
    gift_aid = fields.Boolean("Gift Aid")
    active_sponsor = fields.Boolean("Active")
    readonly = fields.Boolean(default=False,compute="checksponsor")
    count = fields.Integer(default=0)
    remarks = fields.Char("Remarks")
    type = fields.Many2many("sponsorship.type",string="Sponsorship Type")



    # @api.model
    # def create(self, vals):
    #     child = vals.get('child_id')
    #     sponsorship = self.env['sponsorship'].search([("child_id",'=',child),('active_sponsor','=',True)])
    #     print("length of spship", len(sponsorship))
    #     if(len(sponsorship)>=1):
    #         warning_message = 'This child has already sponsorship. You need to set the first sponsorship inactive if another person wants to be a sponsorship.'
    #         raise RedirectWarning(warning_message)
    #         view_id = self.env.ref('Charity.sponsorship_tree_template').id
    #
    #         return {
    #             'name': _('sponsorship_tree_template'),
    #             'view_type': 'form','tree'
    #             'view_mode': 'tree,form',
    #             'views': [(view_id, 'tree')],
    #             'res_model': 'sponsorship',
    #             'view_id': False,
    #             'type': 'ir.actions.act_window',
    #         }
    #         # raise AccessError(_(
    #         #     'This child has already sponsorship. You need to set the first sponsorship inactive if another person wants to be a sponsorship.'))
    #     else:
    #         res = super(sponsorshipTemplate,self).create(vals)
    #     return res
    #
    #
    # @api.multi
    # def write(self, vals):
    #     if(vals.get("active_sponsor") == True):
    #         child = self.child_id
    #         sponsorship = self.env['sponsorship'].search([("child_id", '=', child.id), ('active_sponsor', '=', True)])
    #         if (len(sponsorship) >= 1):
    #             warning_message = 'This child has already sponsorship. You need to set the first sponsorship inactive if another person wants to be a sponsorship.'
    #             raise RedirectWarning(warning_message)
    #             view_id = self.env.ref('Charity.sponsorship_tree_template').id
    #
    #             return {
    #                 'name': _('sponsorship_tree_template'),
    #                 'view_type': 'form', 'tree'
    #                 'view_mode': 'tree,form',
    #                 'views': [(view_id, 'tree')],
    #                 'res_model': 'sponsorship',
    #                 'view_id': False,
    #                 'type': 'ir.actions.act_window',
    #             }
    #             # raise AccessError(_(
    #              #     'This child has already sponsorship. You need to set the first sponsorship inactive if another person wants to be a sponsorship.'))
    #         else:
    #             res = super(sponsorshipTemplate, self).write(vals)
    #     else:
    #         res = super(sponsorshipTemplate, self).write(vals)
    #     return res
    #
