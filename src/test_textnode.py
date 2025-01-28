import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_unequal(self):
        node = TextNode("This is another text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        try:
            self.assertEqual(node, node2)
        except:
            print("test unequal === success")

    def test_represent(self):
        node = TextNode("This is another text node", TextType.IMAGE.value)
        node2 = TextNode("This is a text node", TextType.BOLD)
        if node.__repr__() == "TextNode(This is another text node, image, None)" and node2.__repr__() == "TextNode(This is a text node, TextType.BOLD, None)":
            print("test_represent === test success")
        else:
            print("test_represent === test fail")

    def test_diff_url(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://google.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://yahoo.com")
        
    def test_text_to_leaf(self):
        leaf_node_normal = TextNode("This is a normal node", TextType.NORMAL).text_node_to_html_node()
        leaf_node_bold = TextNode("This is a bold text", TextType.BOLD).text_node_to_html_node()
        leaf_node_italic = TextNode("This is a italic text", TextType.ITALIC).text_node_to_html_node()
        leaf_node_code   = TextNode("This is a italic text", TextType.CODE).text_node_to_html_node()
        leaf_node_link   = TextNode("This is a link", TextType.LINK).text_node_to_html_node()
        leaf_node_image = TextNode("This is an image being described", TextType.IMAGE, "https://google.com").text_node_to_html_node()

    def test_text_none_type(self):
        try:
            leaf_node_none = TextNode("This is a normal node", "TIPO_INEXISTENTE").text_node_to_html_node()
            print(f"test_text_to_leaf(self) NONE === {leaf_node_none.to_html()}")
        except Exception as e:
            print()
            print(f"e message === {e}")
            print()

if __name__ == "__main__":
    unittest.main()
