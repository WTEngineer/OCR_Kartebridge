import os
from pdf2image import convert_from_path

def pdf_to_image(pdf_path, output_format='PNG', dpi=200, output_prefix='output_page', poppler_path=None, output_folder='./output'):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)

    # Save each page as an image file in the specified folder
    for i, image in enumerate(images):
        output_filename = os.path.join(output_folder, f"{output_prefix}_{i + 1}.{output_format.lower()}")
        image.save(output_filename, output_format)
        print(f"Saved {output_filename}")


