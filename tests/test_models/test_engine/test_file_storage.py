#!/usr/bin/python3
"""Unittest for BaseModel
"""


import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """unittest_BaseModel"""

    def test_storage(self):
        """test for storage"""

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]

        try:
            with open("file.json", "r", encoding='utf-8') as f:
                self.assertIsInstance(all_objs, dict)
                self.assertIsInstance(obj, BaseModel)
                val = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
                self.assertEqual(str(obj), val)
                self.assertEqual(f"{obj_id}",
                                 f"{obj.__class__.__name__}.{obj.id}")
        except FileNotFoundError:
            self.assertIsInstance(all_objs, dict)
            self.assertEqual(all_objs, {})

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

    def test_instances(self):
        """check instance"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test doc"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    def test_storage_empty(self):
        """check storage is not empty"""

        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """check type of storage"""

        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """check new user"""
        obj = self.storage.all()
        self.u1.id = 1234
        self.u1.name = "ouafae"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(obj[key])

    def test_json_loading(self):
        """ Checks Storage Engine works."""

        with open("file.json") as f:
            dic = json.load(f)

            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """
        Checks from Storage Engine works.
        """

        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)


if __name__ == '__main__':
    unittest.main()
