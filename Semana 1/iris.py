import pandas as pd

url = 'https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'

df = pd.read_csv(url)

print(df)

df.to_csv ('iris.csv', index = False)
