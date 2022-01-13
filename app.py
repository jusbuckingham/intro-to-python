# this is a comment
# TODO built this fucntion

def add(num, num2):
    '''
    this is supposed to add 2 numbers
    '''

name = "Johnny"

nothing = None

is_working = True
car_off = False

if nothing: 
    print('This is true')
    num = 7
    print('car is off')
elif car_off:
    print('this is the second condition')
    print('this will run if car_off is True')
elif is_working:
    print('This is working')
else: 
    print('This is not true... ')

# this is another conditional

if is_working:
    print('this is working also')

# conditional --> this first item that represents 
# True, it runs that indented [block]

print(15 / 6)
print(15 // 6)

print("ace of spades".split( " "))

print("ace-of-spades".split("-"))

print("ace.ofs.pades".split("."))

my_scare = "boo"
my_scare.upper()

print("eggs" in "green eggs and ham")

food = "eggs"
print(food in "green eggs and ham")
print(len(food))

statement = "my code rules"[3:9]
print(statement)

if 7 != 7:
    print('These are euqal, duh...')
else:
    print('This is the second condition')

location = "Michgan"
number = "11"
my_message = f"{location} is the {number}th largest state"
print(my_message)

topic ='The Drama'
num = 21
y = 1984
my_second_message = "{} is at {} percent.  Highest since {}".format()
print(my_second_message)