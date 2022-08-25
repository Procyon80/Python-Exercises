import pandas as pd
import numpy as np

url = ("https://raw.github.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv")


tips = pd.read_csv(url)

print(tips)