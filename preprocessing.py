import pandas as pd

words_df = pd.read_csv('words.csv')

words_df.sort_values(by='occurrence', ascending=False, inplace=True)

popular_words = words_df.head(5000)

popular_words.to_csv('popluar_words_5000.csv', sep=',', index=False, )