"""
find the number of digits in given integer
"""

num = int(input("enter the number :")) # enter a number from keyboard

exp = 1 # start with eponent 1 for the powerf 10
        # to compare your number with 10**exp
while num > 10**exp : # check the while loop condition

    exp = exp + 1 # if condition true execute the loop's body
                  # increasee exp by 1
print(num,"has",exp,"digits")  # once the condition is false,
                               # exit the while loop