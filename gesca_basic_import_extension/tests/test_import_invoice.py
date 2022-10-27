from odoo import fields
from odoo.tests.common import tagged
from odoo.addons.gesca_basic_import_extension.tests.common import TestImportCommon
from odoo.exceptions import UserError

import datetime

import logging

_logger = logging.getLogger("===== Test Import Invoice Wizard =====")


@tagged("-at_install", "post_install")
class TestImportInvoice(TestImportCommon):
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
                            "tax_ids": cls.product_a.taxes_id,
                        },
                    ),
                ],
            }
        )

    def test_invoice_state(self):

        file = self._data_file("confirm_invoice.xls")

        self.import_inv_wizard = self.env["import.inv.wizard"].create(
            {
                "import_type": "excel",
                "product_by": "name",
                "invoice_type": "inv",
                "account_option": "default",
                "is_validate": False,
                "inv_no_type": "auto",
                "import_mode": "update",
                "file": file,
            }
        )

        # testiamo la data e lo stato
        self.import_inv_wizard.import_inv_apply()
        self.assertEqual(self.invoice_to_update.state, "posted")

        file = self._data_file("cancel_invoice.xls")

        self.import_inv_wizard = self.env["import.inv.wizard"].create(
            {
                "import_type": "excel",
                "product_by": "name",
                "invoice_type": "inv",
                "account_option": "default",
                "is_validate": False,
                "inv_no_type": "auto",
                "import_mode": "update",
                "file": file,
            }
        )

        # testiamo la data e lo stato
        self.import_inv_wizard.import_inv_apply()
        self.assertEqual(self.invoice_to_update.state, "draft")

    def test_invoice_date(self):

        file = self._data_file("import_invoice_date.xls")

        self.import_inv_wizard = self.env["import.inv.wizard"].create(
            {
                "import_type": "excel",
                "product_by": "name",
                "invoice_type": "inv",
                "account_option": "default",
                "is_validate": False,
                "inv_no_type": "auto",
                "import_mode": "update",
                "file": file,
            }
        )

        # testiamo la data e lo stato
        self.import_inv_wizard.import_inv_apply()
        self.assertEqual(
            self.invoice_to_update.invoice_date,
            datetime.datetime.strptime("2025-02-02", "%Y-%m-%d").date(),
        )

    def test_field_error(self):

        file = self._data_file("import_invoice_error.xls")

        self.import_inv_wizard = self.env["import.inv.wizard"].create(
            {
                "import_type": "excel",
                "product_by": "name",
                "invoice_type": "inv",
                "account_option": "default",
                "is_validate": False,
                "inv_no_type": "auto",
                "import_mode": "update",
                "file": file,
            }
        )
        with self.assertRaises(UserError):
            # testiamo la data e lo stato
            self.import_inv_wizard.import_inv_apply()
