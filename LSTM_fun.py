import numpy as np
#import h5py

from keras.models import Sequential
from keras.layers import LSTM, Dense

if __name__ == '__main__':
	print('fuck me, right?')

# generate and shape data
data = [[i for i in range(100)]]
data = np.array(data, dtype=float).reshape(1,1,100)
target = [[i for i in range(1, 101)]]
target = np.array(target, dtype=float).reshape(1,1,100)

# create test data
x_test=[i for i in range(100,200)]
x_test=np.array(x_test).reshape((1,1,100))
y_test=[i for i in range(101,201)]
y_test=np.array(y_test).reshape(1,1,100)

#train
model = Sequential()
model.add(LSTM(100, input_shape=(1,100),return_sequences=True,activation='sigmoid'))
model.add(Dense(100))
#add nesterov somewhere here? 
model.compile(loss='mse', optimizer='adam',metrics=['accuracy'])
model.fit(data, target, epochs=500, batch_size=1, verbose=2, validation_data=(x_test, y_test))
#model.save_weights("/Users/rambo/testweights")
predict = model.predict(data)
weights = model.get_weights()

