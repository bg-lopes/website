import os
from PIL import Image

def convert_to_webp(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            img = Image.open(filepath)
            
            # Create WebP filename
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_filepath = os.path.join(directory, webp_filename)
            
            # Save as WebP
            img.save(webp_filepath, 'webp', quality=80)
            print(f"Converted {filename} to {webp_filename}")

if __name__ == "__main__":
    assets_dir = "/Users/joaowendt/Documents/GitHub/website/assets"
    convert_to_webp(assets_dir)
