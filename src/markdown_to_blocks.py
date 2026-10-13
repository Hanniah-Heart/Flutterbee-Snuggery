def markdown_to_blocks(markdown: str) -> list[str]:
#	print(f"markdown is...{markdown}")
	blocks = markdown.split("\n\n")
	newBlocks = []
	for block in blocks:
		block = block.strip()
		block = block.lstrip("\n")
		block = block.rstrip("\n")
		if block == "":
			continue
		newBlocks.append(block)
	return newBlocks
