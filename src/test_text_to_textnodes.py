import unittest
from text_to_textnodes import *

class TestTextToTextNodes(unittest.TestCase):
	def test_t2tn_class(self):
		text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		out = text_to_textnodes(text)
		expected = [
		    TextNode("This is ", TextType.TEXT),
		    TextNode("text", TextType.BOLD),
		    TextNode(" with an ", TextType.TEXT),
		    TextNode("italic", TextType.ITALIC),
		    TextNode(" word and a ", TextType.TEXT),
		    TextNode("code block", TextType.CODE),
		    TextNode(" and an ", TextType.TEXT),
		    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
		    TextNode(" and a ", TextType.TEXT),
		    TextNode("link", TextType.LINK, "https://boot.dev"),
		]
		self.assertEqual(out, expected)
