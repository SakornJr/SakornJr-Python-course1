score = input(int("Enter your score ="))
if score >= 80 and score <= 100:
    print("Grade 4")
elif score >= 75 and score < 80: 
    print("Grade 3.5")  
elif score >= 70 and score < 75: 
    print("Grade 3")
elif score >= 65 and score < 70: 
    print("Grade 2.5")
elif score >= 60 and score < 65: 
    print("Grade 2")            
elif score >= 55 and score < 60: 
    print("Grade 1.5")
elif score >= 50 and score < 55: 
    print("Grade 1")
elif score < 50:
    print("Grade 0" )
else:
    print("Score error")                
