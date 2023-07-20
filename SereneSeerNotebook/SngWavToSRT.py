import wave
import math
import srt
import Commons

date = Commons.file_date

audio_file = f"AllSignsHoroscopeAudio{date}.wav"
text = Commons.all_signs_horoscope

with wave.open(audio_file, 'rb') as wf:
    frames = wf.getnframes()
    frame_rate = wf.getframerate()
    run_time = frames / frame_rate
    Commons.all_signs_run_time = run_time

# Determine the duration per subtitle
num_of_lines = math.ceil(len(text) / 40)  # Assuming maximum of 40 characters per line
subtitle_duration = run_time / num_of_lines

# Create an empty list to store the subtitles
subtitles = []

# Split the text into lines without splitting words
lines = []
current_line = ""
for word in text.split():
    if len(current_line) + len(word) + 1 <= 40:
        current_line += word + " "
    else:
        lines.append(current_line.strip())
        current_line = word + " "
if current_line:
    lines.append(current_line.strip())

# Create subtitles based on the lines
for i, line in enumerate(lines):
    start_time = i * subtitle_duration
    end_time = (i + 1) * subtitle_duration

    # Create a Subtitle object for each line of text
    subtitle = srt.Subtitle(
        index=i + 1,
        start=srt.timedelta(seconds=start_time),
        end=srt.timedelta(seconds=end_time),
        content=line
    )

    # Append the subtitle to the list
    subtitles.append(subtitle)

# Write the subtitles to the output file
output_file = f"AllSignsSubtitles{date}.srt"
with open(output_file, 'w') as f:
    f.write(srt.compose(subtitles))