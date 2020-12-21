from odoo import models, fields, api, _
from datetime import datetime

class childTemplate(models.Model):
    _name = "custom.child"
    _rec_name = "name"
    # _inherits = {'res.partner': 'partner_id'}

    name = fields.Char("Name", required=True)
    image = fields.Binary(string="Photo",readonly=False)
    dob = fields.Date("Date of Birth", required=False)
    # age = fields.Integer("Age",compute="_compute_age",store=True)
    photos = fields.One2many("profile.picture","child_id","Photos")
    state = fields.Selection([('draft','Draft'),('attending_school', 'Attending School'), ('droppedOut', 'Dropped Out'), ('disqualified', 'Disqualified'),('finished','Finished')], default='draft')
    progress_info = fields.Text("Progress")
    active = fields.Boolean("Active", default="True")

    # @api.depends('dob')
    # def _compute_age(self):
    #     if(self.dob != False):
    #         date1 = datetime.strptime(self.dob, '%Y-%m-%d')
    #         dobyear = date1.year
    #         now = datetime.today()
    #         current_year = now.year
    #         self.age = current_year - dobyear


    # @api.onchange("photos")
    # def get_photo(self):

    # @api.depends('photos')
    # def get_profile(self):
    #     if(self.image != False):
    #         print("self--",self)
    # @api.model
    # def create(self, vals):
    #     photos = vals.get("photos")
    #     child = super(childTemplate, self).create(vals)
    #     selectPhoto = self.env["profile.picture"].search([("child_id", '=', child.id), ("select_profile", "=", True)])
    #     if(selectPhoto):
    #         child.write({"image" :True})
    #     return child
    #
    # @api.onchange("photos")
    # def get_profile(self):
    #     if(self.photos != False):
    #         for photo in self.photos:
    #             if(photo.select_profile == True):
    #                 self.image = photo.photo

                # else:
                #     self.image = False
                    # self.write({"image":photo.photo})
        # selectPhoto = self.env["profile.picture"].search([("child_id", '=', self.id), ("select_profile", "=", True)])

    def get_child_report_name(self):

        lang = self._context.get("lang")

        if lang:

            record_lang = self.env['res.lang'].search([("code", "=", lang)], limit=1)

        date_format = record_lang.date_format or '%d/%m/%Y'
        string_date_format = date_format.encode('utf-8')

        today_date_string = fields.date.today().strftime(string_date_format)
        child_name = self.name
        report_name = child_name+"-"+today_date_string+".pdf"
        encoded_name = report_name.encode('utf-8')
        return encoded_name


    def write(self, vals):
        # print("image", vals.get("image"))

        res = super(childTemplate, self).write(vals)
        return res


    def attend_school(self):
        self.write({"state": "attending_school"})

    def dropout(self):
        self.write({"state": "droppedOut"})


    def disqualified(self):
        self.write({"state": "disqualified"})


    def finished(self):
        self.write({"state": "finished"})
#
# class childProfile(models.Model):
#     _name = 'child.profile'
#
#     child_id = fields.Many2one("custom.child")
#     photo_id = fields.Many2one("profile.picture")
    # date = fields.Date("Date", required=True, default=fields.Date.today())
    # remark = fields.Text("Remarks")
    # select_profile = fields.Boolean(readonly=False)


    # @api.depends("photos")
    # def _get_picture(self):
    #     self.env["profile.picture"].search([("child_id","=",)])

