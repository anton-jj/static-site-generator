from textnode import TextType, Textnode
print("hello world")

textnode = Textnode("this is a text", TextType.ITALLIC, "https://www.boot.dev")

print(textnode.__repr__())
