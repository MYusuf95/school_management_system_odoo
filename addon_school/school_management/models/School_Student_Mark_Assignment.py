# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student_Subject_Assigning(models.TransientModel):
    _name = 'school_management.as_w'

    def _default_sessions(self):
        return self.env['school_management.assignment'].browse(self._context.get('active_ids'))
   
    assignment_ids = fields.Many2many('school_management.assignment', string="Time Table", required=True, default=_default_sessions)
    student_ids = fields.Many2many('school_management.students',string="Students")
   
    @api.multi
    def assign(self):
        for session in self.assignment_ids:
            print(session)
            session.student_ids |= self.student_ids
        return {}