#list
#list count like index[0]
#len() it's name
sports = ["football","basketball","ping-pong","golf"]
print(len(sports))

list1 = [1, 3, 5, 7, 9]
list2 = [True, False, True]

print(type(list1))
print(type(list2[2]))
#list() // []

print(sports[-1])
#golf
#(่ค่าที่เริ่มนับ) : (ค่าที่ไม่นับ)

print(sports[1:3])
#['basketball', 'ping-pong']
print(sports[:3])
#['football', 'basketball', 'ping-pong']
print(sports[1:])
#['basketball', 'ping-pong', 'golf']

sports[1] = "Baseball"
#['football', 'Baseball', 'ping-pong', 'golf']
print(sports)

# .append()
sports.append("badminton")

# .insert
sports.insert(1, "swimming")

# .extend
sports2 = ["muaythai", "taekwondo","running"]
sports.extend(sports2)
print(sports)

# .remove()
sports.remove("football")
print(sports)

# .pop()
sports.pop()
print(sports)

