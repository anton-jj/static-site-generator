import unittest 

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is just a paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "this is just a paragraph")


        child_node = HTMLNode("span",value="click me") 
        node = HTMLNode("div", "Hello World", child_node, {"class" : "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, child_node)  # One child node
        self.assertEqual(node.props, {"class": "container"})


