###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

import pandas as pd

# We import the data as a pandas data frame
df = pd.read_csv('covid.csv')

# We inspect the first rows of the data frame
print(df.head())

# We create a new column of death/confirmed for the whole data frame
df['Death/Confirmed'] = df['Deaths'] / df['Confirmed']

# Now, we print the list of countries (as a data frame) for those countries that 
# have more than 500, 1000 and 5000 active cases respectively.
for i in [500, 1000, 5000]:
    print('Ratio of deaths/confirmed for those countries with more than', i,
          'active cases:\n',
          df[['Country', 'Death/Confirmed']][df['Active'] >= i])