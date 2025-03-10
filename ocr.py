from manga_ocr import MangaOcr

mocr = MangaOcr()
import os
import cv2
# mocrtext = mocr(cropped_path)



# Specify the folder path
folder_path = './output/clip/'  # Replace with your folder path

# List all files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

# Get the full path for each image
image_paths = [os.path.join(folder_path, f) for f in image_files]

# Print the list of image paths
print(image_paths)

# Loop through each image path and process
for image_path in image_paths:
    # # Read the image
    # img = cv2.imread(image_path)
    
    # if img is None:
    #     print(f"Error: Unable to load image {image_path}")
    #     continue  # Skip this image if it couldn't be loaded
    
    mocrtext = mocr(image_path)
    
    print(f"Text result is {image_path} - {mocrtext}:")
