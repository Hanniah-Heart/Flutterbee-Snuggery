import unittest
from blocktypes import *
from markdown_to_blocks import *

class TestBlockTypes(unittest.TestCase):
	def test_BT_paragraph(self):
		markdown = """



this is a paragraph one"""
		blocks = markdown_to_blocks(markdown)
		for block in blocks:
			type = block_to_block_type(block)
			self.assertEqual(type, BlockType.PARAGRAPH)


	def test_BT_code_and_paragraph(self):
#		print("Running test_BT_code_and_paragraph")
		markdown = """



this is a paragraph two

```
this is code three
```
"""
		blocks = markdown_to_blocks(markdown)
#		print(f"blocks for test_BT_code_and_paragraph are...{blocks}")
		for i in range(len(blocks)):
#			print(f"in BTcandp, i is...{i}...and blocks[i] is...{blocks[i]}(End of block reveal)")
			type = block_to_block_type(blocks[i])
			if i in [0]:
#				print(f"in BTcandp, {i} is 0")
				self.assertEqual(type, BlockType.PARAGRAPH)
			if i in [1]:
#				print(f"in BTcandp, {i} is 1")
				self.assertEqual(type, BlockType.CODE)

	def test_BT_every_type_twice_or_more(self):
		markdown = """
paragraph A
paragraph A+1/2

paragraph B

```
Code C```

# heading D
## Heading D2

### Heading E

#### Heading F

##### Heading G

###### Heading H

####### No longer a heading I

> Quote J

> Quote K
> Quote K2

- Unordered List L

- Unordered List M
- Unordered List M2

1. Ordered List N
2. Ordered List N2

1. Ordered List O

```
Code? P```
"""
		blocks = markdown_to_blocks(markdown)
#		print(f"blocks for BTtest3 are...{blocks}")
		for i in range(len(blocks)):
			type = block_to_block_type(blocks[i])
#			print(f"in BTtest3, i is...{i}...and blocks[i] is...{blocks[i]}... and type is...{type}(end of block reveal)")
			if i in [0, 1, 8]:
				self.assertEqual(type, BlockType.PARAGRAPH)
			if i in [2, 15]:
				self.assertEqual(type, BlockType.CODE)
			if i in [3, 4, 5, 6, 7]:
				self.assertEqual(type, BlockType.HEADING)
			if i in [9, 10]:
				self.assertEqual(type, BlockType.QUOTE)
			if i in [11, 12]:
				self.assertEqual(type, BlockType.UNORDERED_LIST)
			if i in [13, 14]:
				self.assertEqual(type, BlockType.ORDERED_LIST)
