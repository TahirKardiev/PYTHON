import csv

import pandas as pd

data = pd.read_csv("list.csv", nrows=1)
print(data)


data = {
    'Name': ['Mika'],
    'Numbers': [91],
    'Adress': [91],
    'Position': [91]
}
df = pd.DataFrame(data)
df.to_csv('list.csv', mode='a', index=False, header=False)


