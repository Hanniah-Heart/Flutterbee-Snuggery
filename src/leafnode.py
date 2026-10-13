from htmlnode import *

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props: dict[str, str] = None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("All leaf nodes must have a value")
		if self.tag is None:
			return self.value
		if self.props is not None:
			outProps = ""
			for prop in self.props:
				outProps+=f" {prop}={self.props[prop]}"
			return f"<{self.tag}{outProps}>{self.value}</{self.tag}>"
		return f"<{self.tag}>{self.value}</{self.tag}>"

	def __repr__(self):
		return f"HTMLNode(tag:'{self.tag}', value:'{self.value}', props:{self.props})"

	def __eq__(self, other):
		return self.tag == other.tag and self.value == other.value and self.props ==  other.props
