import os
import cv2
import easyocr  # Import EasyOCR

# Initialize EasyOCR Reader
reader = easyocr.Reader(['ja'])  # ['en'] for English language (you can add more languages if needed)

# Specify the folder path
folder_path = './output/clip/'  # Replace with your folder path

# List all files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

# Get the full path for each image
image_paths = [os.path.join(folder_path, f) for f in image_files]

# Print the list of image paths
print(image_paths)


