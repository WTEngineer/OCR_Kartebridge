import easyocr
import cv2
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import re
import mangarecog

output_dir = Path('./output/cropped_images')
output_dir.mkdir(parents=True, exist_ok=True)

font_path = './font/NotoSansCJK-Regular.ttc'

reader = easyocr.Reader(['ja'])

def display_japanese_text(image, text, position, font_path, font_size=20):
    # Convert OpenCV image (BGR) to PIL image (RGB)
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(image_pil)

    # Draw the text on the image
    draw.text(position, text, font=font, fill=(255, 0, 0))  # Green text color

    # Convert back to OpenCV image (RGB to BGR)
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    return image

def detect_text(image_path):
    result = reader.readtext(image_path)
    return result

def is_japanese(text):
    # Regular expression to match Hiragana, Katakana, Kanji, and Japanese punctuation
    pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF66-\uFF9F\u3000-\u303F]+')
    return bool(pattern.search(text))

def remove_non_japanese(text_blocks):
    # Filter out any non-Japanese text blocks
    japanese_text_blocks = []
    
    for (bbox, text, prob) in text_blocks:
        # Check if the text block is Japanese
        if is_japanese(text):
            japanese_text_blocks.append((bbox, text, prob))
        else:
            print(f"Removed non-Japanese text: {text}")  # Optional: print or log non-Japanese text

    return japanese_text_blocks

