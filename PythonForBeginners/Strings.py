first_name = 'Franco'
last_name = 'Lorenzo'
print('Hello ' + first_name + ' ' +last_name + '!')

# Some functions to modify strings
sentence = 'The dog is named Sammy.'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# Custom string formatting
output = 'Hello, ' + first_name + ' ' + last_name
print(output)
output = 'Hello, {} {}'.format(first_name, last_name)
print(output)
output = 'Hello, {0} {1}'.format(first_name, last_name)
print(output)
# Only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output)
