from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip
import Commons

date = Commons.file_date
# Paths to new video and subtitle files
video_file = f"AllSignsTempVid{file_date}.mp4"
subtitle_file = f"AllSignsSubtitles.srt{file_date}"

# Load the main video clip
main_video = VideoFileClip(video_file)

# Create the subtitle generator function
def subtitle_generator(txt):
    return TextClip(txt, font="arial", fontsize=40, color="red", method='caption', size=main_video.size)

# Create the subtitle clip using SubtitlesClip and the generator
sub_clip = SubtitlesClip(subtitle_file, subtitle_generator)

# Composite the main video and subtitle clip
result = CompositeVideoClip([main_video.set_audio(None), sub_clip.set_audio(main_video.audio)], size=main_video.size)

# Export the final video with the combined elements
output_file = f"AllSignsFinalVideo{date}.mp4"
result.write_videofile(output_file, fps=main_video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")