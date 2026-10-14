
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


# # Filter student and TA names by length of their name

# short_names = filter(lambda x: len(x) <= 6, student_names | ta_names)

# # Map the short names to all lowercase
# short_lowercase_names = map(lambda x: x.lower(), short_names)

# for s in short_lowercase_names:
#     print(s)
