import os
from pydub import AudioSegment, silence


def convert_audio_to_mono(audio_path):
    audio = AudioSegment.from_wav(audio_path)
    audio = audio.set_channels(1)
    return audio


def extract_speech_from_audio(audio_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for audio_file in os.listdir(audio_dir):
        audio_path = os.path.join(audio_dir, audio_file)

        # Convert audio to mono (if it's stereo)
        audio = convert_audio_to_mono(audio_path)

        # Split audio into speech segments based on silence
        audio_segments = silence.split_on_silence(
            audio, min_silence_len=500, silence_thresh=-40
        )  # Adjust as needed

        # Filter out segments shorter than 6 seconds
        audio_segments = [segment for segment in audio_segments if len(segment) >= 6000]

        # If there are more than 10 segments, take the first 10
        audio_segments = audio_segments[:10]

        # Export speech segments as separate audio files
        for i, speech_segment in enumerate(audio_segments):
            output_path = os.path.join(
                output_dir, f"{os.path.splitext(audio_file)[0]}_speech_{i}.wav"
            )
            speech_segment.export(output_path, format="wav")


# Paths
extracted_audio_dir = "voice_wav"
speech_extraction_dir = "speech_segments"

# Extract speech from the audio files
extract_speech_from_audio(extracted_audio_dir, speech_extraction_dir)
print("Speech extraction completed.")
