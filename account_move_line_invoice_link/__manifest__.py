# -*- coding: utf-8 -*-
{
    'name': 'Apuntes contables con factura relacionada',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Muestra la factura relacionada en apuntes contables de pagos',
    'description': """
Muestra en cada apunte contable de diario tipo banco y cuenta 208.01.01 las facturas relacionadas.
    """,
    'author': 'Tu Nombre o Empresa',
    'depends': ['account'],
    'data': [
        'data/account_move_line_server_action.xml',
        'views/account_move_line_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
