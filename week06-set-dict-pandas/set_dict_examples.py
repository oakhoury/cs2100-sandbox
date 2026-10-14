
# A set is an unordered collection with no duplicates

student_names : set[str] = {'Abhishek', 'Anna', 'Andrew'}
student_names.add('Abhishek')
student_names.add('Avatara')
student_names.add('Alvaro')

ta_names : set[str] = {'Ritik', 'Ankita', 'Sia', 'Alvaro'}

# TODO: Demo of set operations: union, intersection, difference, (strict) subset
print(student_names | ta_names)
print(student_names & ta_names)
print(student_names - ta_names)
print({'Andrew'} < student_names)
print(student_names <= ta_names)



# Using a set constructor, its argument needs to be iterable, so that
# its elements can be extracted and added to the set
letters : set[str] = set('Anna')

# Creating a dictionary by listing entries literally
# Here: str -> list[str]
students_by_first : dict[str, list[str]]= {
    'a' : ['Abhishek', 'Anna', 'Andrew'], 
    'c' : ['Camryn'], 
    'd' : ['Diigant']
    }

print(f'dict of student names: {students_by_first}')

students_by_first['a'].append('Avatara')  # this is why values were lists
students_by_first['i'] = ['Ilisha']

print(f'set of student names: {student_names}')
print(f'dict of student names: {students_by_first}')

print('Iterating over the dictionary and accessing its key:value pairs...\n')
for key, value in students_by_first.items():
    print(f'key={key}, value={value}')

for key in students_by_first:
    print(f'key={key}, value={students_by_first.get(key)}')


# Filter student and TA names by length of their name

print(f'students and tas: {student_names | ta_names}')
short_names = filter(lambda x: len(x) <= 6, student_names | ta_names)

# As result is an iterator, it's lazily generating each name, one at a time
# we need to iterate over it to get the results
print('students and tas with short names: ')
for s in short_names:
    print(s, end='; ')

# Note that the code above iterates over it in its entirety!!
# So we can't continue to use short_names, unless we recreate it.

# Using a generator expression to get the same results as filter
short_names = (s for s in student_names | ta_names if len(s) <= 6)

# Map the short names to all lowercase
short_lowercase_names = map(lambda x: x.lower(), short_names)

print('\n\nstudents and tas with short names in lowercase: ')
for s in short_lowercase_names:
    print(s, end='; ')

# We need the short names again as it was already iterated over
# This is a demo... it's not the kind of thing that should be 
# created over and over!
short_names = (s for s in student_names | ta_names if len(s) <= 6)

# You will find code that uses filter() and map(), however, 
# more recent features of Python are preferred. Specifically,
# use generator expressions. E.g. for the map():

short_lowercase_names = (x.lower() for x in short_names)

