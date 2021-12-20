a = input('Please select a sign (+, -, *, /): ')

b = input('First number: ')
c = input('Second number: ')

b = int(b)
c = int(c)

def plus():
    bc = b + c
    print(bc)

def minus():
    bc = b - c
    print(bc)

def multiplication():
    bc = b * c
    print(bc)
def division():
    bc = b / c
    print(bc)

if a == '+':
    plus()
elif a == '-':
    minus()
elif a == '*':
    multiplication()
elif a == '/':
    division()

