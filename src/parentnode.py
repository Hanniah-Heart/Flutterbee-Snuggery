from htmlnode import *

class ParentNode(HTMLNode):
	def __init__(self, tag: str, children: list[str | HTMLNode], props: dict[str, str] = None):
		if not isinstance(children, list):
			children = [children]
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag is None or self.tag == "":
			raise ValueError("All parent nodes must have a tag")
		if self.children is None or self.children == []:
			raise ValueError("All parent nodes must have children")
		out=f"<{self.tag}>"
		for child in self.children:
			out+=child.to_html()
		out+=f"</{self.tag}>"
		return out

	def __eq__(self, other):
		samechildren = True
		if self.children and isinstance(self.children, list):
			if other.children and isinstance (other.children, list):
				for child in self.children:
					if child not in other.children:
						samechildren = False
				for child in other.children:
					if child not in self.children:
						samechildren = False
			else:
				samechildren = False
		elif other.children:
			samechildren = False
		return self.tag == other.tag and samechildren and self.props == other.props
