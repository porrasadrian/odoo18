# -*- coding: utf-8 -*-
{
    'name': "Tool Maintenance Management",
    'summary': "module to manage work tools assigned to employees, with their usage and maintenance history.",
    'description': """
    module to manage work tools assigned to employees, with their usage and maintenance history.
    """,
    'author': "Adrian Porras",
    'website': "https://www.youtube.com/@odoosystem",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base','hr','stock'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/tool_equipment_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

