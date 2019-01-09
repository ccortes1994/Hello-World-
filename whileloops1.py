# '''
# 1) Swap two variables
# 2)fibonacci sequence
# '''
#
# a = 5
# b = 10
# print(' the value in a = ',a,' and the value in b = ',b)
#
# #  create a temporary var to store a
# temp = a
# a = b     # assign the value b to var a
# b = temp  # assign the temp var(former value of a)
# print(' the value in a = ',a,' and the value in b = ',b)

# while loop
#
# x = 1
#
# while x < 10:
#     print(x, end='  ')
#     x = x + 1

# cont = 'c'
#
# while cont == 'c':
#     print(' the world is beautiful')
#
#     cont = input('do you want to keep going? press c, otherwise, press any key')
#

# fibonacci sequence

x = 1
y = 1
cont = 'c'
while cont == 'c':
    print(' the fibon number is ',x + y)
    temp = x
    x = y
    y = y + temp

    cont = input('if you want more febon numbs press c, else press any key')






