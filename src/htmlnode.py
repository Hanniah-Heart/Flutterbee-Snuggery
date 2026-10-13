class HTMLNode:
	def __init__(self, tag: str = None, value: str = None, children: list[str | HTMLNode] | None  = None, props: dict[str, str] = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if self.props is None or self.props == {}:
			return ""
		out = ""
		for key in self.props:
			out+=f" '{key}'='{self.props[key]}'"
		return out

	def __repr__(self):
		return f"HTMLNode(tag:'{self.tag}', value:'{self.value}', children:{self.children}, props:{self.props})"

	def __eq__(self, other):
		samechildren = True
		if self.children:
#			print(f"self.children are...{self.children}")
			if other.children:
#				print(f"other.children are...{other.children}")
				for child in self.children:
#					print(f"child is {child}")
					if child not in other.children:
						samechildren = False
				for child in other.children:
#					print(f"child is {child}")
					if child not in self.children:
						samechildren = True
			else:
				samechildren = False
		elif other.children:
			samechildren = False
		return self.tag == other.tag and self.value == other.value and samechildren and self.props == other.props

