from odoo import models, fields, api
from odoo.fields import Date 
import time ,datetime

class School_Assignment(models.Model):
    _name = 'school_management.assignment'

    name = fields.Char(default="null")
    total_marks = fields.Float()
    scored_marks = fields.Float()
    # questions = fields.Many2one("school_management.questions")
    deadline = fields.Date()
    description = fields.Text()
    hints = fields.Text()
    state = fields.Selection([('accepted','Accepted'),('regected','Regected'),('pending','Pending')],default="pending")
