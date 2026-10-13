from enum import Enum
import re

class BlockType(Enum):
	PARAGRAPH=1
	HEADING=2
	CODE=3
	QUOTE=4
	UNORDERED_LIST=5
	ORDERED_LIST=6

def block_to_block_type(block) -> BlockType:
#	print(f"block is '{block}'.")
	if re.match(r"#{1,6} ", block):
		return BlockType.HEADING
	if block.startswith("```\n") and block.endswith("```"):
		return BlockType.CODE
	lines = block.splitlines()
#	print(f"lines are...{lines}.")
	for i in range(len(lines)):
		if not lines[i].startswith(">"):
			break
		if i+1 == len(lines):
			return BlockType.QUOTE
	for i in range(len(lines)):
		if not lines[i].startswith("- "):
			break
		if i+1 == len(lines):
			return BlockType.UNORDERED_LIST
	for i in range(len(lines)):
		check = re.match(r"(\d)\. ", lines[i])
		if check is None:
#			print("check is None.")
			break
		number = int(re.findall(r"\d", check[0])[0])
		if number != i+1:
#			print(f"number is...'{number}' which is not {i}+1.")
			break
		if i == len(lines)-1:
			return BlockType.ORDERED_LIST
	return BlockType.PARAGRAPH
