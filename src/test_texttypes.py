import unittest
from textnode import *


class TestTextType(unittest.TestCase):
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_bold(self):
		node = TextNode("This is a bolded text node", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is a bolded text node")
		self.assertEqual(html_node.to_html(), "<b>This is a bolded text node</b>")

	def test_img(self):
		node = TextNode("This is alt text", TextType.IMAGE, "https://fakeimage.png")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.props["src"], "https://fakeimage.png")
		self.assertEqual(html_node.props["alt"], "This is alt text")
		self.assertEqual(html_node.value, "")

