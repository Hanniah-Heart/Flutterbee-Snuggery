from textnode import *
from extract_markdown import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		texts = node.text.split(delimiter)
		if len(texts) % 2 == 0:
			raise Exception(f"Invalid Markdown Syntax: Uneven number of delimiters in node text. The list of texts detected are {texts} and the delimiter in use is {delimiter}")
		for i in range(len(texts)):
			if i%2==0:
				new_nodes.append(TextNode(texts[i], TextType.TEXT))
			else:
				new_nodes.append(TextNode(texts[i], text_type))
	return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		images = extract_markdown_images(node.text)
		for image in images:
			texts = node.text.split(f"![{image[0]}]({image[1]})", maxsplit=1)

			if len(texts[0]):
				pretextNode = TextNode(texts[0], TextType.TEXT)
				new_nodes.append(pretextNode)

			imageNode = TextNode(image[0], TextType.IMAGE, image[1])
			new_nodes.append(imageNode)

			remainingNode = TextNode(texts[1], TextType.TEXT)
			node.text = remainingNode.text
		if len(node.text):
			new_nodes.append(TextNode(node.text, TextType.TEXT))
	return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		links = extract_markdown_links(node.text)
		for link in links:
			texts = node.text.split(f"[{link[0]}]({link[1]})", maxsplit=1)

			if len(texts[0]):
				pretextNode = TextNode(texts[0], TextType.TEXT)
				new_nodes.append(pretextNode)

			linkNode = TextNode(link[0], TextType.LINK, link[1])
			new_nodes.append(linkNode)

			remainingNode = TextNode(texts[1], TextType.TEXT)
			node.text = remainingNode.text
		if len(node.text):
			new_nodes.append(TextNode(node.text, TextType.TEXT))
	return new_nodes

def split_nodes_all(old_nodes: list[TextNode]) -> list[TextNode]:
	old_nodes = split_nodes_image(split_nodes_link(old_nodes))
	for tuple in [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]:
		old_nodes = split_nodes_delimiter(old_nodes, tuple[0], tuple[1])
	newnodes = []
	for node in old_nodes:
#		print(f"node before text_node_to_html_node is...{node}")
		node = text_node_to_html_node(node)
#		print(f"node after text_node_to_html_node is...{node}")
		newnodes.append(node)
	return newnodes
