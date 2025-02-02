# speaker-noise-cancellation

## Objective
The purpose of this software is to capture the output of the speaker and cancel the echo of that output when the microphone records it. When the software is running, people on the call would not need to worry about the echoes from the speaker's output. 

![alt text](readme_images/Hierarchy.png)

## Setup (not neccesary unless you want to remake the data)

Run RecordPlay.py after cloning the repository. The file will convert the mp3 files from soundfiles to wav files in soundfiles_wav and play the wav files then record those sound files through your computer microphone. 


## Repository hierarchy 

### recording_pre_filter 
This is the directory where we store the recording of the sound data which we record from the microphone. These sound files will be used to determine the relationship between the stock sound file and the recording of the microphone on data such as latency, frequency, and amplitude of the recording in comparison to the original data. 

### soundfiles 
This is the directory where we put all the stock sound data, which we will use to be played from the speaker and recorded by the microphone.  

### RecordPlay.py
Use this file to generate the recordings by playing the original data. 

### noise_cancel.py 
This is the file that can generate the filtered output however, currently, it isn't very effective. 

### recording.py (not used anymore)
This file will allow you to play any designated sound file and record your microphone input at the same time. The recorded file will be placed in the recording folder. 
