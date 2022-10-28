# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, api, models, _
import base64
import xlrd
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger("===== Gesca Import Purchase Order Wizard =====")


class ImportPOWizard(models.TransientModel):
    _inherit = "import.po.wizard"

    import_type = fields.Selection(
        [
            ("csv", "CSV File"),
            ("excel", "Excel File")
            # GESCA, mettiamo di default Excel come tipo di file
            # ], default="csv", string="Import File Type", required=True)
        ],
        default="excel",
        string="Import File Type",
        required=True,
    )

    # GESCA
    # per permettere un'importazione in aggiornamento e non solo in creazione, dobbiamo creare un nuovo flag
    import_mode = fields.Selection(
        [("create", "Creazione"), ("update", "Aggiornamento")],
        default="create",
        string="Modalità importazione",
        required=True,
    )

    # GESCA
    # metodo per chiamare le azioni corrispondenti ai vari stati
    def do_corresponding_state_action(self, po, state):
        # For Excel
        if state == "Confermato":
            po.button_confirm()
        elif state == "Cancellato":
            po.button_cancel()
        elif state == "Bozza":
            po.button_draft()

    # GESCA
    # funzione di aggiornamento di ordini di acquisto già esistenti
    def update_purchase_orders(self, matrix):

        fields = matrix[0]
        values = matrix[1:]

        for i in range(len(values)):
            po_to_update = self.env["purchase.order"].search(
                [("name", "=", values[i][0])]
            )

            if not po_to_update:
                raise UserError(
                    "Attenzione! Nessun ordine di vendita presente con riferimento uguale a : "
                    + values[i][0]
                )
            for j in range(len(values[i])):
                if fields[j] != "state":
                    try:
                        po_to_update.write({fields[j]: values[i][j]})
                    except:
                        raise UserError(
                            "Attenzione! Valore errato per il campo: "
                            + fields[j]
                            + " dell'ordine "
                            + values[i][0]
                            + ": "
                            + values[i][j]
                        )
                else:
                    self.do_corresponding_state_action(po_to_update, values[i][j])

    # GESCA
    # metodo per recuperare una matrice da un foglio excel
    def get_matrix(self):
        # For Excel
        wb = xlrd.open_workbook(file_contents=base64.decodebytes(self.file))
        sheet = wb.sheet_by_index(0)
        return [
            [sheet.cell(r, c).value for c in range(sheet.ncols)]
            for r in range(sheet.nrows)
        ]

    def import_po_apply(self):
        # GESCA
        # se abbiamo flaggato aggiornamento, dobbiamo chiamare un altro metodo
        if self.import_mode != "create" and self.file:
            return self.update_purchase_orders(self.get_matrix())
        else:
            return super().import_po_apply()
