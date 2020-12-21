from odoo import models, fields, api,tools, _
import base64

class profile_picture(models.Model):
    _name = "profile.picture"

    code = fields.Char("Code")
    date = fields.Date("Date", required=True,default=fields.Date.today())
    photo = fields.Binary("Photo", attachment=True)
    child_id = fields.Many2one("custom.child",store=True)
    remark = fields.Text("Remarks")
    select_profile = fields.Boolean("Select for profile",readonly=False)

    # @api.onchange("child_id")
    # def getPhoto(self):
    #     product_images = self.env["profile.picture"].search([('child_id', '=', self.child_id)])
    #     for rec in product_images:
    #         with open("imageToSave.jpg", "wb") as imgFile:
    #             imgFile.write(base64.b64decode(rec.photo))

    #
    # @api.onchange("select_profile")
    # def _get_profile(self):
    #     if(self.code != False):
    #         photo_object = self.env["profile.picture"].search([('code', '=', self.code)])
    #
    #         child = self.env["custom.child"].browse(photo_object.id).search([("photos",'=',photo_object.id)])
    #         if(child):
    #             allPhotos = self.env["profile.picture"].search([('child_id', '=', child.id)])
    #             if(allPhotos):
    #                 for photo in allPhotos:
    #                     if(photo.code != self.code):
    #                         photo.write({"select_profile":False})
                        # elif(photo.code == self.code):
                        #     if(self.select_profile == True):
                        #         photo.write({"select_profile": True})
                                # child.write({"image": photo_object.photo})


                            # @api.onchange("select_profile")
    # def selectProfile(self, cr, uid, child_id, context=None):
    #        print("child",child_id)
    #     # for photo in self:
    #     #     child = photo.child_id.id
    #     #     print("Child Id---", child)
    #     #     if(photo.select_profile ==  True):
    #     #         selectPhoto = self.env["profile.picture"].search(
    #     #             [("child_id", '=', child), ("select_profile", "=", True)])
    #     #         if (selectPhoto):
    #     #             selectPhoto.write({"select_profile": False})

        # child = self.id
        # print("child_id",self.child_id)
        # if(self.child_id.id == True):
        #     child_id = self.child_id.id
        #     selectPhoto = self.env["profile.picture"].search(
        #         [("child_id", '=', child_id), ("select_profile", "=", True)])
        #     if (selectPhoto):
        #         selectPhoto.write({"select_profile": False})

    # @api.model
    # def create(self, vals):
    #     child_id = vals.get("child_id")
    #     photo = vals.get("photo")
    #     # report = self.env["charity.menu"].search([("child_id", '=', child_id)])
    #     # if (report):
    #     #     report.write({"profile": photo})
    #     # tools.image_resize_images(vals)
    #
    #     if(vals["select_profile"] == True):
    #         selectPhoto = self.env["profile.picture"].search([("child_id",'=',child_id),("select_profile","=",True)])
    #         if(selectPhoto):
    #             selectPhoto.write({"select_profile": selectPhoto})
    #         res = super(profile_picture, self).create(vals)
    #         photo = vals.get("photo")
    #         child = self.env["custom.child"].search([("id", '=', child_id)])
    #         child.write({"image": photo})
    #     else:
    #         res = super(profile_picture, self).create(vals)
    #     return res
    #

    # def write(self, vals):
    #
    #     if (vals.get("select_profile") == True):
    #         self.child_id.write({"image": False})
    #         selectphotos = self.env["profile.picture"].search([("child_id", '=', self.child_id.id), ("select_profile", "=", True)])
    #         if(selectphotos):
    #             for photo in selectphotos:
    #                 if(photo.id != self.id):
    #                     vals["select_profile"] = False
    #                     response = super(profile_picture, photo).write(vals)
    #                     vals["select_profile"] = True
    #
    #
    #         response = super(profile_picture, self).write(vals)
    #
    #         self.child_id.write({"image":self.photo})
    #     elif(vals.get("select_profile") == False):
    #         response = super(profile_picture, self).write(vals)
    #     else:
    #         photo = vals.get("select_profile")
    #         vals['select_profile'] = False
    #         response = super(profile_picture, photo).write(vals)

            # return super(childTemplate, self.with_context(ctx)).write(values)

            # self.env["custom.child"].search([("id",'=',self.child_id.id)])

    #
    # @api.multi
    # def write(self, vals):
    #      child_id = self.child_id.id
    #      remark = self.remark
    #      profile = vals["select_profile"]
    #      if(profile == True):
    #          updateValue = True
    #          selectPhoto = self.env["profile.picture"].search([("child_id", '=', child_id),("select_profile","=",True)])
    #          if (selectPhoto):
    #             vals["select_profile"]=False
    #             # selectPhoto.write({"select_profile": False})
    #          else:
    #              res = super(profile_picture, self).create(vals)
    #              return res
    #              # selectPhoto = self.env["profile.picture"].search([("id", '=', self.id)])
    #              # selectPhoto.write({"select_profile":True})
    #
    #
    #             # res = super(profile_picture, self).create(vals)
    #             # return res
    #      else:
    #          self.write({"select_profile": False})



