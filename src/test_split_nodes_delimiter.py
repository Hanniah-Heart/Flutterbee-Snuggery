import unittest
from split_nodes_delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
	def test_single_bold(self):
		first_node = TextNode("The word **bold** should be a bold node.", TextType.TEXT)
		old_nodes = [first_node]
		new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
		self.assertEqual(str(new_nodes), "[TextNode(The word , TextType.TEXT, None), TextNode(bold, TextType.BOLD, None), TextNode( should be a bold node., TextType.TEXT, None)]")

	def test_multiple_bold(self):
		first_node = TextNode("The word **bold** should be a bold node.", TextType.TEXT)
		second_node = TextNode("Apples **DO** grow on trees.", TextType.TEXT)
		old_nodes=[first_node, second_node]
		expected = [
			TextNode("The word ", TextType.TEXT),
			TextNode("bold", TextType.BOLD),
			TextNode(" should be a bold node.", TextType.TEXT),
			TextNode("Apples ", TextType.TEXT),
			TextNode("DO", TextType.BOLD),
			TextNode(" grow on trees.", TextType.TEXT)
		]
		new_nodes = split_nodes_delimiter(old_nodes, TextType.BOLD.value, TextType.BOLD)
		self.assertEqual(new_nodes, expected)

	def test_single_italic(self):
		first_node = TextNode("The word _italic_ should be a italic node.", TextType.TEXT)
		old_nodes = [first_node]
		new_nodes = split_nodes_delimiter(old_nodes, TextType.ITALIC.value, TextType.ITALIC)
		self.assertEqual(str(new_nodes), "[TextNode(The word , TextType.TEXT, None), TextNode(italic, TextType.ITALIC, None), TextNode( should be a italic node., TextType.TEXT, None)]")

	def test_unclosed_delimiters(self):
		node = TextNode("This shouldn't work `did it?", TextType.TEXT)
		old_nodes = [node]
		self.assertRaisesRegex(Exception, "Invalid Markdown Syntax: Uneven number of delimiters in node text", split_nodes_delimiter, old_nodes, TextType.CODE.value, TextType.CODE)

