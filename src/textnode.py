from enum import Enum 

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALLIC = "itallic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class Textnode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        if isinstance(other, Textnode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return False


    def __repr__(self):
        return f"TextNode(text={self.text!r}, text_type={self.text_type!r}, url={self.url!r})"

