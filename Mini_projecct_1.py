import random

hp_player = int(random.randint(100, 150))

hp_ai = int(random.randint(100, 150))



print("Your hp is", hp_player)

print("1 is for Attack")
print("2 is for Increase HP")

while hp_player >= 0 and hp_ai >= 0:
    
    damage_player = int(random.randint(1, 15))
    damage_ai = int(random.randint(1, 15))
    choose = str(input("1 or 2"))
    result_player_attack = hp_ai - damage_player
    new_hp_player = int(random.randint(1, 20))
    result_player_Increase_hp = new_hp_player + hp_player
    
    ai_choice = int(random.randint(1, 2))
    result_ai_attack = hp_player - damage_ai
    new_hp_ai = int(random.randint(1, 20))
    result_ai_Increase_hp = new_hp_ai + hp_ai
    
   
    
    
    
    if choose == "1" :
        print("Your opponent hp =", result_player_attack )
    elif choose == "2" :
        print("Your hp has increased to",result_player_Increase_hp)    
        
    if ai_choice == 1 :
        print("Your opponent attacked you, your hp is now",result_ai_attack)
    elif ai_choice == 2 :
        print("Your opponent hp has increased to", result_ai_Increase_hp)
        
    if hp_player <= 0 and hp_ai <= 0:
        break
    else:
        continue        
    
    