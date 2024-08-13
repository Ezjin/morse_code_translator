import pandas as pd


text = 'tem tres palavras'

words = text.split()

for word in words:
    for l in word:
        print(l)