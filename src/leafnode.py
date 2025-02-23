from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props): 
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props


    def to_html(self):
        if self.value is "" or self.value is None:
            return self.value


