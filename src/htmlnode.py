
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props==None:
            return ""
        
        def from_dict_to_string(key,value):
            return f' {key}="{value}"'
        
        string_from_props = "".join(from_dict_to_string(key,value) for key, value in self.props.items()) 
        return string_from_props
    
    def __repr__(self):
        return f"HTMLNode(Tag:{self.tag}, Value:{self.value}, Children:{self.children}, Props:{self.props})"
    
    def __eq__(self, value):
        if not isinstance(value, self.__class__):
            return False
        return self.__dict__ == value.__dict__


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, value):
        if not isinstance(value, self.__class__):
            return False
        return self.__dict__== value.__dict__
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None,children, props)

    def to_html(self):
        if self.tag=="" or self.tag==None:
            raise ValueError("Invalid HTML: no tag.")
        
        if len(self.children)==0 or self.children == None:
            raise ValueError("Invalid HTML: no children")
        
        html_string_represetation = ""
        for child in self.children:
            html_string_represetation += child.to_html()

        html_string_represetation = f"<{self.tag}{self.props_to_html()}>{html_string_represetation}</{self.tag}>"

        return html_string_represetation
    

        
