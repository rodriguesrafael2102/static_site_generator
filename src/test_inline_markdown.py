import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

class TestTextNode(unittest.TestCase):
    def test_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        print()
        print(f"test_delimiter_code ` ")
        list_text_nodes=split_nodes_delimiter([node], "`", TextType.CODE)
        print(f"list_text_nodes === {list_text_nodes}")
        print()
    
    def test_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.NORMAL)
        print()
        print(f"test_delimiter_bold **")
        list_text_nodes=split_nodes_delimiter([node], "**", TextType.BOLD)
        print(f"list_text_nodes === {list_text_nodes}")
        print()

    def test_delimiter_italic(self):
        node = TextNode("This is text with a *italic block* word", TextType.NORMAL)
        print()
        print(f"test_delimiter_italic *")
        list_text_nodes=split_nodes_delimiter([node], "*", TextType.ITALIC)
        print(f"list_text_nodes === {list_text_nodes}")
        print()

    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        print(f"extract_markdown_images(text) === {extract_markdown_images(text)}")

    def test_extract_links(self):
        text = "This is a text with links, two links: [to boot dev](https://www.boot.dev) and [to google](https://www.google.com)"
        print(f"extract_markdown_links(text) === {extract_markdown_links(text)}")

    def test_extracting_both(self):
        text = "This is a text that will have both a image (here: ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)) and a link (here: [to google](https://www.google.com))."
        print()
        print(f"extract_markdown_images(text) === {extract_markdown_images(text)}")
        print(f"extract_markdown_links(text) === {extract_markdown_links(text)}")
        print()

    def test_error_on_purpose(self):
        try:
            text = "This is text with a ![rick rollhttps://i.imgur.com/aKaOqIh.gif)"
            print(f"extract_markdown_images(text) fishing for error*** === {extract_markdown_images(text)}")
        except Exception as e:
            print()
            print(f"Error from EXTRACT test_error_on_purpose === {e}")
            print()

    def test_split_nodes_image(self):
        node = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif): This is text with an image link: ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",TextType.NORMAL,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(": This is text with an image link: ", TextType.NORMAL),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            new_nodes
        )

    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.NORMAL,)
        new_nods = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ],
            new_nods
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_text_nodes_1(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes=text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
                            )
        
    def test_text_to_text_nodes_2(self):
        text = "This is **bold word** with another **bold word** and that is it."
        new_nodes=text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("bold word", TextType.BOLD),
                TextNode(" with another ", TextType.NORMAL),
                TextNode("bold word", TextType.BOLD),
                TextNode(" and that is it.", TextType.NORMAL)
            ],
            new_nodes
                            )
        
    def test_text_to_text_nodes_3(self):
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg): This example starts with an image and ends with a **bold word**"
        new_nodes=text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(": This example starts with an image and ends with a ", TextType.NORMAL),
                TextNode("bold word", TextType.BOLD)
            ],
            new_nodes
                            )
        
    def test_text_to_text_nodes_4(self):
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) - This example starts with an image and ends with a link: [link](https://boot.dev)"
        new_nodes=text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" - This example starts with an image and ends with a link: ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ],
            new_nodes
                            )

    def test_text_to_text_nodes_5(self):
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)![another obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)crazy test**bold word**`code block`"
        new_nodes=text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode("another obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode("crazy test", TextType.NORMAL),
                TextNode("bold word", TextType.BOLD, None),
                TextNode("code block", TextType.CODE, None)
            ],
            new_nodes
                            )

if __name__ == "__main__":
    unittest.main()
