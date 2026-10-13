import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_different_text(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a different text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_different_type(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_both_different(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a different text node", TextType.TEXT)
		self.assertNotEqual(node, node2)

	def test_url_different(self):
		node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_url_extra_none(self):
		node = TextNode("This is a text node", TextType.BOLD, None)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_different_urls(self):
		node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
		node2 = TextNode("This is a text node", TextType.BOLD, "https://noai.duckduckgo.com")
		self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
