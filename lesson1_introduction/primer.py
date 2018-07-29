print(1/4)
print(1//4)
print()

# lists
lst = [3, 2, 7, 1, 5]
print(lst[1])
print(lst[2:4])
print(lst[:2])
print(lst[2:])
print(lst[:-1])
print(sorted(lst))
print(lst)
lst.sort()
print(lst)
print()

# tuples
# tuples are immutable
tup = ("hi", 2, lst)
print(tup)
print()

# dictionaries
employees = {'Jon': 42, 'Anne': 53213}
print(employees)
employees['Elissa'] = 7821
print(employees)
print('Jon' in employees)
print('Mary' in employees)
print(employees['Elissa'])
# print(employees['test']) # exception
print(employees.get('test'))  # no exception
del employees['Jon']
print(employees)
print(employees.items())

tup2 = ('Jonathan', 'Dinu')  # we can use tuples as keys since they are immutable
employees[tup2] = 21235
print(employees)
print()

# sets
sentence1 = {'the', 'red', 'panda', 'jumped', 'over', 'the', 'red', 'barn'}
sentence2 = {'the', 'red', 'fox', 'jumped', 'over', 'the', 'brown', 'fence'}
print(sentence1)
print('fox' in sentence1)
print('panda' in sentence1)
print(sentence2 - sentence1)    # difference
print(sentence1 - sentence2)    # difference
print(sentence1 | sentence2)    # union (deduplicated)
print(sentence1 & sentence2)    # intersection
print()

# if else
myVar = 50
if myVar == 50:
    print('the universe makes sense')
elif myVar == 500:
    print('something else')
else:
    print('yet another something else')

print()

# ternary operator
result = 'first value' if myVar == 50 else 'second value'
print(result)
print()

# for
for item in lst[3:]:
    print(item)
print()
for idx in range(3):
    print(lst[idx])
print()
