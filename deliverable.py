# ALL README Material gets tested here

# 1
idx = "abcde".index("d")
idx = idx + 11
print(idx)
idx * 2
print(idx)

# 2
num = 33
isEven = num % 2 == 0
print(isEven)
print(not isEven)

# 3
str1 = 'marker'
num = len('whiteboard') - len(str1)
print(num)
str2 = 'bootcamp'
print(str2[num].upper())
char = str2[num].lower()
print(char + '!')

# 4
sentence = 'welcome to bootcamp prep'
lastChar = len(sentence) - 1
print(lastChar)
print(sentence[lastChar])

# 5
age = 30
if age > 30:
    print('older than 30')
else:
    print('younger than 30')


# 6
str = 'pizza'
if len(str) > 10:
    print('long string')
else:
    print('short string')
if str[0] == 'p':
    print('starts with p')

# 7
num = 15
if num % 3 == 0:
    print('divisible by 3')
elif (num % 5 == 0):
    print('divisible by 5')

# 8
num = 15
if num % 3 == 0:
    print('divisible by 3')
if num % 5 == 0:
    print('divisible by 5')

# 9
str = 'General Assembly'
if str[0] == str[0].capitalize():
    print('starts with a capital')

if str[len(str) - 1] == str[len(str) - 1].capitalize():
    print('ends with a capital')

# 10
num = -44
if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print(0)

if num % 2 == 0:
    print('even')
else:
    print('odd')

# Task 4

num = 11
if num > 5:
    print('if')

num = 5
if num > 5:
    print('if')
else:
    print('else')


num = 0
if num < 0:
    print('if')
elif num > 0:
    print('elif')
else:
    print('else')


# Task 5

def say_hello(name):
    msg = 'Hello, ' + name + '. How are you?'
    return msg


print(say_hello('bootcamp prep'))


def check_number(num):
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return 'zero'


print(check_number(5))


def fizz_buzz_1(max):
    for i in range(max):
        if i % 3 == 0 and i % 5 != 0:
            print(i, 'fizz')
        elif i % 5 == 0 and i % 3 != 0:
            print(i, 'buzz')
        elif 1 % 5 == 0 and i % 3 == 0:
            print(i, 'fizzbuzz')


fizz_buzz_1(30)


def even_caps(sentence):
    new_sentence = ""
    for i in range(len(sentence)):
        char = sentence[i]
        if i % 2 == 0:
            capital_char = char.upper()
            new_sentence += capital_char
        else:
            new_sentence += char
    return new_sentence


print(even_caps("Hello World"))
