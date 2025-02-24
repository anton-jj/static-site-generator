from textnode import TextType, Textnode
from htmlnode import HTMLNode, LeafNode, ParentNode

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)


print(node.to_html())
