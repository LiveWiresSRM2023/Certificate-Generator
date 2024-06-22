import os

# Get the current directory of this script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the font file relative to this script
FONT_FILE_PATH = os.path.join(base_dir, 'fonts', 'GreatVibes-Regular.ttf')

# Now you can use FONT_FILE_PATH in your code
print(FONT_FILE_PATH)  # This should print the correct path

# Example of using FONT_FILE_PATH
# from PIL import ImageFont
# font = ImageFont.truetype(FONT_FILE_PATH, size=24)
