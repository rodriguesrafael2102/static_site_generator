from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,text, text_type, url=None):
        self.text = text # The text content of the node
        self.text_type = text_type # The type of text this node contains, which is a member of the TextType enum.
        self.url = url #  The URL of the link or image, if the text is a link. Default to None if nothing is passed in.

    def __eq__(self, value):
        if not isinstance(value, self.__class__):
            return False
        return self.__dict__== value.__dict__
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case(TextType.NORMAL):
            return LeafNode(None, text_node.text)
    
        case(TextType.BOLD):
            return LeafNode("b", text_node.text)
        
        case(TextType.ITALIC):
            return LeafNode("i", text_node.text)
        
        case(TextType.CODE):
            return LeafNode("code", text_node.text)
        
        case(TextType.LINK):
            return LeafNode("a", text_node.text, {"href": text_node.url})
        
        case(TextType.IMAGE):
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        
        case _:
            raise Exception(f"Invalid HTML: no valid type {text_node.text_type}")


