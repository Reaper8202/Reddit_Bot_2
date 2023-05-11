from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip

main_path = "/Users/derek/Desktop/Python Code/output.mp4"
subtitle_path = "/Users/derek/Desktop/Python Code/Reddit Optimization/subtitles.srt"
final_path = "/Users/derek/Desktop/Python Code/output_subtitled.mp4"

main_video = VideoFileClip(main_path)
generator = lambda txt: TextClip(txt, font="arial", fontsize=50, color="white", method='caption', size=main_video.size)

sub_clip = SubtitlesClip(subtitle_path, generator)

result = CompositeVideoClip([main_video, sub_clip.set_position(('center', 'bottom'))], size=main_video.size)
result.write_videofile(final_path, fps=main_video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
