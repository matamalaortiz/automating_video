import moviepy.editor as mp

video = mp.VideoFileClip("animation.mp4").subclip(0,1)
video2 = mp.VideoFileClip("ollie.mp4").subclip(30,33)

# video = video.resize((800,600)) ## Resize the video
# video2 = video2.resize((800,600)) ## Resize the video

clips = [video, video2]

composition = mp.concatenate(clips)
composition.write_videofile('composition.mp4', fps=25)
