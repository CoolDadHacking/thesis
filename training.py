#### training.py
#### train neural network
## Rambo You
## University of Minnesota
## Capstone MSST 2017

from keras.models import Sequential
from keras.layers import LSTM, Dense, Flatten, TimeDistributed, Embedding
from keras.utils.np_utils import to_categorical

from processData import *

max_features = 34


## shaping training data and labels for keras
x = trainingData[0:5000]
x = np.reshape(x,(x.shape[0], x.shape[1]))
y = keysPressed[0:5000]
y = np.reshape(y, (5000,1))
x_test = trainingData[5001:len(trainingData)]
x_test = np.reshape(x_test,(x_test.shape[0], x_test.shape[1]))
y_test = keysPressed[5001:len(trainingData)]
y_test = np.reshape(y_test,(260,1))
#y = to_categorical(y)
#y_test = to_categorical(y_test)


model = Sequential()
model.add(Embedding(max_features, 64))
model.add(Dense(64, activation='relu'))
model.add(LSTM(64, dropout=0.2, recurrent_dropout=0.2))

model.add(Dense(1, activation='sigmoid'))
#model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# this one works right now better:
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
#model.fit(x, y, epochs=5,batch_size=1, verbose=2, validation_data=(x_test, y_test))

def train():
    model.fit(x, y, epochs=5,batch_size=1, verbose=2, validation_data=(x_test, y_test))
    predict = model.predict(x)
    return predict

