# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, api, models, _
import base64
import xlrd
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger("===== Gesca Update Project Task Wizard =====")


class ImportPROJTASKWizardInherit(models.TransientModel):
    _name = "import.proj.task.wizard"

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
    def update_project_tasks(self):

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

        # nel caso dei task, è opportuno fornire due campi per l'aggiornamento:
        # nome del progetto e nome del task
        for i in range(len(values)):
            project_to_update = self.env["project.project"].search(
                [("name", "=", values[i][0])]
            )
            if project_to_update:
                task_to_update = self.env["project.task"].search(
                    [
                        ("name", "=", values[i][1]),
                        ("project_id", "=", project_to_update.id),
                    ]
                )

                if task_to_update:

                    # _logger.info(values[i])

                    for j in range(2, len(values[i])):
                        # _logger.info(j)
                        # _logger.info(fields[i][j])

                        # _logger.info(values[i][j])

                        try:
                            task_to_update.write({fields[j]: values[i][j]})
                        except:
                            raise UserError(
                                "Attenzione! Valore errato per il campo: "
                                + fields[j]
                                + " del task "
                                + values[i][1]
                                + ": "
                                + values[i][j]
                            )
                else:
                    raise UserError(
                        "Attenzione! Nessun task presente con nome: " + values[i][1]
                    )
            else:
                raise UserError(
                    "Attenzione! Nessun progetto presente con nome: " + values[i][0]
                )
