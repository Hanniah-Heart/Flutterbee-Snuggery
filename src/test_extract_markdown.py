import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
	def test_example_extract_image(self):
		exampleText = r"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4VkJRm4Vk.jpeg)"
		self.assertEqual("[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4VkJRm4Vk.jpeg')]",str(extract_markdown_images(exampleText)))

	def test_example_extract_link(self):
		exampleText = r"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		self.assertEqual(str(extract_markdown_links(exampleText)),"[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]")

	def test_link_and_image(self):
		twitch_pfp = r"https://static-cdn.jtvnw.net/jtv_user_pictures/a4e4ec2c-a0da-4a73-af04-fee192a23232-profile_image-70x70.png"
		text = f"Normally [Hanniah](https://www.boot.dev/u/hanniahheart) looks like this.![red headed girl with glasses in a green shirt]({twitch_pfp})"
		self.assertEqual(f"[('Hanniah', 'https://www.boot.dev/u/hanniahheart')][('red headed girl with glasses in a green shirt', '{twitch_pfp}')]", str(extract_markdown_links(text))+str(extract_markdown_images(text)))

