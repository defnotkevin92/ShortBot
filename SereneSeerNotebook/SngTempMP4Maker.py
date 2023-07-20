from moviepy.editor import VideoFileClip, concatenate
from moviepy.editor import AudioFileClip
import math
import Commons

date = Commons.file_date
run_time = Commons.all_signs_runtime
video_file = "SereneRenderV0.avi"
audio_file = f"AllSignsHoroscopeAudio{date}.wav"

# Load the video clip
video_clip = VideoFileClip(video_file)

# Load the audio clip
audio_clip = AudioFileClip(audio_file)

# Calculate the duration of the video clip
video_duration = video_clip.duration

# Calculate the number of times the video needs to loop
num_loops = math.ceil(run_time / video_duration)+1

# Create a list of video clips with the necessary number of loops
video_clips = [video_clip] * num_loops

# Concatenate the video clips together
concatenated_clips = concatenate(video_clips)

# Set the audio of the concatenated video clip
final_clip = concatenated_clips.set_audio(audio_clip)

# Trim the final clip to match the desired run_time
final_clip = final_clip.subclip(0, run_time)

# Export the final clip as an MP4 file
output_file = f"AllSignsTempVid{date}.mp4"
final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")