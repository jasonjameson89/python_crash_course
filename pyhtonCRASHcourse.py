#Variables and data types:

print('hello world')

message = 'hello world message'
print(message)


#Strings

x = 'this is strings text'
y = 'thisisstringtext'
z = 'this is also 123 string text'
xyz = '123123'
print(x,y,z,xyz)


#String manipulation

#lowercase
#uppercase
x = 'Message'
print(x.lower())
print(x.upper())

#Using variables in strings

x = 'jason'
y = 'jameson'
print('hello ' + x + ' ' + y + '.' )

#Using Fstrings

a = '1'
b = '2'
c = '3'
x = f'{a}{b}{c}'
print(x)

#more

a = 'asd'
b = 'dsa'
x = f'{a} {b}'
print(x.title())

x = ('ASDASDsadas')
y = ('32')
z = x.lower()
print(f'{z.title()} {y}')


#stripping white space

a = 'asdas asda sdasd                 '
print(a.rstrip())
print(a.lstrip())
print(a.strip())

#using escape characters

print('h\ne\nl\nl\no\n')








