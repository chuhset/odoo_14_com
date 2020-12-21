from odoo import api, fields, models, tools
class progressTemplate (models.Model):

    _name = "custom.progress"
    _order = 'date asc'

    child_id = fields.Many2one("custom.child",readonly=True)
    progress_info = fields.Text("Notes")
    date = fields.Date("Date",default=fields.Date.today())

    # @api.onchange("child_id")
    # def defineChild_id(self):
    #     context = self.env.context
    #     child = context['child_id']
    #     self.child_id = child
    #     print("Child id--", child)

    # @api.model
    # def create(self, vals):
    #     child_id = vals.get("child_id")
    #     # progress = vals.get("progress_info")
    #     # progessList = self.env["custom.progress"].search([("child_id", '=', child_id)])
    #     # text = ''
    #     # for pro in progessList:
    #     #     text += pro.progress_info+"\n\n"
    #     # text += progress
    #     # report = self.env["charity.menu"].search([("child_id",'=',child_id)])
    #     # if(report):
    #     #     report.write({"progress":text})
    #     if(child_id == None):
    #         context = self.env.context
    #         child = context['child_id']
    #         state = context['state']
    #         # self.child_id = child
    #         vals['child_id'] = child
    #         child = self.env["custom.child"].search([("id","=",child)])
    #         child.state = state
    #         child.write({"state": state})
    #     res = super(progressTemplate, self).create(vals)
    #     child.write({"progress": [[1, self.id,{'progress':self}]]})
    #     return res