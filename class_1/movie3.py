import moviepy.editor as mp
import random

video1 = mp.VideoFileClip("ollie.mp4")
video2 = mp.VideoFileClip("ollie2.mp4")

clips = []

for i in range(0,10):
    start = random.uniform(0, video1.duration-1)
    end = start + 1
    clip1 = video1.subclip(start, end)

    start = random.uniform(0, video2.duration-1)
    end = start + 1
    clip2 = video2.subclip(start, end)

    clips.append(clip1)
    clips.append(clip2)

composition = mp.concatenate(clips)
composition.write_videofile('composition_random_two_video.mp4', fps=25)
