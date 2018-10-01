from odoo import models, fields, api
from odoo.fields import Date 
import time ,datetime



class School_Attendance(models.Model):
    _name = 'school_management.attendance'


    student_id = fields.Many2one("school_management.students" ,string="Student",readonly=True)	

    attendance = fields.Boolean(string="present" , default=False) #this will be related to timetable classes