{
    'name': "ACT",
    'version': '1.0',
    'author': "Yoma Technologies",
    'category': 'Sales',
    'website': 'http://www.yomatechnologies.com/',
    'description': """
           The Andrew Clark Trust
        """,
    # 'depends': ['base','web','web_widget_darkroom'],
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'report/custom_layout.xml',
        # 'views/template_css.xml',
        # 'views/sponsor_view.xml',
        'views/child_view.xml',
        # 'views/sponsorship_view.xml',
        # 'views/profile_vew.xml',
        # 'views/progress_info_view.xml',
        # 'views/menu_template.xml',
        'views/custom_report_view.xml',
        'views/report_view.xml',
        # 'views/sponsorship_report_view.xml',
        # 'views/sponsorship_type.xml',
        'views/charity_menu.xml',

    ],
    'installable': True,
    'auto_install': False,
}