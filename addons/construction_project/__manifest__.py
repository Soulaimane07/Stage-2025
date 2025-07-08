{
'name': 'Construction Project Lite',
    'version': '1.0',
    'author': 'Your Name',
    'depends': ['base', 'project', 'hr', 'stock', 'purchase', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/construction_project_views.xml',
    ],
    'installable': True,
    'application': True,
}
