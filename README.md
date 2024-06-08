# speaker-noise-cancellation

The purpose of this repository is to create a software that is able to capture the output of the speaker and be able to cancel that echo of that output when it is recorded by the microphone. When this software is running, it is able to make people are in call not worry about echos even without wearing any headphones.

# recording.py 

This file will allow you to play any designated sound file and record your microphone input at the same time. The recorded file will be placed in the recording folder. 

# TODO 

1. loop through all the soundfiles and record all the recording
2. figure out a method that would be able to compare the recorded file and the original file and allow us to filter it out (mathematically) PSNR?
3. filter the output of the speaker out or suppress it. 
