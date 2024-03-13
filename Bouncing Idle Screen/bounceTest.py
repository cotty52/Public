import os
import cv2
import numpy as np
from moviepy.editor import *
import moviepy.editor as mp

# Read the image and resize it to
imgSize = 300
img = cv2.imread('ryan ninja.jpg')
img = cv2.resize(img, (imgSize, imgSize))

fps = 30
vidLength = 1200  # in seconds

x = 900
y = 0
x_direction = 1
y_direction = 1

# Define the animation function


def animate(t):
    global x, y, x_direction, y_direction

    # Change direction if image reaches edge of screen
    if x <= 0:
        y -= x
        x -= x
        x_direction = 1
    elif x >= 1920 - imgSize:
        y -= x-(1920 - imgSize)
        x -= x-(1920 - imgSize)
        x_direction = -1

    if y <= 0:
        x -= y
        y -= y
        y_direction = 1
    elif y >= 1080 - imgSize:
        x -= y-(1080 - imgSize)
        y -= y-(1080 - imgSize)
        y_direction = -1

    # Update position based on direction
    x += x_direction * 3  # can change speed by multiplying by a different number
    y += y_direction * 3

    # Create a new blank frame
    frame = np.zeros((1080, 1920, 3), dtype=np.uint8)      # black
    # frame = np.full((1080, 1920, 3), 255, dtype=np.uint8)   # white

    # Copy the image onto the frame at the current position
    frame[y:y+imgSize, x:x+imgSize] = img

    return frame

os.system("cls")
print("100 %")

# Create the video clip
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_clip = cv2.VideoWriter('ryanMyLove.mp4', fourcc, fps, (1920, 1080))

frameTotal = vidLength*fps
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

# Close the video clip
video_clip.release()

# Load the video file
video = mp.VideoFileClip('ryanMyLove.mp4')

# Load the audio file and repeat it to match the duration of the video
audio = mp.AudioFileClip('I Want To Be Ninja.mp3').audio_loop(
    duration=video.duration)

# Add the audio to the video and save the result
result = video.set_audio(audio)
result.write_videofile('ninja.mp4', fps=fps)