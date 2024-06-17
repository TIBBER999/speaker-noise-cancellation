import numpy as np
import wave
import math 
def read_audio(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        n_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        n_frames = wav_file.getnframes()
        framerate = wav_file.getframerate()
        frames = wav_file.readframes(n_frames)
        audio = np.frombuffer(frames, dtype=np.int16)
        audio = audio.reshape(-1, n_channels)
        return audio, framerate

def write_audio(file_path, audio, framerate):
    with wave.open(file_path, 'wb') as wav_file:
        n_channels = audio.shape[1]
        sample_width = 2
        n_frames = audio.shape[0]
        wav_file.setnchannels(n_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(framerate)
        wav_file.writeframes(audio.tobytes())

def calculate_rms(audio):
    return np.sqrt(np.mean(audio**2))

def adjust_amplitude(known_audio, mixed_audio):
    rms_known = calculate_rms(known_audio)
    rms_mixed = calculate_rms(mixed_audio)
    print ("rms rec then ori", rms_mixed, rms_known)

    gain_factor = rms_mixed / rms_known 
    print("gain factors are", gain_factor)
    print("known_audio decimal places", known_audio)
    adjusted_known_audio =  (known_audio * gain_factor).astype(np.int16)
    print("adjusted_known_audio decimal places", adjusted_known_audio, adjusted_known_audio.dtype)


    return adjusted_known_audio

def cancel_signal(mixed_audio, adjusted_known_audio):
    known_audio_inverted = -adjusted_known_audio
    audio_diff = mixed_audio + known_audio_inverted
    return audio_diff

# Load mixed and known audio
mixed_audio, framerate_mixed = read_audio('Rectest.wav')
known_audio, framerate_known = read_audio('Oritest.wav')

# Make sure the sample rates match:
if framerate_mixed != framerate_known:
    raise ValueError("Sample rates do not match.")

# Align if necessary (this is a simplified example; alignment requires sophisticated methods)

# Adjust the amplitude of the known audio
adjusted_known_audio = adjust_amplitude(known_audio, mixed_audio)

# Cancel known audio
result_audio = cancel_signal(mixed_audio, adjusted_known_audio)

# Write the result to a new file
write_audio('output_signal.wav', result_audio, framerate_mixed)
