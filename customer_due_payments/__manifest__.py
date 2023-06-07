# -*- coding: utf-8 -*-
{
    'name': "Customer Due payment Sale order",

    'summary': """
Customer Due payment Sale order   """,

    'description': """
Customer Due payment Sale order    """,

    'author': "Kitsolutions",
    'website': "https://kitsolutions.org",
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
