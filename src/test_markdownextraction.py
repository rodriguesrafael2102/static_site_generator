import unittest

from gencontent import extract_title

class TestMarkDown(unittest.TestCase):
    def test_markdown_extraction1(self):
        markdown_text = """
this is an h1

this is how an h1 is in html:

# This is a h1 title in html

## this is an h2
"""
        h1_text = extract_title(markdown_text)
        self.assertEqual(
            h1_text,
            "This is a h1 title in html",
        )

    def test_markdown_extraction2(self):
        markdown_text = """
# this is an h1

this is how an h1 is in html: # This is a h1 title in html

## this is an h2
"""
        h1_text = extract_title(markdown_text)
        self.assertEqual(
            h1_text,
            "this is an h1",
        )


if __name__ == "__main__":
    unittest.main()
