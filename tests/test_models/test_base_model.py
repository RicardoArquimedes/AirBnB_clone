#!/usr/bin/python3
""" Test for base models
"""


import unittest
import pep8
from models.base_model import BaseModel
from datetime import date, datetime


class testBase(unittest.TestCase):

    """ Test base class
    """

    def test_pep8_conformance_BaseModel(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_to_dict(self):
        """Test the to_dict method from BaseModel"""
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertEqual(bm1_dict["__class__"], "BaseModel")
        self.assertEqual(str(bm1.id), bm1_dict["id"])
        self.assertIsInstance(bm1_dict["created_at"], str)
        self.assertIsInstance(bm1_dict["updated_at"], str)

    def test_new_attributte(self):
        """test to check if new attribute  can be added"""
        bm1 = BaseModel()
        bm1.name = "Miguel"
        self.assertEqual(bm1.name, "Miguel")

    def test_init_from_dict(self):
        """test to check a new instance witk Kwargs"""
        my_dict = {'id': 'fe96e299-dd6e-42da-9e9f-9d49d229e850',
                   'created_at': '2017-09-28T21:03:54.052298',
                   '__class__': 'BaseModel', 'my_number': 89,
                   'updated_at': '2017-09-28T21:03:54.052302',
                   'name': 'Holberton'}
        bm1 = BaseModel(**my_dict)
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm1.id, str)
        self.assertEqual(bm1.id, 'fe96e299-dd6e-42da-9e9f-9d49d229e850')
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertIsInstance(bm1.name, str)
        self.assertEqual(bm1.name, 'Holberton')
        self.assertEqual(
            bm1.created_at.isoformat(), '2017-09-28T21:03:54.052298')
        self.assertEqual(
            bm1.updated_at.isoformat(), '2017-09-28T21:03:54.052302')
