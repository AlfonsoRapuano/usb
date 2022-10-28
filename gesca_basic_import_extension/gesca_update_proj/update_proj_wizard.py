# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, api, models, _
import base64
import xlrd
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger("===== Gesca Update Project Wizard =====")


class ImportPROJWizardInherit(models.TransientModel):
    _name = "import.proj.wizard"

    file = fields.Binary(string="File", required=True)

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
    # funzione di aggiornamento di progetti già esistenti
    def update_projects(self):

        # For Excel
        # Da provare: https://stackoverflow.com/questions/28774960/how-to-get-read-excel-data-into-an-array-with-python
        wb = xlrd.open_workbook(file_contents=base64.decodebytes(self.file))
        sheet = wb.sheet_by_index(0)
        matrix = [
            [sheet.cell(r, c).value for c in range(sheet.ncols)]
            for r in range(sheet.nrows)
        ]

        fields = matrix[0]
        values = matrix[1:]

        for i in range(len(values)):
            project_to_update = self.env["project.project"].search(
                [("name", "=", values[i][0])]
            )

            if not project_to_update:
                raise UserError(
                    "Attenzione! Nessun progetto presente con nome: " + values[i][0]
                )
            for j in range(len(values[i])):
                try:
                    project_to_update.write({fields[j]: values[i][j]})
                except:
                    raise UserError(
                        "Attenzione! Valore errato per il campo: "
                        + fields[j]
                        + " del progetto "
                        + values[i][0]
                        + ": "
                        + values[i][j]
                    )
