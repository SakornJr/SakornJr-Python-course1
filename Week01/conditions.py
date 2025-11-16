#if




a = 30 

b = 50

c = 70

e = 50

d = 100
 
"""  
   if [condition]:
      function


"""


if a < b:
    print("a is less than b")
    
#if...elseif
"""  
    if [condition]:
        function
    elif[condition]:
        function    
"""

if a > b:
    print("a is greater than b")
elif  c < b:
    print("c is less than b")
elif  b > d:
    print("b is greater than d")
elif b >= e:
    print("b is greater than e or equal")        

"""  
    if [condition]:
        function
    else:
    function    
"""


if  a > b:
    print("a is great than b")
else:
    print("a is not greater than b")
    
    
"""  
if [condition]:
    function
elif [condition]:
    function
else:
    function        
"""       

if c < b:
    print("c is less than b")
elif c < e:
    print("c is less than e")
else:
    print("It's not TRUE")        