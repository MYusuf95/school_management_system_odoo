from odoo import models, fields, api
from odoo.fields import Date 
import time ,datetime

class School_Questions(models.Model):
    _name = 'school_management.questions'

    name = fields.Char(default="null")
    # assignment_id = fields.One2many("school_management.assignment")
