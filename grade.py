""" 
score = 57

4 = 80-100
3.5 = 75-79 
3 = 70-74
2.5 = 65-69
2 = 60-64
1.5 = 55-59
1 = 50-54
0 = 0-49

"""


grade = float(input("Enter your score ->"))
if grade >= 80 and grade <= 100:
    print("Grade 4")

elif grade >= 75 and grade < 80:
    print("Grade 3.5")  
elif grade >= 70 and grade < 75:
    print("Grade 3")      
elif grade >= 65 and grade < 70:
    print("Grade 2.5")
elif grade >= 60 and grade < 65:
    print("Grade 2")
elif grade >= 55 and grade < 60:
    print("Grade 1.5")
elif grade >= 50 and grade < 55:
    print("Grade 1")
elif grade < 50 and grade >= 0:
    print ("Grade 0")    
else:
    print("Score Error")                