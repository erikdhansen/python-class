# Triple single quotes indicate a multiline string,
# in this case, a comment

'''
 Simple Python dictionary

 Dictionaries are otherwise known as
 associative arrays, or hashes
 depending on the programming language
  being used
'''

dict = {
   'key_1':'value_1',
   'key_2':'value_2',
   'key_3':'value_3',
   'key_4':'value_4',
   'key_5':'value_5',   
}

print 'Printing list of keys...'
list_of_keys = dict.keys()
for key in list_of_keys:
    print('keys[] = %s' % (key))
    
print ''
print 'Printing list of values...'
list_of_values = dict.values()
for value in list_of_values:
    print('values[] = %s' % (value))

print ''
print 'Printing key=>value...'
for key in dict:
    print('dict[%s] = %s' % (key, dict[key]))
    
print ''
print 'Creating new empty dictionary...'
empty_dict = {}
print 'Inserting empty_dict[key_four] => value_4...'
empty_dict['key_four'] = 'value_4'

print 'Printing empty_dict...'
for key in empty_dict:
    print('dict[%s] = %s' % (key, empty_dict[key]))
print ''

# sorting the keys and then accessing dictionary
# in key sorted order
print 'Sorting dict keys...'
keys = dict.keys()
keys.sort()
for key in keys:
    print('dict[%s] = %s' % (key, dict[key]))

print ''
print 'Getting both key and value simultaneously...'
for key, value in dict.items():
    print('dict[%s] = %s' % (key, value))
    
print 'Deleting a single dict entry (key_3)...'
del dict['key_3']

print ''
print 'Getting both key and value simultaneously...'
for key, value in dict.items():
    print('dict[%s] = %s' % (key, value))

print ''
print 'Clearing the entire dict...'
dict.clear()

print ''
print('New length of dict = %d' % (len(dict)))
print 'Getting both key and value simultaneously...'
for key, value in dict.items():
    print('dict[%s] = %s' % (key, value))




