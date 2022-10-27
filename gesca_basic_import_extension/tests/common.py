# -*- coding: utf-8 -*-
from odoo.tests.common import tagged
from odoo.addons.sale.tests.common import TestSaleCommon

from os import path
from base64 import b64encode


@tagged("-at_install", "post_install")
class TestImportCommon(TestSaleCommon):
    @classmethod
    def _data_file(self, filename, encoding=None):
        mode = "rt" if encoding else "rb"
        with open(path.join(path.dirname(__file__), filename), mode) as file:
            data = file.read()
            if encoding:
                data = data.encode(encoding)
            return b64encode(data)
