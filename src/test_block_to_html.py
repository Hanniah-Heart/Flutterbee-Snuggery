import unittest
from block_to_html import *

class TestBlockToHTML(unittest.TestCase):
	def test_bth_1(self):
		# this should confirm whether or not the basic function even works
#		print("running test_bth_1")
		markdown = """# This is a heading"""
		output = markdown_to_html_node(markdown)
		comparison = ParentNode("div", ParentNode("h1", LeafNode(None, "This is a heading")))
#		print(f"\noutput is...{output}\n\n")
#		print(f"comparison is...{comparison}\n\n")
		self.assertEqual(output, comparison)
#		print("done with test_bth_1"

	def test_bth_class_paragraphs(self):
		# this should confirm whether or not we have a complete flow from markdown to an html string
		md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
		node = markdown_to_html_node(md)
#		compareNode = ParentNode("div", [ParentNode("p", [LeafNode(None, "This is "), LeafNode("b", "bolded"), LeafNode("p"
		html = node.to_html()
#		print(f"\nhtml is...{html}\n")
#		print(f"\n<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>\n")
		self.assertEqual(
			html,
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
		)

	def test_bth_class_codeblock(self):
		md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		comparison = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
#		print(f"html is...{html}\n")
#		print(f"comparison is...{comparison}\n")
		self.assertEqual(
			html,
			comparison,
		)

	def test_bth_codeblock_failed_separation(self):
		md = """
```
This is the first codeblock.
``````
This is a failed codeblock separation because it doesn't have enough newlines between them.```
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		comparison = "<div><pre><code>This is the first codeblock.\n``````\nThis is a failed codeblock separation because it doesn't have enough newlines between them.</code></pre></div>"
#		print(f"html is...{html}\n")
#		print(f"comparison is...{comparison}\n")
		self.assertEqual(
			html,
			comparison,
		)

	def test_bth_codeblock(self):
		md = """
```
This is the first codeblock again.```

```
This is a second codeblock for real.```

"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		comparison = "<div><pre><code>This is the first codeblock again.</code></pre><pre><code>This is a second codeblock for real.</code></pre></div>"
#		print(f"html is...{html}\n")
#		print(f"comparison is...{comparison}\n")
		self.assertEqual(
			html,
			comparison,
		)

	def test_bth_headings(self):
		md = """


####### This is a paragraph since it's 7 #'s.

## This is a heading 2.

# This is a heading 1.

### 3

#### 4

##### This has **bold text** in the heading 5.
I'm part of heading 5.

###### 6"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		comparison = r"<div><p>####### This is a paragraph since it's 7 #'s.</p><h2>This is a heading 2.</h2><h1>This is a heading 1.</h1><h3>3</h3><h4>4</h4><h5>This has <b>bold text</b> in the heading 5. I'm part of heading 5.</h5><h6>6</h6></div>"
#		print(f"html is...{html}\n")
#		print(f"comparison is...{comparison}\n")
		self.assertEqual(
			html,
			comparison,
		)

	def test_bth_unordered_list(self):
#		print("starting bth unordered list test")
		md = """- An unordered list has started
- and continues
- this one finishes but

- Another one starts!
- This one has `code`, **bold**, and _italic_ text!"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		comparison = r"<div><ul><li>An unordered list has started</li><li>and continues</li><li>this one finishes but</li></ul><ul><li>Another one starts!</li><li>This one has <code>code</code>, <b>bold</b>, and <i>italic</i> text!</li></ul></div>"
#		print(f"html is...{html}\n")
#		print(f"comparison is...{comparison}\n")
		self.assertEqual(
			html,
			comparison,
		)

	def test_bth_ordered_list(self):
		md = """1. Order (You mean welfare and workers' rights?)
2. Freedom (You've shown you mean trade...)
3. Autocracy (At least we agree here)

1. Games that had weird renames of communism that massively misinterpret the point"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		comparison = r"<div><ol><li>Order (You mean welfare and workers' rights?)</li><li>Freedom (You've shown you mean trade...)</li><li>Autocracy (At least we agree here)</li></ol><ol><li>Games that had weird renames of communism that massively misinterpret the point</li></ol></div>"
#		print(f"html is...{html}\n")
#		print(f"comparison is...{comparison}\n")
		self.assertEqual(
			html,
			comparison,
		)

	def test_bth_quote(self):
		md = """>We hold these truths to be self evident, that all men are created equal,
>that they are endowed by their creator with certain unalienable rights,
>that among these are life, liberty, and the pursuit of happiness

> Quotes right wingers would be surprised we communists mostly love"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		comparison = r"<div><blockquote>We hold these truths to be self evident, that all men are created equal, that they are endowed by their creator with certain unalienable rights, that among these are life, liberty, and the pursuit of happiness</blockquote><blockquote>Quotes right wingers would be surprised we communists mostly love</blockquote></div>"
#		print(f"html is...{html}\n")
#		print(f"comparison is...{comparison}\n")
		self.assertEqual(
			html,
			comparison,
		)

	def test_bth_all(self):
		md = """# heading**b**_i_`c`end

paragraph**b**_i_`c`end

```
code**b**_i_`c`end```

- unordered list**b**_i_`c`end

1. ordered list**b**_i_`c`end

> quote **b**_i_`c`end


"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		comparison = r"<div><h1>heading<b>b</b><i>i</i><code>c</code>end</h1><p>paragraph<b>b</b><i>i</i><code>c</code>end</p><pre><code>code**b**_i_`c`end</code></pre><ul><li>unordered list<b>b</b><i>i</i><code>c</code>end</li></ul><ol><li>ordered list<b>b</b><i>i</i><code>c</code>end</li></ol><blockquote>quote <b>b</b><i>i</i><code>c</code>end</blockquote></div>"
#		print(f"html is...{html}\n")
#		print(f"comparison is...{comparison}\n")
		self.assertEqual(
			html,
			comparison,
		)
