# -*- coding: utf-8 -*-
from odoo.tests.common import tagged
from odoo.addons.gesca_basic_import_extension.tests.common import TestImportCommon


import logging

_logger = logging.getLogger("===== Test Import So Wizard =====")


@tagged("-at_install", "post_install")
class TestSaleImport(TestImportCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        SaleOrder = cls.env["sale.order"].with_context(tracking_disable=True)
        # create a generic Sale Order with all classical products and empty pricelist
        cls.sale_order = SaleOrder.create(
            {
                "name": "SO187154",
                "partner_id": cls.partner_a.id,
                "partner_invoice_id": cls.partner_a.id,
                "partner_shipping_id": cls.partner_a.id,
                "pricelist_id": cls.company_data["default_pricelist"].id,
            }
        )
        cls.sol_product_order = cls.env["sale.order.line"].create(
            {
                "name": cls.company_data["product_order_no"].name,
                "product_id": cls.company_data["product_order_no"].id,
                "product_uom_qty": 2,
                "product_uom": cls.company_data["product_order_no"].uom_id.id,
                "price_unit": cls.company_data["product_order_no"].list_price,
                "order_id": cls.sale_order.id,
                "tax_id": False,
            }
        )

    def test_so_state(self):
        self.assertEqual(self.sale_order.state, "draft")

        file = self._data_file("confirm_sale_order.xls")

        self.import_so_wizard = self.env["import.so.wizard"].create(
            {
                "import_type": "excel",
                "import_mode": "update",
                "file": file,
            }
        )

        self.import_so_wizard.import_so_apply()
        self.assertEqual(self.sale_order.state, "sale")
