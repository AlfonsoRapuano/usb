# -*- coding: utf-8 -*-
from odoo.tests.common import tagged
from odoo.addons.gesca_basic_import_extension.tests.common import TestImportCommon


import logging

_logger = logging.getLogger("===== Test Import Po Wizard =====")


@tagged("-at_install", "post_install")
class TestPurchaseImport(TestImportCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PurchaseOrder = cls.env["purchase.order"].with_context(tracking_disable=True)
        # create a generic purchase Order with all classical products and empty pricelist
        cls.purchase_order = PurchaseOrder.create(
            {
                "name": "P00001",
                "partner_id": cls.partner_a.id,
            }
        )
        cls.pol_product_order = cls.env["purchase.order.line"].create(
            {
                "name": cls.company_data["product_order_no"].name,
                "product_id": cls.company_data["product_order_no"].id,
                "product_uom_qty": 2,
                "product_uom": cls.company_data["product_order_no"].uom_id.id,
                "price_unit": cls.company_data["product_order_no"].standard_price,
                "order_id": cls.purchase_order.id,
                "taxes_id": False,
            }
        )

    def test_po_state(self):
        self.assertEqual(self.purchase_order.state, "draft")

        file = self._data_file("confirm_purchase_order.xls")

        self.import_po_wizard = self.env["import.po.wizard"].create(
            {
                "import_type": "excel",
                "import_mode": "update",
                "file": file,
            }
        )

        self.import_po_wizard.import_po_apply()
        self.assertEqual(self.purchase_order.state, "purchase")

        file = self._data_file("cancel_purchase_order.xls")

        self.import_po_wizard = self.env["import.po.wizard"].create(
            {
                "import_type": "excel",
                "import_mode": "update",
                "file": file,
            }
        )

        self.import_po_wizard.import_po_apply()
        self.assertEqual(self.purchase_order.state, "cancel")

        file = self._data_file("reset_draft_purchase_order.xls")

        self.import_po_wizard = self.env["import.po.wizard"].create(
            {
                "import_type": "excel",
                "import_mode": "update",
                "file": file,
            }
        )

        self.import_po_wizard.import_po_apply()
        self.assertEqual(self.purchase_order.state, "draft")
