# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Date 
import time ,datetime

class School_Management(models.Model):
    _name = 'school_management.school_management'

    name = fields.Char()
    address = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    value = fields.Float()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

