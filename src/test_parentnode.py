import unittest
from parentnode import *
from leafnode import *

class TestParentNode(unittest.TestCase):
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>"
		)

	def test_to_html_with_aunkcles(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		second_child_node = LeafNode("a", "2nd child")
		parent_node = ParentNode("div", [child_node, second_child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span><a>2nd child</a></div>"
		)

	def test_to_html_childless_parent(self):
		parent_node = ParentNode("div", [])
		self.assertRaisesRegex(ValueError, "All parent nodes must have children", parent_node.to_html)

	def test_to_html_tagless_parent(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("", [child_node])
		self.assertRaisesRegex(ValueError, "All parent nodes must have a tag", parent_node.to_html)
