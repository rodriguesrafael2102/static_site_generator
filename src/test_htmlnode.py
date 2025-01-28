import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):
    def test_equal(self):
        html_node = HTMLNode(tag="div", value="Hello, world!", children=None, props={"class": "greeting"})
        html_node2 = HTMLNode(tag="div", value="Hello, world!", children=None, props={"class": "greeting"})
        self.assertEqual(html_node, html_node2)

    def test_html_node_childre(self):
        image_node = HTMLNode(tag="img",
                                props={
                                    "src": "https://example.com/image.jpg",
                                    "alt": "Example image",
                                    "width": "600",
                                    "height": "400"})
        href_node= HTMLNode("a", value="Click here", children=None, props={"href": "https://www.google.com", "target": "_blank"})
        list_html_node = [image_node, href_node]
        div_node = HTMLNode("div", "Hello World", children=list_html_node, props={"class": "greeting"})

    def test_leaf_equal(self):
        leaf_node = LeafNode(tag="div", value="Hello, world!", props={"class": "greeting"})
        leaf_node2 = LeafNode(tag="div", value="Hello, world!", props={"class": "greeting"})
        self.assertEqual(leaf_node, leaf_node2)

    def test_to_html(self):
        leaf_node = LeafNode(tag="p", value="This is a paragraph", props={"class": "start-paragraph"})
        print(f"leaf_node.to_html() === {leaf_node.to_html()}")
        

    def test_to_html2(self):
        leaf_node = LeafNode(tag=None, value="This is a paragraph")
        print(f"leaf_node.to_html() - 2 === |{leaf_node.to_html()}|")
        

    def test_to_html3(self):
        try:
            leaf_node = LeafNode(tag=None, value="")
            print()
            print("test_to_html3:")
            print(f"leaf_node.to_html() === |{leaf_node.to_html()}|")
            print()
        except Exception as e:
            print(f"exception? === {type(e)}")
                  
    def test_ParentNode(self):
        parent_Node = ParentNode("p",
                                    [
                                        LeafNode("b", "Bold text"),
                                        LeafNode(None, "Normal text"),
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Normal text"),
                                    ],)
        print()
        print(f"parent_Node.to_html() === {parent_Node.to_html()}")
        print()

    def test_ParentNode2(self):
        parent_Node = ParentNode("",
                                    [
                                        LeafNode("b", "Bold text"),
                                        LeafNode(None, "Normal text"),
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Normal text"),
                                    ],)
        try:
            print(f"parent_Node.to_html() test 2 === {parent_Node.to_html()}")
        except Exception as e:
            print()
            print("test2 - parent node")
            print(f"error message === {e}")
            print()

    def test_ParentNode3(self):
        parent_Node = ParentNode("p", [])
        try:
            print(f"parent_Node.to_html() test 3 === {parent_Node.to_html()}")
        except Exception as e:
            print()
            print("test3 - parent node")
            print(f"error message === {e}")
            print()
    
    def test_ParentNode4(self):
        parent_Node = ParentNode("p", None  )
        try:
            print(f"parent_Node.to_html() test 3 === {parent_Node.to_html()}")
        except Exception as e:
            print()
            print("test4 - parent node")
            print(f"error message === {e}")
            print()

    def test_ParentNode5(self):
        parent_Node = ParentNode("div",
                                    [
                                        LeafNode("b", "Bold text"),
                                        ParentNode("div",
                                                    [
                                                        LeafNode("b", "Bold text"),
                                                        ParentNode("p",
                                                                    [
                                                                        LeafNode("a", "This is a link", {"href": "www.google.com"}),
                                                                        LeafNode(None, "Normal text"),
                                                                        LeafNode("i", "italic text"),
                                                                        LeafNode(None, "Normal text"),
                                                                    ],props={"class": "greeting"}),
                                                        LeafNode("i", "italic text"),
                                                        LeafNode(None, "Normal text"),
                                                    ],props={"class": "greeting"}),
                                        LeafNode("i", "italic text"),
                                        ParentNode("p",
                                    [
                                        LeafNode("b", "Bold text"),
                                        LeafNode(None, "Normal text"),
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Normal text"),
                                    ],props={"class": "greeting"}),
                                    ],props={"class": "greeting"})
        try:
            print()
            print(f"parent_Node.to_html() test 5 === {parent_Node.to_html()}")
            print()
        except Exception as e:
            print()
            print("test5 - parent node")
            print(f"error message === {e}")
            print()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("i", "This is text to be italic")
        child_node3 = LeafNode(None, "This is just a normal text")
        child_node4 = LeafNode("a", "This is a link", {"href": "www.google.com"})
        parent_node = ParentNode("div", [child_node, child_node2, child_node3,child_node4])
        self.assertEqual(parent_node.to_html(), '<div><span>child</span><i>This is text to be italic</i>This is just a normal text<a href="www.google.com">This is a link</a></div>')
        

if __name__ == "__main__":
    unittest.main()