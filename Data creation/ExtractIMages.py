# import libraries
import cv2
import os

# set path to dataset
video_folder_path = 'C:/Users/ava/OneDrive/Desktop/extract images/Dataset'

video_files = [f for f in os.listdir(video_folder_path) if f.endswith('.mp4')]

# set path to save extracted images
os.makedirs('C:/Users/ava/OneDrive/Desktop/extract images/Dataset/extractimages', exist_ok=True)

for video_file in video_files:
    # Open the video file
    cap = cv2.VideoCapture(os.path.join(video_folder_path, video_file))

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Set the frame interval (e.g., 1 frame per second)
    frame_interval = int(cap.get(cv2.CAP_PROP_FPS))

    # Loop through each frame and extract image
    for i in range(0, total_frames, frame_interval):
        # Set the frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)

        # Read the frame
        ret, frame = cap.read()

        # Save the image
        cv2.imwrite(os.path.join('C:/Users/ava/OneDrive/Desktop/extract images/Dataset/extractimages', f'{video_file}_{i}.jpg'), frame)
        print("Save image",i)

    # Release the video file
    cap.release()
