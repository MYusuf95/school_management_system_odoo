from odoo import models, fields, api
from odoo.fields import Date 
import time ,datetime






class School_Students(models.Model):
    _name = 'school_management.students'

    field_study = fields.Char(string="Field")
    name = fields.Char('Sequence', readonly=True)
    student_name = fields.Char()  														# Students can have same name 
    address = fields.Char()														# thanks no change needed
    roll_no = fields.Char()														# must be unique it will be auto generated
    year = fields.Date(string="Admision date",default=fields.Date.context_today)# year also needs to be calculate use strip and date time now to get current year
    year_roll= fields.Char()
    date_of_birth = fields.Date()												# age needs to be calculated ALSO check at that the age is as it should be
    semester = fields.Integer()   					# will also be computed when student passes
    subjects = fields.Char()						# wil be a model							
    			# These are the field for parents									
    partner_id = fields.Many2one("res.partner" ,string="Parent")	    
    parent_company_street = fields.Char(related='partner_id.street' ,string="Street No" , readonly="True")
    parent_phone = fields.Char(related='partner_id.phone' ,string="Phone Number", readonly="True")
    parent_email = fields.Char(related='partner_id.email' ,string="Email", readonly="True")
    state = fields.Selection([('student', 'Student'), ('left', 'Left'), ('passed', 'Passed'), ('expeled', 'Expeled'), ('suspended', 'Suspended')],default="student") 													 # this is an important field which will tell if the student (left,passed out or currently a student keep this field in the last )
    
    # @api.multi
    # def _year(self):
    #     self.year_roll=time.strftime('%Y')
    #     print("Why no in    dff sdf sd",self.year_roll)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('roll.no') or '/'
        return super(School_Students, self).create(vals)