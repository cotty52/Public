import os
import cv2  # pip install opencv-python
import numpy as np  # pip install numpy

# Screen size
x_Screen = 1920
y_Screen = 1080

# Read the image and resize it 
imgSize = 300
img = cv2.imread(r'ImgName.jpg')      # path to image
img = cv2.resize(img, (imgSize, imgSize))   # resize image

fps = 30
vidLength = 20  # in seconds

# Staring position of image
x_Img = 900 
y_Img = 0

# Starting direction
x_Direction = 1
y_Direction = 1

moveSpeed = 3

# Define the animation function
def animate(t):
    global x_Img, y_Img, x_Direction, y_Direction

    # Change direction if image reaches edge of screen
    if x_Img <= 0:
        y_Img -= x_Img
        x_Img -= x_Img
        x_Direction = 1
    elif x_Img >= x_Screen - imgSize:
        y_Img -= x_Img-(x_Screen - imgSize)
        x_Img -= x_Img-(x_Screen - imgSize)
        x_Direction = -1

    if y_Img <= 0:
        x_Img -= y_Img
        y_Img -= y_Img
        y_Direction = 1
    elif y_Img >= y_Screen - imgSize:
        x_Img -= y_Img-(y_Screen - imgSize)
        y_Img -= y_Img-(y_Screen - imgSize)
        y_Direction = -1

    # Update position based on direction
    x_Img += x_Direction * moveSpeed
    y_Img += y_Direction * moveSpeed

    # Create a new blank frame
    frame = np.zeros((y_Screen, x_Screen, moveSpeed), dtype=np.uint8)      # black background
    # frame = np.full((y_Screen, x_Screen, moveSpeed), 255, dtype=np.uint8)   # white background

    # Copy the image onto the frame at the current position
    frame[y_Img:y_Img+imgSize, x_Img:x_Img+imgSize] = img

    return frame


# Create the video clip
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_clip = cv2.VideoWriter('FileName.mp4', fourcc, fps, (x_Screen, y_Screen))

frameTotal = vidLength*fps  # Claculates total number of frames
count = 0
mult = 1
# Write the video frames to file
for t in np.arange(0, vidLength, 1/fps):
    frame = animate(t)
    video_clip.write(frame)
    percentComplete = t/vidLength

    out = int(percentComplete*100)
    count += 1
    if count == (frameTotal/100)*mult:
        os.system("cls")
        print(out, "%")
        mult += 1

# Create the video clip
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
clip = cv2.VideoWriter('FileName.mp4', fourcc, fps, (x_Screen, y_Screen))
for t in np.arange(0, vidLength, 1/fps):
    frame = animate(t)
    clip.write(frame)

os.system("cls")
print("100 %")