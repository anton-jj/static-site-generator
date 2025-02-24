

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props  if props is not None else {}

    def to_html(self): 
        pass

    def props_to_html(self):
        if self.props is None: 
            return ""
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())


    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None): 
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("there shoudl be a value in the value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
            
    def to_html(self):
        if self.tag is None:
            raise ValueError("this has to have a tag")
        if self.children is None:
            raise ValueError("this is a parent node children can't be none")

        child_html = ''.join(child.to_html() for child in self.children)


        return f"<{self.tag}>{self.props_to_html()}>{child_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"


