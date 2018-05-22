# -*- coding: utf-8 -*-
{
    'name': "a2-martic20",

    'summary': """
        Tercer intent de mòdul, aquest funcionarà""",

    'description': """
        Mòdul per practicar herència en Odoo
    """,

    'author': "martic20",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['a1'],

    # always loaded
    'data': [
        #'security/todo_access_rules.xml',
        #'security/ir.model.access.csv',
        'views/todo_task.xml'
        #'views/todo_view.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}