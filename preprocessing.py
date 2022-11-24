import pandas as pd

words_df = pd.read_csv('words.csv')

words_df.sort_values(by='occurrence', ascending=False, inplace=True)

popular_words = list(words_df.head(5000)['word'])

with open('popular_words_5000.txt', 'w') as file:
    for word in popular_words:
        file.write(word+'\n')
