furniture = ['John', 'Peter', 'Debora', 'Charles']
furniture[0]
'John'
furniture[1]

'Peter'
furniture[2]
'Debora'
furniture[3]
'Charles'

furniture[-1]
'Charles'
furniture[-2]
'Debora'
furniture[-3]
'Peter'
f'{furniture[-1]} je rychlejší než {furniture[-3]}'
'Charles je rychlejší než Peter'
furniture[0:4]
['John', 'Peter', 'Debora', 'Charles']
furniture[1:3]
['Peter', 'Debora']
furniture[0:-1]
['John', 'Peter', 'Debora']
furniture[:2]
['John', 'Peter']
furniture[1:]
['Peter', 'Debora', 'Charles']
furniture[:]
['John', 'Peter', 'Debora', 'Charles']


spam = ['John', 'Peter', 'Debora', 'Charles']
spam2 = spam[:]
spam2
['John', 'Peter', 'Debora', 'Charles']
spam.append('Gabriel')
spam
['John', 'Peter', 'Debora', 'Charles', 'Gabriel']
spam2
['John', 'Peter', 'Debora', 'Charles']

len(furniture)
4

furniture[0] = 'Ivan'
furniture
['Ivan', 'Peter', 'Debora', 'Charles']
furniture[2] = furniture[1]
furniture
['Ivan', 'Peter', 'Peter', 'Charles']

