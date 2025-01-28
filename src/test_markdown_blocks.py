import unittest

from markdown_blocks import (
markdown_to_blocks, 
block_to_block_type,
markdown_to_html_node,
block_type_paragraph,
block_type_heading,
block_type_code,
block_type_quote,
block_type_ulist,
block_type_olist)

class TestSplitMarkdown(unittest.TestCase):
    def test_split_markdown_block3(self):
        markdown_text = """
# This is heading

Normal paragraph

Normal paragraph
"""
        list_markdown = markdown_to_blocks(markdown_text)
        self.assertEqual(
            ["# This is heading",
             "Normal paragraph",
             "Normal paragraph"], list_markdown
        )

    def test_split_markdown_block4(self):
        markdown_text = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown_text)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type_heading6(self):
        markdown_block = """###### This is a Heading 6"""

        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_heading6_tricky(self):
        markdown_block = """# # This is a Heading 6"""

        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_heading5(self):
        markdown_block = """##### This is a Heading 5"""

        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_heading4(self):
        markdown_block = """#### This is a Heading 4"""

        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_heading3(self):
        markdown_block = """### This is a Heading 3"""

        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_heading2(self):
        markdown_block = """## This is a Heading 2"""

        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_heading1(self):
        markdown_block = """# This is a Heading 1"""

        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_unordered_list(self):
        markdown_block = """* Item 1
* Item 2
* Item 3"""
        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_ulist)

    def test_block_to_block_type_unordered_list_tricky(self):
        markdown_block = """* *Item* 1
* Item 2
* Item 3"""
        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_ulist)

    def test_block_to_block_type_ordered_list_tricky(self):
        markdown_block = """1. 1 Para Vencer
2. 2Second item
3. Third item"""
        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_olist)

    def test_block_to_block_type_quote(self):
        markdown_block = """> This is a blockquote.
> It can span multiple lines or paragraphs.
>
> You can even nest blockquotes:
> > This is a nested blockquote."""
        block_type = block_to_block_type(markdown_block)
        self.assertEqual(block_type, block_type_quote)

    def test_block_to_block_types_all(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_code(self):
        md = """```code_code_code```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>code_code_code</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )   

if __name__ == "__main__":
    unittest.main()



