# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, api, models, _
import base64
import xlrd
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger("===== Gesca Import Sale Order Wizard =====")


class ImportSOWizard(models.TransientModel):
    _inherit = "import.so.wizard"

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
    def do_corresponding_state_action(self, so, state):
        # For Excel
        if state == "Confermato":
            so.action_confirm()
        elif state == "Cancellato":
            so.action_cancel()
        elif state == "Bozza":
            so.action_draft()

    # GESCA
    # funzione di aggiornamento di ordini di vendita già esistenti
    def update_sale_orders(self, matrix):

        fields = matrix[0]
        values = matrix[1:]

        for i in range(len(values)):
            so_to_update = self.env["sale.order"].search([("name", "=", values[i][0])])

            if not so_to_update:
                raise UserError(
                    "Attenzione! Nessun ordine di vendita presente con riferimento uguale a : "
                    + values[i][0]
                )
            for j in range(len(values[i])):
                if fields[j] != "state":
                    try:
                        so_to_update.write({fields[j]: values[i][j]})
                    except:
                        raise UserError(
                            "Attenzione! Valore errato per il campo: "
                            + fields[j]
                            + " della fattura "
                            + values[i][0]
                            + ": "
                            + values[i][j]
                        )
                else:
                    self.do_corresponding_state_action(so_to_update, values[i][j])

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

    def import_so_apply(self):
        # GESCA
        # se abbiamo flaggato aggiornamento, dobbiamo chiamare un altro metodo
        if self.import_mode != "create" and self.file:
            return self.update_sale_orders(self.get_matrix())
        else:
            return super().import_so_apply()
