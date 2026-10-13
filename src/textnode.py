from enum import Enum
from leafnode import *

class TextType(Enum):
	TEXT = ""
	BOLD = "**"
	ITALIC = "_"
	CODE = "`"
	LINK = "[anchor text](url)"
	IMAGE = "![alt text](url)"

class TextNode:
	def __init__(self, text, text_type, url = None):
		self.text: str = text
		self.text_type: TextType = text_type
		self.url: str = url

	def __eq__(self, other) -> bool:
		return self.text == other.text and self.text_type == other.text_type and self.url == other.url

	def __repr__(self) -> str:
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
	if text_node.text_type not in TextType:
		raise Exception("The target text node has an illegal text type")
	match text_node.text_type:
		case TextType.TEXT:
			return LeafNode(None, text_node.text)
		case TextType.BOLD:
			return LeafNode("b", text_node.text)
		case TextType.ITALIC:
			return LeafNode("i", text_node.text)
		case TextType.CODE:
			return LeafNode("code", text_node.text)
		case TextType.LINK:
			return LeafNode("a", text_node.text, {"href":text_node.url})
		case TextType.IMAGE:
			return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
