import pickle
import pandas as pd

with open('ipl_data.pickle', 'rb') as handle:
    dictionary = pickle.load(handle)

print(dictionary)
