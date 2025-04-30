#moviepy library
import moviepy.editor
cvt_video = moveipy.editor.VideoFileClip("Time")

ext_audio = cvt_video.audio

ext_audio.write_audiofile("audio_Extracted.mp3")