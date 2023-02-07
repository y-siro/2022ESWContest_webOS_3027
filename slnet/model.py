from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
import numpy as np

DATA_PATH = os.path.join('MP_Data') 
actions = np.array([]) # Enter sign language name

label_map = {label:num for num, label in enumerate(actions)}

sequences, labels = [], []

        
for sl_name in os.listdir(DATA_PATH):
    sl_video_path = os.path.join(DATA_PATH + "/" + sl_name)
    for num_video in os.listdir(sl_video_path):
        num_sl_npy_path = os.path.join(sl_video_path + "/" + num_video)
        print(num_sl_npy_path)
        window = []
        for num_npy in os.listdir(num_sl_npy_path):
            print(num_npy)
            res = np.load(os.path.join(num_sl_npy_path, num_npy))
            window.append(res)

        flag = 0
        while len(window)>30:
            if flag==0 or flag==1:
                window = window[1:]
                flag += 1
            else:
                window.pop()
                flag = 0
        
        sequences.append(window)
        labels.append(label_map[sl_name])


X = np.array(sequences)
print(X.shape)

padding_X = pad_sequences(X)

y = to_categorical(labels).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

log_dir = os.path.join('Logs')
callback = EarlyStopping(monitor='loss', patience=20)
model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,258)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.fit(X_train, y_train, epochs=100, callbacks=[callback])

res = model.predict(X_test)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test accuracy :" , accuracy)

model.save('action.h5')