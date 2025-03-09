import cv2
import numpy as np

def find_most_changed_grid_section(image1_path, image2_path, width_num_parts, height_num_parts):
    """
    Compares two images by dividing them into a grid and identifies the section with the most changes.

    :param image1_path: Path to the first image.
    :param image2_path: Path to the second image.
    :param width_num_parts: Number of vertical sections to divide the images into.
    :param height_num_parts: Number of horizontal sections to divide the images into.
    :return: The (row, column) index (1-based) of the section with the most changes.
    """
    # Read images in grayscale mode
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Verify if images are loaded properly
    if image1 is None or image2 is None:
        raise ValueError("One or both images could not be loaded. Please check the file paths.")

    # Ensure images have the same dimensions
    if image1.shape != image2.shape:
        raise ValueError("Images must have the same dimensions for comparison.")

    # Get image dimensions
    height, width = image1.shape

    # Determine width and height of each section
    part_width = width // width_num_parts
    part_height = height // height_num_parts

    # Compute differences for each section
    differences = np.zeros((height_num_parts, width_num_parts))  # Grid to store differences

    for i in range(height_num_parts):
        for j in range(width_num_parts):
            # Extract corresponding parts
            part1 = image1[i * part_height: (i + 1) * part_height, j * part_width: (j + 1) * part_width]
            part2 = image2[i * part_height: (i + 1) * part_height, j * part_width: (j + 1) * part_width]

            # Compute absolute difference
            diff = cv2.absdiff(part1, part2)

            # Sum of differences as a measure of change
            differences[i, j] = np.sum(diff)

    # Identify the section with the most changes (returns row, col index)
    most_changed_row, most_changed_col = np.unravel_index(np.argmax(differences), differences.shape)

    # Convert to 1-based index
    return most_changed_row, most_changed_col

# # Example usage
# image1_path = "./output/clip/cropped_box_11.png"
# image2_path = "./comimg/com_1.png"
# result = find_most_changed_grid_section(image1_path, image2_path, width_num_parts=4, height_num_parts=4)
# print(f"The most changed section is at row {result[0]}, column {result[1]}.")
