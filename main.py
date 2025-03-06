import cv2
import detecttext
import util
import chromesearch

def process_video():
    # Set the source
    source = 0  # Uncomment this to use the webcam
    # source = "./input/test2.mp4"  # Path to the video file

    # Capture the video
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Unable to open the video source.")
        return

    # Loop to read and display video frames
    while True:
        ret, frame = cap.read()  # Read a frame from the video source
        title=""
        author=""
        publisher=""
        other=""
        combined_text = ""  # Initialize the search text
        if not ret:
            print("End of video or error reading the frame.")
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        
# Call the function
process_video()
