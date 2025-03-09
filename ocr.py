from manga_ocr import MangaOcr

mocr = MangaOcr()
import os
import cv2
# mocrtext = mocr(cropped_path)



# Specify the folder path
folder_path = './output/clip/'  # Replace with your folder path

# List all files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]


