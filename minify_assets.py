import re
import os

def minify_js(content):
    # Remove comments
    content = re.sub(r'//.*', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove whitespace
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{}();,:])\s*', r'\1', content)
    return content.strip()

def minify_css(content):
    # Remove comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove whitespace
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{}();,:])\s*', r'\1', content)
    return content.strip()

def process_files():
    base_dir = "/Users/joaowendt/Documents/GitHub/website"
    
    # Minify JS
    js_path = os.path.join(base_dir, "main.js")
    if os.path.exists(js_path):
        with open(js_path, 'r') as f:
            js_content = f.read()
        min_js = minify_js(js_content)
        with open(os.path.join(base_dir, "main.min.js"), 'w') as f:
            f.write(min_js)
        print("Minified main.js")

    # Minify CSS
    css_path = os.path.join(base_dir, "style.css")
    if os.path.exists(css_path):
        with open(css_path, 'r') as f:
            css_content = f.read()
        min_css = minify_css(css_content)
        with open(os.path.join(base_dir, "style.min.css"), 'w') as f:
            f.write(min_css)
        print("Minified style.css")

if __name__ == "__main__":
    process_files()
