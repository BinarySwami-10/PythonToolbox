import numpy as np
import pandas as pd
from keras.utils import np_utils
def read_this (path):
	a=''
	f=open(path,'r',errors='ignore')
	a+=f.read()
	print('File Opened And Engaged : ',path)
	return a
projectTitle="huffpostData-c"
textObj = (open('./data/clean/'+projectTitle+".txt"))
text= textObj.read(200)
tokens = read_this('./data/standardtokens.txt').split()
tokens.append(' ')


# characters1 = sorted(list(set(text)))
# print(characters1==characters)
tokens = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n_to_char = {n:char for n, char in enumerate(tokens)}
char_to_n = {char:n for n, char in enumerate(tokens)}

X = []
Y = []
length = len(text)
seq_length = 10

# print('char n conversions Completed AND np array start')
for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label =text[i + seq_length]
    X.append([char_to_n[char] for char in sequence])
    Y.append(char_to_n[label])

print( X[2], Y[1],sep='\n')


X_modified = np.reshape(X, (len(X), seq_length, 1))
X_modified = X_modified / float(len(tokens))
Y_modified = np_utils.to_categorical(Y)
print(X_modified[2],Y_modified[1])

# ind=0
# string_mapped=[char_to_n[i] for i in 'we saw a unicorn there and']

# print( Y_modified.shape[1] )
# # print(X_modified[2],Y_modified.shape[1] )

