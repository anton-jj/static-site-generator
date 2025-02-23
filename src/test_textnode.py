
import unittest

from textnode import Textnode, TextType

class TestTextnoce(unittest.TestCase):
    def test_eq(self):
        node = Textnode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text_type, TextType.BOLD)

        node = Textnode("click here", TextType.LINKS)
        self.assertEqual(node.text, "click here")
        self.assertEqual(node.text_type, TextType.LINKS)


if __name__ == "__main__":
    unittest.main()
