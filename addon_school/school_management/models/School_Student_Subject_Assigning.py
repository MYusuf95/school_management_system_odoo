# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student_Subject_Assigning(models.TransientModel):
    _name = 'school_management.a_w'

    session_id = fields.Many2many('school_management.students',
        string="Students", required=True)
    attendee_ids = fields.Many2many('school_management.time_table', string="Time Table")