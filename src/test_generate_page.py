import unittest
from generate_page import *

class TestGeneratePage(unittest.TestCase):
	def test_extract_title(self):
		md = """Not the title

# Title

# Still not the title"""
		self.assertEqual(extract_title(md), "Title")

	def test_extract_title_fail(self):
		md = "No"
		self.assertRaisesRegex(Exception, "no title in input", extract_title, md)
