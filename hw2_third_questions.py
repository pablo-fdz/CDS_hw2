# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)

covid_cases = {
    'Spain': [4, 8, 2, 0, 1], 
    'France': [2, 3, 6], 
    'Italy': [6, 8, 1, 7]
    }

# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

def total_registered_cases(data, country_name):
    return sum(data[country_name])

# This should print 15
print(total_registered_cases(covid_cases, 'Spain'))

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had

def total_registered_cases_per_country(data):
    country_list = []
    values_list = []
    for key, values in data.items():
        country_list.append(key)
        values_list.append(sum(values))
    totals_dictionary = dict(zip(country_list, values_list))
    return totals_dictionary

# This should create a dictionary with the keys 'Spain', 'France' and 'Italy',
# with the total cases for each country
covid_totals_dictionary = total_registered_cases_per_country(covid_cases)
print(covid_totals_dictionary)

# The code below prints the country with the maximum number of COVID cases
print(max(covid_totals_dictionary, key = covid_totals_dictionary.get))

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(data):
    totals_dictionary = total_registered_cases_per_country(data)
    maximum_case_country = max(totals_dictionary, 
                               key = totals_dictionary.get)
    # When finding the maximum, max() applies totals_dictionary.get to each key, 
    # retrieving the associated values (the total case numbers). It then compares 
    # these values and finds the key corresponding to the largest value.
    return maximum_case_country

# We create another sample dictionary
covid_cases_2 = {
    'Spain': [4, 8, 2, 0, 1], 
    'France': [2, 3, 6], 
    'Italy': [6, 8, 1, 7],
    'Germany': [9, 23, 3, 2],
    'UK': [32, 123, 56, 4]
    }

# Example with this last function, with another dictionary (it should print 'UK')
print(country_with_most_cases(covid_cases_2))

    