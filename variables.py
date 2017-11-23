'''Variables and data types'''

greeting = 'hello world'

greeting = 'hello everyone'#Reassisn, not append

print(greeting)


'''data types'''
'''string'''
myString = "hello"
'''integer'''
myInteger = 25

'''float'''
myFloat = 25.34

'''Python IS case sensitive'''
print(myFloat)

'''this is a list'''
myList = [1,2,3,'hello']

print(myList)

'''This is a dictionary'''
myDict = {'a':1,'b':2,'c':3}

'''functions'''

print(type(myString),myString)
print(type(myInteger),myInteger)
print(type(myFloat),myFloat)
print(type(myDict),myDict)
print(type(myList),myList)

print(myList[3])
print(myDict['a'])


print(myString,'world')

greeting = myString + ' world'
print(greeting)