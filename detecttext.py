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

def categorize_by_box_size(text_blocks):
    # Initialize variables to store the main text
    title = ""
    author = ""
    publisher = ""
    other = ""
    
    # Calculate the average bounding box size
    avg_box_size = np.mean([((bbox[2][0] - bbox[0][0]) * (bbox[2][1] - bbox[0][1])) for (bbox, _, _) in text_blocks])

    # Now check each bounding box's area and categorize based on size
    for (bbox, text, prob) in text_blocks:
        # Calculate the area of the current bounding box
        width = bbox[2][0] - bbox[0][0]
        height = bbox[2][1] - bbox[0][1]
        area = width * height

        # Categorize based on box area size relative to the average box size
        if area > avg_box_size * 1.2:  # 1.5x the average area as a threshold for "larger" boxes
            # Assuming larger boxes are the title
            # if len(title) < len(text):  # Prefer the longest text as the title
            title += (text + " ")
        elif "??" in text or "??" in text:
            # If the text contains "author" keywords, it's likely the author
            author += (text + " ")
        elif "???" in text or "??" in text:
            # If the text contains "publisher" keywords, it's likely the publisher
            publisher += (text + " ")
        else:
            # If the text doesn't fit into the categories above, consider it as potential author or other info
            if len(author) == 0:
                author += (text + " ")
            elif len(publisher) == 0:
                publisher += (text + " ")
            else:
                other += text + " "  # Accumulate other text into a single string

    return title, author, publisher, other

def show_textregion(image, result):
    combined_text = ""
    text_blocks = []
    


    # Filter out non-Japanese text blocks
    text_blocks = remove_non_japanese(text_blocks)
    
    # Categorize the text blocks based on their box size
    title, author, publisher, other = categorize_by_box_size(text_blocks)
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Publisher: {publisher}")
    print(f"Other: {other}")
    
    print(f"Combined Text: {combined_text}")
    
    return title, author, publisher, other, combined_text