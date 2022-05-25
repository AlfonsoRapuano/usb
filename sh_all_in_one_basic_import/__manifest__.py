# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "All In One Basic Import - Partner, Product, Sales, Purchase, Accounts, Inventory",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Extra Tools",
    "summary": "Import Partner From Csv App,Import Product From Excel,Import Sale Order From CSV,Import Purchase Order From Excel,Import Account From Csv,Import Invoice From XLS,Import Account From XLSX,Import Inventory From Csv Module,Import Stock From Excel Odoo",
    "description": """
This module is useful to import data from CSV/Excel file. You can import custom fields from CSV or Excel.

All In One Basic Import - Partner, Product, Sales, Purchase, Account, Inventory Odoo
 Import Partner From Csv, Import Partner From Excel, Import Partner From XLS, Import Partner From XLSX, Import Product From Csv, Import Product From Excel, Import Product From XLS, Import Product From XLSX,  Import Sales From Csv, Import Sale Order From Excel, Import Quotation From XLS, Import so From XLSX, Import Purchase From Csv, Import Purchase Order From Excel, Import Request For Quotation From XLS, Import RFQ From XLSX, Import Account From Csv, Import Invoice From Excel, Import Invoice From XLS, Import Account From XLSX, Import Inventory From Csv, Import Stock From Excel, Import Inventory From XLS, Import Stock From XLSX Odoo.
 Import Partner From Csv App, Import Partner From Excel, Import Partner From XLS, Import Partner From XLSX, Import Product From Csv App, Import Product From Excel, Import Product From XLS Module, Import Product From XLSX,  Import Sales From Csv, Import Sale Order From Excel, Import Quotation From XLS, Import so From XLSX, Import Purchase From Csv Module, Import Purchase Order From Excel, Import Request For Quotation From XLS, Import RFQ From XLSX, Import Account From Csv App, Import Invoice From Excel, Import Invoice From XLS, Import Account From XLSX, Import Inventory From Csv Module, Import Stock From Excel, Import Inventory From XLS, Import Stock From XLSX Odoo""",
    "version": "14.0.7",
    "depends": [
        "sh_message",
            "sale_management",
            "stock",
            "account",
            "purchase",
            "sh_product_multi_barcode",
    ],
    "application": True,
    "data": [
        'sh_import_ail/security/import_ail_security.xml',
        'sh_import_ail/security/ir.model.access.csv',
        'sh_import_ail/wizard/import_ail_wizard.xml',
        'sh_import_ail/views/account_view.xml',

        'sh_import_inv/security/import_inv_security.xml',
        'sh_import_inv/security/ir.model.access.csv',
        'sh_import_inv/wizard/import_inv_wizard.xml',
        'sh_import_inv/views/account_view.xml',
        
        'sh_import_inv_with_payment/security/import_inv_security.xml',
        'sh_import_inv_with_payment/security/ir.model.access.csv',
        'sh_import_inv_with_payment/wizard/import_inv_wizard.xml',
        'sh_import_inv_with_payment/views/account_view.xml',

        'sh_import_inventory_with_lot_serial/security/import_inventory_with_lot_serial_security.xml',
        'sh_import_inventory_with_lot_serial/security/ir.model.access.csv',
        'sh_import_inventory_with_lot_serial/wizard/import_inventory_with_lot_serial_wizard.xml',
        'sh_import_inventory_with_lot_serial/views/stock_view.xml',
        
        'sh_import_inventory_without_lot_serial/security/import_inventory_without_lot_serial_security.xml',
        'sh_import_inventory_without_lot_serial/security/ir.model.access.csv',
        'sh_import_inventory_without_lot_serial/wizard/import_inventory_without_lot_serial_wizard.xml',
        'sh_import_inventory_without_lot_serial/views/stock_view.xml',

        'sh_import_partner/security/import_partner_security.xml',
        'sh_import_partner/security/ir.model.access.csv',
        'sh_import_partner/wizard/import_partner_wizard.xml',
        'sh_import_partner/views/sale_view.xml',

        'sh_import_po/security/import_po_security.xml',
        'sh_import_po/security/ir.model.access.csv',
        'sh_import_po/wizard/import_po_wizard.xml',
        'sh_import_po/views/purchase_view.xml',

        'sh_import_pol/security/import_pol_security.xml',
        'sh_import_pol/security/ir.model.access.csv',
        'sh_import_pol/wizard/import_pol_wizard.xml',
        'sh_import_pol/views/purchase_view.xml',

        'sh_import_product_tmpl/security/import_product_tmpl_security.xml',
        'sh_import_product_tmpl/security/ir.model.access.csv',
        'sh_import_product_tmpl/wizard/import_product_tmpl_wizard.xml',
        'sh_import_product_tmpl/views/sale_view.xml',

        'sh_import_product_tmpl_mb/security/import_product_tmpl_security.xml',
        'sh_import_product_tmpl_mb/security/ir.model.access.csv',
        'sh_import_product_tmpl_mb/wizard/import_product_tmpl_wizard.xml',
        'sh_import_product_tmpl_mb/views/sale_view.xml',

        'sh_import_product_var/security/import_product_var_security.xml',
        'sh_import_product_var/security/ir.model.access.csv',
        'sh_import_product_var/wizard/import_product_var_wizard.xml',
        'sh_import_product_var/views/sale_view.xml',

        'sh_import_product_var_mb/security/import_product_var_security.xml',
        'sh_import_product_var_mb/security/ir.model.access.csv',
        'sh_import_product_var_mb/wizard/import_product_var_wizard.xml',
        'sh_import_product_var_mb/views/sale_view.xml',

        'sh_import_so/security/import_so_security.xml',
        'sh_import_so/security/ir.model.access.csv',
        'sh_import_so/wizard/import_so_wizard.xml',
        'sh_import_so/views/sale_view.xml',

        'sh_import_sol/security/import_sol_security.xml',
        'sh_import_sol/security/ir.model.access.csv',
        'sh_import_sol/wizard/import_sol_wizard.xml',
        'sh_import_sol/views/sale_view.xml',

        'sh_all_in_one_basic_import_advance/security/sh_all_in_one_basic_import.xml',
        'sh_all_in_one_basic_import_advance/security/ir.model.access.csv',
        'sh_all_in_one_basic_import_advance/data/sh_all_in_one_basic_kanban_data.xml',
        'sh_all_in_one_basic_import_advance/views/sh_all_in_one_basic_kanban_view.xml',

    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.gif", ],
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 55,
    "currency": "EUR"
}
