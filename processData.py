#### processData.py
#### process audio and csv data for neural network training
## Rambo You
## University of Minnesota
## Capstone MSST 2017

#import sys,csv
import numpy as np
from scipy.io.wavfile import read
from python_speech_features import mfcc

int_key_file = 'longTractIntKey.csv'
when_pressed_file = 'longtract.csv'
audio_file = 'longTract.wav'

## reading in data and setting variables
# converting key presses and when they were pressed to 2 separate arrays
keysPressed = np.genfromtxt(int_key_file, delimiter=',', usecols=0, dtype=int)
whenPressed = np.genfromtxt(when_pressed_file, delimiter=',', usecols=1, dtype=float)
# convert audio file to array
rate,signal = read(audio_file)
millisecond = 4410

# variables
windowSize = 4410 #might change this to argv, and do negative window timings


## manually processing data
#if __name__ == "__main__":
#    audioFile = sys.argv[1] + ".wav"
#    audioFile = read(audioFile)
#    dataFile = sys.argv[1] + ".csv"
#

## process audio data, will turn into a class later
# one ms is equal to 4410 samples or length of array
# locate where each key is pressed, and take out 100 ms audio data windows into 1 array

def keys():
    windows = np.empty([0,1]) #window size of 100 ms
    for tstamp in whenPressed:
        start_window = np.floor(tstamp*millisecond).astype(np.int) - 1470
        end_window = start_window + millisecond
        window_signal = signal[start_window:end_window]
        windows = np.append(windows, window_signal)
    return(windows,window_signal.shape)

def key_windows():
    windows = np.empty([0,1]) #window size of 100 ms
    for tstamp in whenPressed:
        start_window = np.floor(tstamp*millisecond).astype(np.int) - 1470
        end_window = start_window + millisecond
        window_signal = signal[start_window:end_window]
        window_signal = mfcc(window_signal,rate,winlen=.001,numcep=200)
        windows = np.append(windows, window_signal)
    return(windows,window_signal.shape)
# reshape for training. For some reason, reshaping data in a function causes
# significant slowdown
trainingData,shape = key_windows()
columns = shape[0]*shape[1]
rows = len(trainingData)/columns
rows = int(rows)
## gotta recalulate this for mfcc array
trainingData = np.reshape(trainingData,(rows,columns))
