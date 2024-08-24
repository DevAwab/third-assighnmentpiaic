#all programs of the assighnment
#age according to the year
from datetime import datetime
current_year=datetime.now().year
birth_year = int(input("enter your birth year:"))
age=current_year-birth_year
print(age)


#programe to calculate area of rectangle
length:int=int(input("Enter the length:"))
width:int=int(input("Enter the width:"))
Area=length*width
print(Area)

#calculates the area of circle
import math
radius=float(input("Enter the radius of the circle:"))
area=math.pi*radius*radius
print("Area of the circle is:{0}".format(area))

#writes a program that calculates the area of the cube
side=float(input("side="))

area=6*side*side
print("AREA=",area)

#converts farenheit to celcius and vise versa
F=float(input("F="))

celsiustofarenheit=(F-32)*5/9
print("celsius to Farenheit:",celsiustofarenheit)

#converts given number of seconds into minutes and second using variables
import math
S=float(input("S="))
secondstominute=S/60
print("SECONDS TO MINUTE=",secondstominute)

#write a program that calculates the percentage 
import math
numbers=float(input("numbers="))
total=float(input("total="))
percentage=numbers/total*100
print(percentage)

#write a program that calculates the bmi 

import math
weight=float(input("weight in kg="))
height=float(input("height in cm=",))
BMI=weight/height**2
print(BMI)

#program to calculate the volume of the cylinder
import math
r=float(input("r="))
h=float(input("h="))
Volume=math.pi*r**2*h
print(Volume)