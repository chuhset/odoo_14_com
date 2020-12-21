from odoo import api, fields, models, tools

class custom_report_charity(models.Model):
    _name = 'report.charity'
    _auto = False

    child = fields.Char("Child Name")
    # profile_id = fields.Many2one("profile.picture", string="Profile", readonly=True)
    info = fields.Text("Progress Information")
    payment = fields.Char("Monthly Donation Amount")
    sponsor = fields.Char("Sponsor Name")
    image = fields.Binary()

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'report_charity')
        self._cr.execute("""
                CREATE OR REPLACE VIEW report_charity AS (
                    SELECT sp.id AS id, c.name AS child,sp.amount AS payment,
                     s.name AS sponsor, p.progress_info AS info,profile.photo AS image
                    FROM sponsorship sp
                    LEFT JOIN custom_child c ON c.id = sp.child_id
                    LEFT JOIN sponsor s ON s.id = sp.sponsor_id
                    LEFT JOIN custom_progress p ON p.child_id = sp.child_id
                    LEFT JOIN profile_picture profile ON profile.child_id = sp.child_id
                )""")
        charity = self.env["report_charity"].search([('child', '=', self.child)])
        for s in charity:
            self.child = charity.child
            self.sponsor = charity.sponsor
            self.image = charity.image

    @api.onchange("child")
    def getdata(self):
        charity = self.env["report_charity"].search([('child', '=', self.child)])
        for s in charity:
            self.child = charity.child
            self.sponsor = charity.sponsor
            self.image = charity.image

    # @api.one
    # def _getBase64Image(self):
    #
    #     product_images = self.env["profile.picture"].search([('child_id', '=', self.child_id.id)])
    #     self.image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAAC....."