import pandas as bamboo
import matplotlib as mpl
import seaborn as sb
import warnings as w

w.filterwarnings('ignore')

df = bamboo.read_csv(r'Projects\Getting_started_with_ML\vgsales.csv')

df.drop(columns= ['Name', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Publisher'], inplace= True)
df.drop_duplicates(inplace= True)

df['Year'] = df['Year'].fillna(df['Year'].median())

print(df)
print(df.shape)
print(df.head())
print(df.tail())
print(df.isnull().sum())

Q1 = df['Global_Sales'].quantile(0.25)

Q3 = df['Global_Sales'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR

upper_bound = Q3 + 1.5 * IQR

df = df[(df['Global_Sales'] >= lower_bound) & (df['Global_Sales'] <= upper_bound)]

sb.lineplot(x = 'Year', y = 'Global_Sales', data = df)
mpl.pyplot.show()