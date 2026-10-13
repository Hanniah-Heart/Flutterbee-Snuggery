import unittest
from split_nodes_delimiter import *

class TestSplitNodesExtractable(unittest.TestCase):
	def test_split_nodes_image_1(self):
		one = TextNode("a![b](c)d![e](f)", TextType.TEXT)
		old_nodes = [one]
		splitNodes = split_nodes_image(old_nodes)
		self.assertEqual(str(splitNodes), "[TextNode(a, TextType.TEXT, None), TextNode(b, TextType.IMAGE, c), TextNode(d, TextType.TEXT, None), TextNode(e, TextType.IMAGE, f)]")

	def test_no_pretext_link(self):
		old = [TextNode("[a](b)c", TextType.TEXT)]
		splitnodes = split_nodes_link(old)
		self.assertEqual(str(splitnodes), "[TextNode(a, TextType.LINK, b), TextNode(c, TextType.TEXT, None)]")

	def test_extactable_link_only(self):
		old = [TextNode("[a](b)", TextType.TEXT)]
		splitnodes = split_nodes_link(old)
		self.assertEqual(str(splitnodes), "[TextNode(a, TextType.LINK, b)]")

	def test_extractable_image_only(self):
		old = [TextNode("![a](b)", TextType.TEXT)]
		splitnodes = split_nodes_image(old)
		self.assertEqual(str(splitnodes), "[TextNode(a, TextType.IMAGE, b)]")

	def test_extractable_mismatch(self):
		old = [TextNode("![a](b)", TextType.TEXT)]
		splitnodes = split_nodes_link(old)
		self.assertEqual(str(splitnodes), "[TextNode(![a](b), TextType.TEXT, None)]")

	def test_extractable_nested(self):
		old = [TextNode("[a](b)![c](d)", TextType.TEXT)]
		splitnodes = split_nodes_image(split_nodes_link(old))
		self.assertEqual(str(splitnodes), "[TextNode(a, TextType.LINK, b), TextNode(c, TextType.IMAGE, d)]")

	def test_extractable_nested_2(self):
		old = [TextNode("[a](b)![c](d)", TextType.TEXT)]
		splitnodes = split_nodes_link(split_nodes_image(old))
		self.assertEqual(str(splitnodes), "[TextNode(a, TextType.LINK, b), TextNode(c, TextType.IMAGE, d)]")

