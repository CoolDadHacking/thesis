Full thesis outline in the docx files.


training an AI:
recordTraining.sh <output training file>
runs sox and buildKeylog.py. It takes one argument. If possible shorten the data file for the seconds you want to capture.

run to train an AI. This will take a while depending on your GPU. You will need to manually change this in the code.
training.py <training file>

to predict keystrokes
LSTM_fun.py <audio_file>
