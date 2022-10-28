# -*- coding: utf-8 -*-
from odoo.tests.common import tagged
from odoo.addons.gesca_basic_import_extension.tests.common import TestImportCommon
import datetime

import logging

_logger = logging.getLogger("===== Test Import Project Wizard =====")


@tagged("-at_install", "post_install")
class TestProjectImport(TestImportCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Test users to use through the various tests
        Users = cls.env["res.users"].with_context({"no_reset_password": True})

        user_group_employee = cls.env.ref("base.group_user")
        user_group_project_user = cls.env.ref("project.group_project_user")
        user_group_project_manager = cls.env.ref("project.group_project_manager")

        cls.user_projectuser = Users.create(
            {
                "name": "Armande ProjectUser",
                "login": "Armande",
                "email": "armande.projectuser@example.com",
                "groups_id": [
                    (6, 0, [user_group_employee.id, user_group_project_user.id])
                ],
            }
        )

        cls.user_projectmanager = Users.create(
            {
                "name": "Bastien ProjectManager",
                "login": "bastien",
                "email": "bastien.projectmanager@example.com",
                "groups_id": [
                    (6, 0, [user_group_employee.id, user_group_project_manager.id])
                ],
            }
        )

        # Test 'Pigs' project
        cls.project_pigs = (
            cls.env["project.project"]
            .with_context({"mail_create_nolog": True})
            .create(
                {
                    "name": "Pigs",
                    "privacy_visibility": "employees",
                    "alias_name": "project+pigs",
                    "partner_id": cls.partner_a.id,
                }
            )
        )
        # Already-existing tasks in Pigs
        cls.task_1 = (
            cls.env["project.task"]
            .with_context({"mail_create_nolog": True})
            .create(
                {
                    "name": "Pigs UserTask",
                    "user_id": cls.user_projectuser.id,
                    "project_id": cls.project_pigs.id,
                }
            )
        )
        cls.task_2 = (
            cls.env["project.task"]
            .with_context({"mail_create_nolog": True})
            .create(
                {
                    "name": "Pigs ManagerTask",
                    "user_id": cls.user_projectmanager.id,
                    "project_id": cls.project_pigs.id,
                }
            )
        )

        """
        # Test 'Goats' project, same as 'Pigs', but with 2 stages
        cls.project_goats = cls.env['project.project'].with_context({'mail_create_nolog': True}).create({
            'name': 'Goats',
            'privacy_visibility': 'followers',
            'alias_name': 'project+goats',
            'partner_id': cls.partner_1.id,
            'type_ids': [
                (0, 0, {
                    'name': 'New',
                    'sequence': 1,
                }),
                (0, 0, {
                    'name': 'Won',
                    'sequence': 10,
                })]
            })
        """

    def test_import_project_field(self):

        file = self._data_file("update_project.xls")

        self.import_proj_wizard = self.env["import.proj.wizard"].create(
            {
                "import_type": "excel",
                "file": file,
            }
        )

        self.import_proj_wizard.update_projects()
        self.assertEqual(
            self.project_pigs.description, "<p>Descrizione progetto di test</p>"
        )

    def test_import_project_task_field(self):

        file = self._data_file("update_project_task.xls")

        self.import_proj_task_wizard = self.env["import.proj.task.wizard"].create(
            {
                "import_type": "excel",
                "file": file,
            }
        )

        self.import_proj_task_wizard.update_project_tasks()
        self.assertEqual(
            self.task_1.date_assign,
            datetime.datetime(2025, 2, 2, 0, 0),
        )
