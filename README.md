# Voice-Cloning-Project
## Introduction
This project aims to perform voice cloning and translation tasks using Python. It utilizes various libraries and techniques to achieve the following objectives:


***Here my input is string (example: sharukhan tedx, samanatha tedx)***


1.***YouTube Video Extraction***: The project starts by searching for YouTube videos related to a specific keyword using the YouTube Data API. It extracts video links for further processing.

2.***Video Download and Audio Extraction***: It downloads the YouTube videos and extracts the audio content from them. The extracted audio is saved as WAV files.

3.***Audio Segmentation***: The audio files are split into smaller segments to process them individually. This segmentation helps in handling longer audio recordings efficiently.

4.***Speech Recognition***: Using the SpeechRecognition library, the project converts audio segments into text. This step enables the system to work with spoken content.

5.***Translation***: The extracted text is translated into multiple languages. In this project, translations to Telugu and Hindi are demonstrated using the Google Translate API.

6.***Voice Cloning***: Custom voice cloning is performed using the Tortoise library. It generates speech in multiple languages with the voice of the user's choice.

#### Note:
You should keep all the voice_segment files in Voice_Clone with ***tortoise-tts.ipynb*** where ***voice_segments*** are act as a dataset and u get the voice segment by executing the ***main.py***

## Project Structure
The project is structured as follows:

- '***main.py***': The main script that orchestrates the entire process, from video extraction to voice cloning.
- '***audio_processing.py***': Contains functions for audio extraction and segmentation.
- '***translation.py***': Handles text translation to Telugu and Hindi.
- '***Voice_Clone with tortoise-tts.ipynb***': Manages the custom voice cloning process.
- '***videos_dir/***': Directory to store downloaded YouTube videos.
- '***voice_wav/***': Directory to store extracted audio in WAV format.
- '***voice_segments/***': Directory to store segmented audio clips.
- '***tortoise***': Contains custom voice models and related data.

## Getting Started

1.Clone the repository to your local machine.

2.Install the required Python libraries listed in the '***requirements.txt***' file.

3.Obtain a '***YouTube Data API***' key from the Google Developer Console and replace the api_key variable in '***main.py***' with your key.

4.Run '***main.py***' to execute the entire voice cloning and translation pipeline.

## Dependencies

- Python 3.x
- Google YouTube Data API
- Tortoise Voice Cloning Library
- SpeechRecognition Library
- Pytube Library
- Googletrans Library
- MoviePy Library
- NumPy Library


![Screenshot (115)](https://github.com/VattamBhavaniPrasad5i5/Voice-Cloning-Project/assets/97446586/26c00841-8c64-4174-8ded-53a957121510)




## Recorded Video


https://github.com/VattamBhavaniPrasad5i5/Voice-Cloning-Project/assets/97446586/31e695cc-6d4e-4c5a-a037-506bdca99bc1



