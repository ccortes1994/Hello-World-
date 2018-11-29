"""
convert from F to C, and from C to F
"""
degree = input("Enter C for Celsius, or F for Fahrenheit :")
temp = int(input(" Enter the temperature value :"))

if degree == 'F' :
    C = ( temp - 32)*5/9
    print(" The converted temp in Celsius is : ", round(C))

elif degree == 'C' :
    F = temp*9/5 + 32
    print("The converted temp to Fahrenheit is : ")

else :
    print("There is no such type of degree :", degree)
exit()
