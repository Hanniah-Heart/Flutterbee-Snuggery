from markdown_to_blocks import *
from htmlnode import *
from textnode import *
from split_nodes_delimiter import *
from leafnode import *
from parentnode import *
from blocktypes import *
import re

def markdown_to_html_node(markdown) -> ParentNode:
	blocks = markdown_to_blocks(markdown)
	parentBlocks = []
	for block in blocks:
		match block_to_block_type(block):
			case BlockType.CODE:
				block = block.lstrip("` \n")
				block = block.rstrip("` ")
				parent = ParentNode("pre", [LeafNode("code", block)])
				parentBlocks.append(parent)
			case BlockType.PARAGRAPH:
				block = " ".join(block.splitlines())
				nodes = [TextNode(block, TextType.TEXT)]
				nodes = split_nodes_all(nodes)
				parentBlocks.append(ParentNode("p", nodes))
				continue
			case BlockType.HEADING:
				block = " ".join(block.splitlines())
				nodes = [TextNode(block, TextType.TEXT)]
				nodes = split_nodes_all(nodes)
				poundCount = str(len(re.match(r"#{1,6} ", block)[0])-1)
				nodes[0].value = nodes[0].value.lstrip("# ")
				parentBlocks.append(ParentNode("h"+poundCount, nodes))
				continue
			case BlockType.ORDERED_LIST:
				lineNodes = []
				for line in block.splitlines():
					matched = re.match(r"\d\. ", line)[0]
					bulletless = line.lstrip(matched)
					segmentNodes = split_nodes_all([TextNode(bulletless, TextType.TEXT)])
					lineNodes.append(ParentNode("li", segmentNodes))
				parentBlocks.append(ParentNode("ol", lineNodes))
				continue
			case BlockType.UNORDERED_LIST:
				lineNodes = []
				for line in block.splitlines():
					segmentNodes = split_nodes_all([TextNode(line.lstrip("- "), TextType.TEXT)])
					lineNodes.append(ParentNode("li", segmentNodes))
				parentBlocks.append(ParentNode("ul", lineNodes))
				continue
			case BlockType.QUOTE:
				lines = []
				for line in block.splitlines():
					lines.append((line.lstrip(">")).lstrip(" "))
				line = " ".join(lines)
				nodes = split_nodes_all([TextNode(line, TextType.TEXT)])
				parentBlocks.append(ParentNode("blockquote", nodes))
	return ParentNode("div", parentBlocks)
