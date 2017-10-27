import random
import moviepy.editor as mp
from skimage.filter import gaussian_filter


video1 = mp.VideoFileClip("ollie.mp4")
video2 = mp.VideoFileClip("ollie2.mp4")

clips = []


clip1 = video1.subclip(0, 3)
clip2 = clip1.fl_image( blur )


clips.append(clip2)
clips.append(clip1)

composition = mp.concatenate(clips)
composition.write_videofile('composition_test.mp4', fps=25)
