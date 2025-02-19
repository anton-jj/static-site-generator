
import unittest

from textnode import Textnode, TextType

class TestTextnoce(unittest.TestCase):
    def test_eq(self):
        node = Textnode("This is a text node", TextType.BOLD)
        node2 = Textnode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
