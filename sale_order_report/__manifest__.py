
{
    'name': 'sale order report',
    'version': '2',
    'category': 'Reporting',
    'summary': 'Sale Reports',
    'depends': [
        'base',
        'sale',
        'stock',
    ],
    'data': [
        'view/view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
