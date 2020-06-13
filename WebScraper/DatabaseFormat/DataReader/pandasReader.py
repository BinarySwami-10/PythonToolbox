import html5lib,requests
from bs4 import BeautifulSoup as soup
import random
import pandas as pd
filename='BSE_link1.csv'
frame=pd.read_csv(filename)

# load 2 rows
print(frame[0:2])

# Display all columns
print('\n\nCOLUMNS :')
columns=frame.columns
for i in columns:
	print(i)

# load 2 column names
columns=frame.columns
print('\n\nCOLS',frame[columns[0:2]]) 
# print(frame[columns[1]])



