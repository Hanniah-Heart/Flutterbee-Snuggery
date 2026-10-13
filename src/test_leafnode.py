import unittest
from leafnode import *


class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Hello, world!")
		self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

	def test_leaf_eq(self):
		node = LeafNode("a", "Hello, world!")
		node2 = LeafNode("a", "Hello, world!")
		self.assertEqual(node, node2)

	def test_leaf_to_html_link(self):
		node = LeafNode("a", "Anchor Text Here", {"href": "https://www.boot.dev"})
		html = node.to_html()
#		print(html)
		self.assertEqual(html, "<a href=https://www.boot.dev>Anchor Text Here</a>")


if __name__ == "__main__":
	unittest.main()
