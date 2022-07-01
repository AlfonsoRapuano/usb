# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger("===== GESCA Product Pack ======")


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def _get_invoiceable_lines(self, final=False):
        return [i for i in super()._get_invoiceable_lines() if not i.pack_parent_line_id]
    

class Sale_order_line(models.Model):
    _inherit = 'sale.order.line'
    
    # Fields for common packs
    pack_depth = fields.Integer(
        "Depth", help="Depth of the product if it is part of a pack."
    )
    pack_parent_line_id = fields.Many2one(
        "sale.order.line",
        "Pack",
        help="The pack that contains this product.",
    )
    pack_modifiable = fields.Boolean(help="The parent pack is modifiable")
    
    is_pack = fields.Boolean(related='product_id.is_pack')
    
    @api.model
    def create(self, vals):
        record = super().create(vals)
        record.expand_pack_line()
        return record
    
    def write(self, vals):
        res = super().write(vals)
        if "product_id" in vals or "product_uom_qty" in vals:
            for record in self:
                record.expand_pack_line(write=True)
        return res
    
    def expand_pack_line(self, write=False):
        self.ensure_one()
        vals_list = []
        if self.product_id.is_pack:
            for subline in self.product_id.pack_ids:
                vals = subline.get_sale_order_line_vals(self, self.order_id)
                vals["sequence"] = self.sequence
                vals_list.append(vals)
            if vals_list:
                self.create(vals_list)
    

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    pack_modifiable = fields.Boolean(
        help="If you check this field yo will be able to edit "
        "sale/purchase order line relate to its component",
    )
    pack_component_price = fields.Selection(
        [
            ("detailed", "Detailed per component"),
            ("totalized", "Totalized in main product"),
            ("ignored", "Ignored"),
        ],
        "Pack component price",
        help="On sale orders or purchase orders:\n"
        "* Detailed per component: Detail lines with prices.\n"
        "* Totalized in main product: Detail lines merging "
        "lines prices on pack (don't show component prices).\n"
        "* Ignored: Use product pack price (ignore detail line prices).",
    )
    pack_type = fields.Selection(
        [("detailed", "Detailed"), ("non_detailed", "Non Detailed")],
        string="Pack Display Type",
        help="On sale orders or purchase orders:\n"
        "* Detailed: Display components individually in the sale order.\n"
        "* Non Detailed: Do not display components individually in the"
        " sale order.",
    )
    
                
class ProductPack(models.Model):
    _inherit = "product.pack"

    sale_discount = fields.Float(
        "Sale discount (%)",
        digits="Discount",
    )

    def get_sale_order_line_vals(self, line, order):
        self.ensure_one()
        quantity = self.qty_uom * line.product_uom_qty
        line_vals = {
            "order_id": order.id,
            "product_id": self.product_id.id or False,
            "pack_parent_line_id": line.id,
            "pack_depth": line.pack_depth + 1,
            "company_id": order.company_id.id,
            "pack_modifiable": line.product_id.pack_modifiable,
        }
        sol = line.new(line_vals)
        sol.product_id_change()
        sol.product_uom_qty = quantity
        sol.product_uom_change()
        sol._onchange_discount()
        vals = sol._convert_to_write(sol._cache)
        pack_price_types = {"totalized", "ignored"}
        sale_discount = 0.0
        if line.product_id.pack_component_price == "detailed":
            sale_discount = 100.0 - (
                (100.0 - sol.discount) * (100.0 - self.sale_discount) / 100.0
            )
        elif (
            line.product_id.pack_type == "detailed"
            and line.product_id.pack_component_price in pack_price_types
        ):
            vals["price_unit"] = 0.0
        vals.update(
            {
                "discount": sale_discount,
                "name": "{}{} > {}".format("> " * (line.pack_depth + 1),sol.pack_parent_line_id.name, sol.name),
            }
        )
        return vals
