from odoo import models, fields, api
from odoo.fields import Date 
import time ,datetime

class School_Teachers(models.Model):
    _name = 'school_management.teachers'
    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()