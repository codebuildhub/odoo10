# -*- coding: utf-8 -*-
{
    'name': "Sale Order History",

    'summary': """
    Sale Order History
   """,

    'description': """
    Sale Order History
    """,

    'author': "Kitsolutions",
    'website': "https://kitsolutions.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales Management',
    'version': '0.1',

    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
