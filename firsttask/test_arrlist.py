import unittest
from arrlist import ArrayList  # Assuming ArrayList class is defined in arraylist.py

class TestArrayList(unittest.TestCase):

    def setUp(self):
        self.array_list = ArrayList()

    def test_initialization(self):
        self.assertEqual(self.array_list.size(), 0)
        self.assertTrue(self.array_list.is_empty())

    def test_add_and_get(self):
        self.array_list.add(1)
        self.array_list.add(2)
        self.assertEqual(self.array_list.size(), 2)
        self.assertEqual(self.array_list.get(0), 1)
        self.assertEqual(self.array_list.get(1), 2)

    def test_get_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.array_list.get(0)  # Empty list, index 0 should raise IndexError

        self.array_list.add(1)
        self.array_list.add(2)

        with self.assertRaises(IndexError):
            self.array_list.get(2)  # Index 2 is out of bounds

    def test_remove(self):
        self.array_list.add(1)
        self.array_list.add(2)
        self.assertEqual(self.array_list.size(), 2)

        removed_value = self.array_list.remove(0)
        self.assertEqual(removed_value, 1)
        self.assertEqual(self.array_list.size(), 1)
        self.assertEqual(self.array_list.get(0), 2)

    def test_remove_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.array_list.remove(0)  # Empty list, index 0 should raise IndexError

        self.array_list.add(1)
        self.array_list.add(2)

        with self.assertRaises(IndexError):
            self.array_list.remove(2)  # Index 2 is out of bounds

    def test_multiple_operations(self):
        self.assertTrue(self.array_list.is_empty())

        self.array_list.add(1)
        self.array_list.add(2)
        self.assertEqual(self.array_list.size(), 2)

        self.assertEqual(self.array_list.get(0), 1)
        self.assertEqual(self.array_list.get(1), 2)

        removed_value = self.array_list.remove(0)
        self.assertEqual(removed_value, 1)
        self.assertEqual(self.array_list.size(), 1)
        self.assertEqual(self.array_list.get(0), 2)

        self.array_list.add(3)
        self.assertEqual(self.array_list.size(), 2)
        self.assertEqual(self.array_list.get(1), 3)

    def test_edge_cases(self):
        # Test with large number of elements
        for i in range(1000):
            self.array_list.add(i)
        self.assertEqual(self.array_list.size(), 1000)
        self.assertEqual(self.array_list.get(999), 999)

        # Test removing all elements
        for i in range(999, -1, -1):
            self.assertEqual(self.array_list.remove(0), i)
        self.assertTrue(self.array_list.is_empty())
        self.assertEqual(self.array_list.size(), 0)

if __name__ == '__main__':
    unittest.main()

