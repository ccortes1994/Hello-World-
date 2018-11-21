"""
Using the keyboard input
input()
"""
a = int(input("enter the number : "))

print(a)

b = int(input("enter a second number :"))
print(b)

print(a + b)

num = int(input("enter the number : "))
if num%2==0:
    print("number",num,"is even")
else:
    print("number ",num," is odd")





# Error in line 28 
num = int(input("enter the number :"))

exp = 1
while num> 10**exp :
    exp = exp +1

print(num,"has ", exp,"digits")
