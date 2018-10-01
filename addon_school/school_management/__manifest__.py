# -*- coding: utf-8 -*-
{
    'name': "school_management",

    'summary': """
        This is a detailed model that handle the processes requred in a school & help in the management of these process """,

    'description': """
        For Schools and Tution Centers, 
        Helps in following areas
        -Admissions
        -Fees management 
        -Progress report of teacher,students and school
    """,

    'author': "Comstar",
    'website': "http://www.comstar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/School_Student.xml',
        'views/School_Teachers.xml',
        'views/School_Academics.xml',
        'views/School_Assignment.xml',
        'views/School_Attendance.xml',
        'views/School_Sequences.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}