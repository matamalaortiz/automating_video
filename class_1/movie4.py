import random
import moviepy.editor as mp

video1 = mp.VideoFileClip("ollie.mp4")
video2 = mp.VideoFileClip("ollie2.mp4")

#video1 = video1.resize((800,600)) ## Resize the video
#video2 = video2.resize((800,600)) ## Resize the video

clips = []

clip1 = video1.subclip(0, 3)
clip2 = video2.subclip(0, 3)

clip1 = clip1.set_pos((100, 100)).resize((200, 200));
clip1 = clip1.set_start(1)
# clip1 = clip1.crossfadein(1)

clips.append(clip2)
clips.append(clip1)

composition = mp.CompositeVideoClip(clips)
composition.write_videofile('composition_overlay.mp4', fps=25)
