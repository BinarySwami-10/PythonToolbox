import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense,Dropout,LSTM,RNN
from keras.utils import np_utils
import os
def read_this (path):
    a='';f=open(path,'r',errors='ignore');a+=f.read()
    print('File Opened And Engaged : ',path)
    return a
LOCAL_RUNTIME=1
if LOCAL_RUNTIME:
    masterpath='./data/clean'
    os.chdir(masterpath)
else:
    masterpath='/content/drive/My Drive/Python/data/'
    os.chdir(masterpath)

projectTitle="huffpostData-t" #nameoffile and also weightfile
print('opening file')

textObj=(open( projectTitle + ".txt",'r',errors='ignore'))
tokens = read_this('standardtokens.txt').split();#tokens.extend(['xyz'])
n_to_tok = {n:char for n, char in enumerate(tokens)}
tok_to_n = {char:n for n, char in enumerate(tokens)}

text = textObj.read().split()
textMunda=[];lnth= int(len(text)/100) ; print(lnth)
for i in range(lnth):
    abc=text[i*40000:(i+1)*40000]
    textMunda.append(abc)

epchs = 50
for i in range(epchs):
    print('epoch number ',i)
    textArr = textMunda[i] ; print('i th TextMunda.len = ',len(textMunda[i]))
    # tokens = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    
    X = []
    Y = []

    length = len(textArr)
    seq_length = 32
    print('array start')
    for i in range(0, length-seq_length, 1):
        sequence = textArr[i:i + seq_length]
        label =textArr[i + seq_length]
        X.append([tok_to_n[char] for char in sequence])
        Y.append(tok_to_n[label])
    # print( X[1], Y[0],sep='\n')

    X_modified = np.reshape(X, (len(X), seq_length, 1))
    X_modified = X_modified / float(len(tokens))
    Y_modified = np_utils.to_categorical(Y,num_classes=1000);

    print('np COMPLETD')
    print('X_modified has shape',X_modified.shape)
    print('Y_modified has shape',Y_modified.shape)

    print('model start')
    model = Sequential()
    model.add( LSTM(500, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add( LSTM(500, return_sequences=True))
    model.add(Dropout(0.2))
    model.add( LSTM(500),)
    model.add(Dropout(0.1))

    model.add(Dense(Y_modified.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    
    print('model compiled')
    train1_predict0=1; #SWITCH TRAIN OR PREDICT

    if (train1_predict0==0):
        for i in range(1):
            print('X:Ymodified has',X_modified.shape,Y_modified.shape)
            try:
                model.load_weights(masterpath + projectTitle + 'huffpostData-5c5c5c.h5')
            except Exception as e :
                # raise e
                print ("MODE NOT LOADED DURING TRAIN as :", e )
                pass
            model.fit(X_modified, Y_modified, epochs=10, batch_size=32)
            model.save_weights(masterpath + projectTitle + 'huffpostData-5c5c5c.h5')

    else:
        model.load_weights( 'huffpostData-5c5c5c.h5')

        string_mapped='how are you do my name is this and i love eat food and drive and go trump and i love eat food and i love eat food are you do my '.split()
        string_mapped=[tok_to_n[i] for i in string_mapped]
        string_mapped = X[91]
        full_string = [n_to_tok[value] for value in string_mapped]
        # generating characters
        for i in range(100):
            x = np.reshape(string_mapped,(1,len(string_mapped), 1))
            x = x / float(len(tokens))

            pred_index = np.argmax(model.predict(x, verbose=0))
            seq = [n_to_tok[value] for value in string_mapped]
            full_string.append(n_to_tok[pred_index])
            print((n_to_tok[pred_index]) , end='.')

            string_mapped.append(pred_index)
            string_mapped = string_mapped[1:len(string_mapped)]
        pass
