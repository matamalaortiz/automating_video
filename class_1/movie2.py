import moviepy.editor as mp
import random

video = mp.VideoFileClip("ollie2.mp4")

clips = []

start = 0
duration = 0.5
end = start + duration

while end < video.duration:
    clip = video.subclip(start,end)
    clips.append(clip)
    start = start + duration
    end = end + duration

random.shuffle(clips)
clips = clips[0:10] ## short the time of clips

composition = mp.concatenate(clips)
composition.write_videofile('composition_random_3.mp4', fps=25)
