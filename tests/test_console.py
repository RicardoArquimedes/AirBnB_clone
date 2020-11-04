#!/usr/bin/python3
"""Command test
"""
import unittest
from unittest.mock import patch
import sys
from io import StringIO
import os
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class testCommand(unittest.TestCase):
    """test for command"""
    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("quit")
        value = fd.getvalue()
        self.assertEqual(value, "")

    def test_emptyline(self):
        """test for emptyline"""
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("")
        value = fd.getvalue()
        self.assertEqual(value, "")

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("EOF")
        value = fd.getvalue()
        self.assertEqual(value, "")
