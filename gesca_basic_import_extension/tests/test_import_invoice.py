from odoo import fields
from odoo.tests.common import tagged
from odoo.addons.account.tests.common import AccountTestInvoicingCommon

from os import path
from base64 import b64encode


import logging
_logger = logging.getLogger("===== Test Import Invoice Wizard =====")


@tagged('-at_install', 'post_install')
class TestImportInvoice(AccountTestInvoicingCommon):
    
    @classmethod
    def _data_file(self, filename, encoding=None):
        mode = "rt" if encoding else "rb"
        with open(path.join(path.dirname(__file__), filename), mode) as file:
            data = file.read()
            if encoding:
                data = data.encode(encoding)
            return b64encode(data)

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super(TestImportInvoice, cls).setUpClass()
        
        cls.invoice_to_update = cls.env["account.move"].create(
            {
                "move_type": "out_invoice",
                "name": "INV/TO/UPDATE",
                "date": "2022-01-01",
                "partner_id": cls.partner_a.id,
                "invoice_date": fields.Date.from_string("2022-01-01"),
                "currency_id": cls.currency_data["currency"].id,
                "invoice_payment_term_id": cls.pay_terms_a.id,
                "invoice_line_ids": [
                    (
                        0,
                        None,
                        {
                            "name": cls.product_a.name,
                            "product_id": cls.product_a,
                            "product_uom_id": cls.product_a.uom_id,
                            "quantity": 5,
                            "price_unit": cls.product_a.lst_price,
                            "tax_ids": cls.product_a.taxes_id
                        },
                    ),
                ],
            }
        )

        
        file = cls._data_file("import_inv_excel.xls")
        
        cls.import_inv_wizard = cls.env['import.inv.wizard'].create({
            "import_type": "excel",
            "product_by": "name",
            "invoice_type": "inv",
            "account_option": "default",
            "is_validate": False,
            "inv_no_type": "auto",
            "import_mode": "update",
            "file": file
        })
        

    def test_import_invoice(self):
        # testiamo la data e lo stato
        self.import_inv_wizard.import_inv_apply()        
        self.assertEqual(self.invoice_to_update.state, "posted")
    