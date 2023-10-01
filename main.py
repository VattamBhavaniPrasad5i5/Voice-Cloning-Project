import cv2
import os
import requests
from bs4 import BeautifulSoup
from moviepy.editor import *
import numpy as np
from gtts import gTTS
from pytube import YouTube
import random
import os
import numpy as np
from pydub import AudioSegment
import speech_recognition as sr
from googletrans import Translator, LANGUAGES

# from moviepy.editor import TextClip, CompositeVideoClip
from googleapiclient.discovery import build


def search_youtube_videos(api_key, keyword, max_results=10):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(
        q=keyword, type="video", part="id", maxResults=max_results
    )
    response = request.execute()
    video_links = [
        "https://www.youtube.com/watch?v=" + item["id"]["videoId"]
        for item in response.get("items", [])
    ]
    return video_links


def download_video_clips(video_links, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for i, video_link in enumerate(video_links):
        try:
            yt = YouTube(video_link)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=save_dir, filename=f"clip_{i}")
        except Exception as e:
            print(f"Error downloading video {i}: {e}")


def extract_audio_from_video(video_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, video_file in enumerate(os.listdir(video_dir)):
        video_path = os.path.join(video_dir, video_file)
        audio_clip = VideoFileClip(video_path).audio
        audio_clip.write_audiofile(os.path.join(output_dir, f"voice_{i}.wav"))


def split_audio(audio_dir, output_dir, num_segments=20, segment_duration=(6, 10)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for audio_file in os.listdir(audio_dir):
        audio_path = os.path.join(audio_dir, audio_file)
        audio = AudioSegment.from_wav(audio_path)

        # Calculate the desired duration for each segment
        total_duration = len(audio)
        target_duration = total_duration / num_segments

        for i in range(num_segments):
            # Generate a random duration within the specified range
            min_duration, max_duration = segment_duration
            random_duration = np.random.uniform(
                min_duration * 1000, max_duration * 1000
            )

            # Ensure the segment doesn't exceed the audio length
            random_duration = min(
                random_duration,
                total_duration - (num_segments - i - 1) * target_duration,
            )

            # Split the audio segment
            segment = audio[:random_duration]

            # Save the segment as a WAV file
            segment.export(
                os.path.join(output_dir, f"{os.path.splitext(audio_file)[0]}_{i}.wav"),
                format="wav",
            )

            # Remove the used portion from the original audio
            audio = audio[random_duration:]


def translate_to_telugu(text):
    # Create a Translator object
    translator = Translator()

    # Translate English to Telugu
    translation = translator.translate(text, src="en", dest="te")

    # Return the translated text in Telugu
    return translation.text


def translate_to_hindi(text):
    # Create a Translator object
    translator = Translator()

    # Translate English to Hindi
    translation = translator.translate(text, src="en", dest="hi")

    # Return the translated text in Hindi
    return translation.text


##############################################################

keyword = "SharuKhan Tedx"
videos_dir = "videos_dir"
output_file = "new_output_VK.mp4"
num_clips = 1
api_key = "YOUR_YOUTUBE_API_KEY"
video_links = search_youtube_videos(api_key, keyword, num_clips)

print(len(video_links))
download_video_clips(video_links, videos_dir)


# Extract audio from downloaded videos and save as WAV files
extracted_audio_dir = "voice_wav"
extract_audio_from_video(videos_dir, extracted_audio_dir)
print("audio extraction done")


split_audio_dir = "voice_segments"

# Split the extracted audio into 10 segments
split_audio(
    extracted_audio_dir, split_audio_dir, num_segments=20, segment_duration=(6, 10)
)
print("Audio splitting completed.")
print("Done")
#######################################################################
recognizer = sr.Recognizer()

# Load your WAV file
#
speech_text = ""
# Extract text from the audio file
for i in range(10):
    audio_file_path = "voice_segments/" + "voice_0_" + str(i) + ".wav"
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            speech_text += text + " "

        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
print(speech_text)
print("/n")
telugu_translation = translate_to_telugu(speech_text)
hindi_translation = translate_to_hindi(speech_text)


print(telugu_translation)
print(hindi_translation)
