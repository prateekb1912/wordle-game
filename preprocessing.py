import pandas as pd

words_df = pd.read_csv('words.csv')

words_df.sort_values(by='occurrence', ascending=False, inplace=True)

words_df.to_csv('popluar_words_1000.csv', sep=',', index=False)