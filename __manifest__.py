# -*- coding: utf-8 -*-
{
    'name': 'Employee Department Types',
    'version': '1.0',
    'summary': 'تعزيز وظائف قسم الموارد البشرية',
    'description': '''
        إضافة نوع جديد للأقسام (قطاع) وحقول إضافية للعرض في نموذج الموظف
    ''',
    'category': 'Human Resources',
    'author': 'Admin',
    'depends': ['hr'],
    'data': [
        'views/hr_department_views.xml',
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}