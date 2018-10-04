from odoo import models, fields, api
from odoo.fields import Date 
import time ,datetime

class School_Time_Table(models.Model):

    _name = 'school_management.time_table'
    courses_id = fields.Many2one("school_management.courses")
    student_id = fields.Many2one("school_management.students")	
    attendance = fields.Boolean(string="present",default=True, track_visibility="onchange") 
    classes = fields.Char(string = "Classes") 
    marked_date = fields.Date(string="Marked date",default=fields.Date.context_today) 