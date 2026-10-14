import random
pas = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'   #password

len = input("whats is the length of your pasword?")
made=""
for i in range(int(len)):
    rand = random.choice(pas)               #random word/number
    
    made += rand                #adding them to the variable
    
print(made)