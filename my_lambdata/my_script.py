import pandas
from my_mod import enlarge
#import category-encoders

print('Hello World')

df = pandas.DataFrame({'state': ['CT', 'CO', 'CA', 'TX']})
print(df.head())

print('---------')
x = 5
print('Number', x)
print('Enlarged Number', enlarge(x))
