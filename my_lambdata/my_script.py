import pandas
from my_mod import enlarge, train_val_test_split

print('Hello World')

df = pandas.DataFrame({'nums': range(100)})
print(df.head())

print('---------')
train, val, test = train_val_test_split(df)
print('Train size',train.shape)
print('Val size',val.shape)
print('Test size',test.shape)

