import pandas
import my_mod

print('Hello World')

print('---------')

cbag = my_mod.coffee_bag(50,'Bolivia')
cbag.quality_reminder()

print('Bag weight in lbs: ',cbag.weight_to_lbs())
