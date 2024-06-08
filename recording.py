import os
import sounddevice as sd
import soundfile as sf
import concurrent.futures

# Define the path to the sound file
file_folder = 'soundfiles_wav'
filename = 'We Choose to go to the Moon.mp3'
full_path = os.path.join(file_folder, filename)

# Load the sound file
data, fs = sf.read(full_path)

# Define the duration of the playback and recording in seconds
play_duration = 10  # Seconds

# Calculate the number of samples to extract for the given duration
num_samples = int(play_duration * fs)

# Slice the data array to get only the desired duration
data_to_play = data[:num_samples]

# Record audio function
def record_audio(duration, fs, channels=2, dtype='int16'):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype=dtype)
    sd.wait()  # Wait until recording is finished
    file_folder = 'recording'
    filename = 'We Choose to go to the Moon.wav'
    full_path = os.path.join(file_folder, filename)
    sf.write(full_path, recording, fs)  # Save recording to a file
    return recording

# Play the sound file and record simultaneously using concurrent futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    play_future = executor.submit(sd.play, data_to_play, fs)
    record_future = executor.submit(record_audio, play_duration, fs, 2)
    
    # Wait for both tasks to complete
    play_future.result()
    record_future.result()

print("Playback and Recording complete.")