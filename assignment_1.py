import pandas as bamboo
import matplotlib as mpl
import seaborn as sb
import warnings as w

w.filterwarnings('ignore')

df = bamboo.read_csv(r'Projects\Getting_started_with_ML\vgsales.csv')

print(df)
print(df.shape)
print(df.head())
print(df.tail())