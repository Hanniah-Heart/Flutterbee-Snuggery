import os
import sys
import shutil
from block_to_html import *
from generate_page import *

def main():
	print("starting...")
	basepath = "/"
	if len(sys.argv) > 1:
		basepath = sys.argv[1]
	shutil.rmtree("docs")
	os.mkdir("docs")
	replace_file_tree("static", "docs")
	generate_pages("content", "template.html", "docs", basepath)

def replace_file_tree(source: str, destination: str):
	if not os.path.exists(source):
		return
	if os.path.isfile(source):
		os.makedirs(os.path.dirname(destination), exist_ok=True)
		shutil.copy(source, destination)
		return
	if not os.path.isdir(source) and not os.path.isfile(path):
		raise Exception(f"Source is not a file nor a directory. Source is {source}\n")
	children = os.listdir(source)
	for child in children:
		replace_file_tree(source+"/"+child, destination+"/"+child)

def generate_pages(from_path, template_path, dest_path, basepath):
	print(f"Generating all pages from {from_path} to {dest_path} use {template_path}")
	children = os.listdir(from_path)
	for child in children:
		new = from_path+"/"+child
		if os.path.isdir(new):
			generate_pages(new, template_path, dest_path+"/"+child, basepath)
		elif child == "index.md":
			generate_page(new, template_path, dest_path+"/"+"index.html", basepath)
		else:
			 raise Exception("Unexpected File Type")

def generate_page(from_path, template_path, dest_path, basepath):
	print(f"Generating page from {from_path} to {dest_path} use {template_path}")
	f = open(from_path).read()
	t = open(template_path).read()
	html = markdown_to_html_node(f)
	content = html.to_html()
	title = extract_title(f)
	t = t.replace("{{ Title }}", title)
	t = t.replace("{{ Content }}", content)
	t = t.replace('href="/', f'href="{basepath}')
	t = t.replace('src="/', f'src="{basepath}')
	t = t.replace('src=/', f'src={basepath}')
	t = t.replace('href=/', f'href={basepath}')
	os.makedirs(os.path.dirname(dest_path), exist_ok=True)
	(open(dest_path, mode='w')).write(t)



main()
