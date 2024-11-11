# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Ensigncode',
    'version': '17.0',
    'description': '''custom module ''',
    'depends': ['base','sale_management', 'mail', 'account','purchase'],
    'data': ['views/sale_order_view.xml',
             'views/report_templates.xml',
             'views/purchase_order_views.xml',
             'data/email_template.xml',
            ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
