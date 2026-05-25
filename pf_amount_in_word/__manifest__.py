{
    'name': "Amount In Word",
    'version': '15.0.1.0.0',
    'category': 'Sales/Sales',
    'sequence': 10,
    'summary': "Amount In Word",
    'license': 'OPL-1',
    'description': """
      The Amount In Words module is designed to automatically convert numeric values into words across various business documents in Odoo. It provides support for Sales Orders, Quotations, Purchase Orders, RFQs, and Invoices, ensuring that the total amount is clearly represented in both numeric and textual formats.

By displaying the amount in words, the module helps eliminate confusion and reduces the chances of errors in financial communication. This feature is particularly useful in official documents where the written format of the amount is required for verification, approval, or legal purposes.

The functionality is seamlessly integrated into both form views and report views, allowing users to easily view the amount in words while creating, reviewing, or printing documents. It ensures consistency across all documents and improves overall readability.

This module is easy to use, requires minimal configuration, and integrates smoothly with standard Odoo applications like Sales, Purchase, and Accounting. It enhances the professionalism of business documents and supports better communication across organizational processes.
     """,
    'author': "Prefortune Technologies LLP",
    'website': "https://www.prefortune.com/",
    'maintainer': 'Prefortune Technologies LLP',
    "support": "odoo@prefortune.com",
    'currency': 'EUR',
	'price': '0.00',
    'depends': ['sale', 'purchase', 'account'],
    'data': [
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/account_move_views.xml',
        'reports/sale_report_templates.xml',
        'reports/purchase_report_templates.xml',
        'reports/account_move_report_templates.xml',
    ],
    'images': ["static/description/banner.png"],
    'installable': True,
    'application': False,
    'auto_install': False,
}
