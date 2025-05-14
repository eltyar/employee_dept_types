# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Department(models.Model):
    _inherit = 'hr.department'
    
    # تحديث حقل نوع القسم لإضافة نوع 'قطاع'
    department_type = fields.Selection([
        ('section', 'قسم'),
        ('department', 'إدارة'),
        ('sector', 'قطاع')
    ], string='نوع القسم', default='section')
