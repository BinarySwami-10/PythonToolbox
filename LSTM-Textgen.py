# %tensorflow_version 1.x
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import RNN
from keras.utils import np_utils

masterpath='/content/drive/My Drive/Python/data/'; localpath='data/'
projectTitle="sampleenglish-c" #nameoffile and also weightfile
print('opening file')
textObj=(open(localpath + projectTitle + ".txt",'r',errors='ignore'))

train1_predict0=0; #SWITCH TRAIN OR PREDICT
epchs = 50

for i in range(epchs):
    print('epoch number ',i)
    text = textObj.read(1024*64)
    characters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    n_to_char = {n:char for n, char in enumerate(characters)}
    char_to_n = {char:n for n, char in enumerate(characters)}
    X = []
    Y = []
    length = len(text)
    seq_length = 26

    print('array start')
    for i in range(0, length-seq_length, 1):
        
        sequence = text[i:i + seq_length]
        label =text[i + seq_length]
        X.append([char_to_n[char] for char in sequence])
        Y.append(char_to_n[label])
    print('np COMPLETD')

    X_modified = np.reshape(X, (len(X), seq_length, 1))
    X_modified = X_modified / float(len(characters))
    Y_modified = np_utils.to_categorical(Y)

    print('model start')
    model = Sequential()
    model.add(LSTM(500, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add( LSTM(500, return_sequences=True ))
    model.add(Dropout(0.2))
    model.add( LSTM(500,))
    model.add(Dense(Y_modified.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    
    print('model compiled')

    if (train1_predict0==1):
        for i in range(1):
            try:
                model.load_weights(localpath + projectTitle+'d700-700-700.h5')
            except :
                print ("MODE NOT LOADED DURING TRAIN")
                pass
            model.fit(X_modified, Y_modified, epochs=10, batch_size=512)

            model.save_weights(localpath + projectTitle+'d700-700-700.h5')
    else:
        model.load_weights(localpath + projectTitle+'d700-700-700.h5')
        pass


#_____________________________________________________________________
    model.load_weights(localpath + projectTitle+'d700-700-700.h5')
    string_mapped = X[90]
    print(string_mapped)
    full_string = [n_to_char[value] for value in string_mapped]
    string_mapped=[char_to_n[i] for i in 'we saw a unicorn there and']
    # print(full_string)
    # generating characters
    for i in range(300):
        x = np.reshape(string_mapped,(1,len(string_mapped), 1))
        x = x / float(len(characters))

        pred_index = np.argmax(model.predict(x, verbose=0))
        seq = [n_to_char[value] for value in string_mapped]
        full_string.append(n_to_char[pred_index])
        print((n_to_char[pred_index]) , end='')

        string_mapped.append(pred_index)
        string_mapped = string_mapped[1:len(string_mapped)]

    # txt=""
    # for char in full_string:
    #     txt = txt+char
    # print(txt)