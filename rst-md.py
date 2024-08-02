import os
from docutils.core import publish_string
import markdownify

def rst_to_md(rst_content):
    html_content = publish_string(rst_content, writer_name='html')
    md_content = markdownify.markdownify(html_content.decode('utf-8'), heading_style="ATX")
    return md_content

def convert_files():
    for filename in os.listdir('.'):
        if filename.endswith('.rst'):
            with open(filename, 'r', encoding='utf-8') as rst_file:
                rst_content = rst_file.read()
            md_content = rst_to_md(rst_content)
            with open(filename.replace('.rst', '.md'), 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)
            print(f"Converted {filename} to {filename.replace('.rst', '.md')}")

if __name__ == "__main__":
    convert_files()
