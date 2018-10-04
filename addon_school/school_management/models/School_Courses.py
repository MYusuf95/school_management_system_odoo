from odoo import models, fields, api
from odoo.fields import Date 
import time ,datetime

class School_Courses(models.Model):

    _name = 'school_management.courses'
    time_table_id = fields.One2many("school_management.time_table" , "courses_id")	
   