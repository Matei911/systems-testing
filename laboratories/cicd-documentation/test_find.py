import unittest
from tree import Tree
# tests for the find method in the Tree class
class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.t = Tree()
        for v in (10, 5, 15, 3, 7, 13, 18):
            self.t.add(v)

    def test_find_existing(self):
        node = self.t.find(7)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 7)

    def test_find_root(self):
        self.assertEqual(self.t.find(10).data, 10)

    def test_find_missing(self):
        self.assertIsNone(self.t.find(42))

if __name__ == "__main__":
    unittest.main()