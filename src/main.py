from leafnode import LeafNode
from textnode import TextType, Textnode
from htmlnode import HTMLNode
print("hello world")

textnode = Textnode("this is a text", TextType.ITALLIC, "https://www.boot.dev")
htmlnode = HTMLNode("p", "this is a paragraph")
child_node = HTMLNode("span",value="click me") 
node = HTMLNode("div", "Hello World", child_node, {"class" : "container"})
leafnode = LeafNode("div", "value",  "http://something.com")
    


print(textnode.__repr__())
print(node.__repr__())
print("this is a leaf " + leafnode.__repr__())
