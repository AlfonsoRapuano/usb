# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, api, models, _
import base64
import xlrd

import logging

_logger = logging.getLogger("===== Gesca Import Invoice Wizard =====")


class ImportINVWizardInherit(models.TransientModel):
    _inherit = "import.inv.wizard"

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
        string="Modailità importazione",
        required=True,
    )

    # GESCA
    # metodo per chiamare le azioni corrispondenti ai vari stati
    def do_corresponding_state_action(self, invoice, state):
        # For Excel
        if state == "Confermato":
            invoice.action_post()
        elif state == "Cancellato":
            invoice.button_draft()

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

    # GESCA
    # funzione di aggiornamento di fatture già esistenti
    def update_invoices(self, matrix):

        fields = matrix[0]
        values = matrix[1:]

        for i in range(len(values)):
            invoice_to_update = self.env["account.move"].search(
                [("name", "=", values[i][0])]
            )
            for j in range(len(values[i])):
                if fields[j] != "state":
                    invoice_to_update.write({fields[j]: values[i][j]})

                else:
                    self.do_corresponding_state_action(invoice_to_update, values[i][j])

    def import_inv_apply(self):
        # GESCA
        # se abbiamo flaggato aggiornamento, dobbiamo chiamare un altro metodo
        if self.import_mode != "create" and self.file:
            return self.update_invoices(self.get_matrix())
        else:
            return super().import_inv_apply()
