#Khan_Shahmeer CA-01.py October 2022 -- Vessel Draft calculator
#Input three values - Calculate draft of vessel – Output draft and echo inputs

#Input Section:

height = 0
length = 0
breadth = 0

#User input is converted into a float value as it allows both integer and decimal values to be used within the arithmetic processes
height = input("Please enter the height of the barge: ")
height = float(height)

length = input("Please enter the length of the barge: ")
length = float(length)

breadth = input("Please enter the breadth of the barge: ")
breadth = float(breadth)
print()

#Process Section
area_Wall = height*length*4
area_Floor = length*breadth
surface_Area = area_Wall+area_Floor

#The mass of iron is 1.06kg
mass_of_barge = 1.06*surface_Area
draft = mass_of_barge/area_Floor
#The area of the floor is technically length * width 



#Output Section: 
print("The height entered was:", height)
print("The lenght entered was:", length)
print("The breadth entered was:", breadth)
print("The surface area of the barge is:", surface_Area)
print("The mass of the barge is:", mass_of_barge)
print("The draft of the barge is:", draft)


# Test Table
#--------------------------------------------------
# h l b    expected draft  actual draft  comment
# 2 4 5         2.76          2.76       ok
# 3 5 6         3.18          3.18       ok
# 10 20 30      2.47          2.47       ok
# 2.5 3.5 4.5   3.42          3.42       ok
#10.5 11.5 12.5 4.62          4.62       ok

      
