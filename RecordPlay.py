import os
import argparse
from pydub import AudioSegment
import sounddevice as sd
import soundfile as sf
import concurrent.futures

def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    """
    Converts an MP3 file to WAV format.
    
    Parameters:
    mp3_file_path (str): The path to the input MP3 file.
    wav_file_path (str): The path to save the output WAV file.
    """
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")

def convert_all_mp3_in_directory(mp3_directory, wav_directory):
    """
    Converts all MP3 files in the specified directory to WAV format.
    
    Parameters:
    mp3_directory (str): The path to the directory containing MP3 files.
    wav_directory (str): The path to the directory where WAV files should be saved.
    """
    if not os.path.exists(wav_directory):
        os.makedirs(wav_directory)
    
    for filename in os.listdir(mp3_directory):
        if filename.endswith(".mp3"):
            mp3_file_path = os.path.join(mp3_directory, filename)
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_file_path = os.path.join(wav_directory, wav_filename)
            
            convert_mp3_to_wav(mp3_file_path, wav_file_path)
            print(f"Converted: {mp3_file_path} to {wav_file_path}")

def record_audio(duration, fs, channels):
    """
    Records audio for a specified duration.
    
    Parameters:
    duration (int): Duration of the recording in seconds.
    fs (int): Sample rate of the recording.
    channels (int): Number of audio channels.

    Returns:
    numpy.ndarray: The recorded audio data.
    """
    return sd.rec(int(duration * fs), samplerate=fs, channels=channels)


def output2input(wavdirectory):
    for filename in os.listdir(wavdirectory):
        if filename.endswith(".wav"):
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_file_path = os.path.join(wavdirectory, wav_filename)
    
        # Load the sound file 
        data, fs = sf.read(wav_file_path)

        # Define the duration of the playback and recording in seconds
        play_duration = 10  # Seconds

        # Calculate the number of samples to extract for the given duration
        num_samples = int(play_duration * fs)

        # Slice the data array to get only the desired duration
        data_to_play = data[:num_samples]

        # Play the sound file and record simultaneously using concurrent futures
        with concurrent.futures.ThreadPoolExecutor() as executor:
            play_future = executor.submit(sd.play, data_to_play, fs)
            record_future = executor.submit(record_audio, play_duration, fs, 2)

            # Wait for both tasks to complete
            play_future.result()
            recorded_data = record_future.result()
            sd.wait()  # Ensure all playback and recording is complete

        print("Playback and Recording complete.")

        # Optionally, save the recorded audio to a file
        recorded_filename = os.path.join("recording_pre_filter", wav_filename)
        sf.write(recorded_filename, recorded_data, fs)
        print(f"Recorded audio saved as {recorded_filename}")


if __name__ == "__main__":
    help = "Can convert, or Playback, or Both\n 0: Both Conversion and Playback\n 1: Only Conversion \n 2: Only Playback"
    parser = argparse.ArgumentParser(description = help)
    parser.add_argument('--option', type =int, default=0)
    parser.parse_args()

    args = parser.parse_args()
    option = args.option
    if (option ==0):
        print("Both Conversion and Playback")
    if (option == 1):
        print("Only Conversion")
    else:
        print ("Only Playback")



    mp3directory = "soundfiles"  # Replace with the path to your directory containing MP3 files
    wavdirectory = "soundfiles_wav"
    if (option == 0 or option == 1):
        convert_all_mp3_in_directory(mp3directory, wavdirectory)
        print("All MP3 files have been converted to WAV format and stored in soundfiles_wav")
    
    # Define the path to the sound file
    file_folder = 'soundfiles_wav'
    if (option == 0 or option == 2):
        output2input(file_folder)
        print("All playback has been completed and saved to recording_pre_filter/")

    
