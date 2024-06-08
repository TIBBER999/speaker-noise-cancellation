import os
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    """
    Converts an MP3 file to WAV format.
    
    Parameters:
    mp3_file_path (str): The path to the input MP3 file.
    wav_file_path (str): The path to save the output WAV file.
    """
    # Load the mp3 file
    audio = AudioSegment.from_mp3(mp3_file_path)

    # Export as wav format
    audio.export(wav_file_path, format="wav")

def convert_all_mp3_in_directory(mp3directory_path, wavdirectory_path):
    """
    Converts all MP3 files in the specified directory to WAV format.
    
    Parameters:
    directory_path (str): The path to the directory containing MP3 files.
    """
    for filename in os.listdir(mp3directory_path):
        if filename.endswith(".mp3"):
            mp3_file_path = os.path.join(mp3directory_path, filename)
            wav_file_path = os.path.join(wavdirectory_path, os.path.splitext(filename)[0] + ".wav")
            
            convert_mp3_to_wav(mp3_file_path, wav_file_path)
            print(f"Converted: {mp3_file_path} to {wav_file_path}")

if __name__ == "__main__":
    mp3directory = "soundfiles"  # Replace with the path to your directory containing MP3 files
    wavdirectory = "soundfiles_wav"
    convert_all_mp3_in_directory(mp3directory, wavdirectory)
    print("All MP3 files have been converted to WAV format, and stored in soundfiles_wav")