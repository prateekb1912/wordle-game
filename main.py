from rich.console import Console
from random import choice
import pandas as pd

words = pd.read_csv('popular_words_5000.csv', sep=',')

words = words['word']

print(words)