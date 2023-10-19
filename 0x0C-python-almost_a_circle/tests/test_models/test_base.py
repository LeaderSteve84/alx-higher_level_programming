#!/usr/bin/python3
"""a module of unittest for base.py."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unittest for testing base.py."""

    def test_create_instance(self):
        instance = Base()
        self.assertIsInstance(instance, Base)

    def test_create_with_id(self):
        instance = Base(10)
        self.assertEqual(instance.id, 10)

    def test_to_json_string(self):
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        json_string = Base.to_json_string(data)
        self.assertEqual(
                json_string, '[{"id": 1, "name": "Alice"}, {
                    "id": 2, "name": "Bob"}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(
                data, [{"id": 1, "name": "Alice"}, {
                    "id": 2, "name": "Bob"}])


if __name__ == "__main__":
    unittest.main()
