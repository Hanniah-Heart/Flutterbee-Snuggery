def extract_title(markdown):
	title = None
	for line in markdown.splitlines():
		if line.startswith("# "):
			title = line
			break
	if title is None:
		raise Exception("no title in input")
	return (title.lstrip("# ")).lstrip()
