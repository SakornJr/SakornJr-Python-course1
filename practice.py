#Hello = "HelloEDco"
#total = 0
#for x in Hello:
#  total += 1
#   print(x)
#print(total) 

#print(len(Hello))


# -------
#  -----
#   ---
#    -

height = int(input("layer of triangle"))
for layer in range(height, 0, -1):
    spaces = height - layer
    triangle = 2*layer -1
    print(' ' * spaces + '*' * triangle)




