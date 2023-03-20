from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"
    student_continuous_ids = fields.One2many(
        string="partner",
        inverse_name="partner",
        comodel_name="students.studentcontinuous",
        required=True,
    )
