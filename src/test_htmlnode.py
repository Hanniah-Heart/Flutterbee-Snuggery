import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
	def test_repr(self):
		node = HTMLNode('tag', 'value', ['child'], {'href': 'https://www.boot.dev',})
		representation = "HTMLNode(tag:'tag', value:'value', children:['child'], props:{'href': 'https://www.boot.dev'})"
		self.assertEqual(str(node), representation)

	def test_props_to_html(self):
		node = HTMLNode('tag', 'value', ['child'], {'href': 'https://www.boot.dev',})
		expected = " 'href'='https://www.boot.dev'"
		actual = node.props_to_html()
		self.assertEqual(expected, actual)

	def test_multiple_props_to_html(self):
		node = HTMLNode('tag', 'value', ['child'], {'href': 'https://www.boot.dev', 'fake': 'Fakity Fake'})
		expected = " 'href'='https://www.boot.dev' 'fake'='Fakity Fake'"
		actual = node.props_to_html()
		self.assertEqual(expected, actual)

	def test_eq(self):
		node = HTMLNode('tag', 'value', ['child'], {'href': 'https://www.boot.dev',})
		node2 = HTMLNode('tag', 'value', ['child'], {'href': 'https://www.boot.dev',})
		self.assertEqual(node, node2)

	def test_not_equal_props(self):
		node = HTMLNode('tag', 'value', ['child'], {'href': 'https://www.boot.dev/leaderboard',})
		node2 = HTMLNode('tag', 'value', ['child'], {'href': 'https://www.boot.dev',})
		self.assertNotEqual(node, node2)

	def test_not_equal_children(self):
		node = HTMLNode('tag', 'value', ['child', 'other child'], {'href': 'https://www.boot.dev',})
		node2 = HTMLNode('tag', 'value', ['child'], {'href': 'https://www.boot.dev',})
		self.assertNotEqual(node, node2)

if __name__ == "__main__":
	unittest.main()
