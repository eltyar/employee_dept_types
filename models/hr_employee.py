# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'
    
    # حقل للحصول على القطاع الذي يتبع له الموظف
    sector_id = fields.Many2one('hr.department', string='القطاع', compute='_compute_sector_department', store=True, readonly=True)
    
    # حقل للحصول على الإدارة التي يتبع لها الموظف
    department_management_id = fields.Many2one('hr.department', string='الإدارة', compute='_compute_sector_department', store=True, readonly=True)
    
    @api.depends('department_id')
    def _compute_sector_department(self):
        for employee in self:
            # إعداد القيم الافتراضية
            employee.sector_id = False
            employee.department_management_id = False
            
            # الحصول على القسم الحالي
            current_department = employee.department_id
            if not current_department:
                continue
                
            # البحث عن الإدارة والقطاع
            if current_department.department_type == 'section':
                # إذا كان القسم الحالي هو 'قسم'، نبحث عن الإدارة والقطاع المرتبطين به
                parent_dept = current_department.parent_id
                if parent_dept and parent_dept.department_type == 'department':
                    employee.department_management_id = parent_dept
                    # البحث عن القطاع (إذا كان الإدارة تحت قطاع)
                    if parent_dept.parent_id and parent_dept.parent_id.department_type == 'sector':
                        employee.sector_id = parent_dept.parent_id
            
            elif current_department.department_type == 'department':
                # إذا كان القسم الحالي هو 'إدارة'، نحدد هذا كإدارة ونبحث عن القطاع
                employee.department_management_id = current_department
                if current_department.parent_id and current_department.parent_id.department_type == 'sector':
                    employee.sector_id = current_department.parent_id
            
            elif current_department.department_type == 'sector':
                # إذا كان القسم الحالي هو 'قطاع'، نحدد هذا كقطاع
                employee.sector_id = current_department