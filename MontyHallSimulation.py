import random

counter=0
runs=int(input("enter depth of simulation "))
doors=int(input("enter how many doors "))
Sheesh=range(int(doors))
Ranger=[*Sheesh]
Ranger.remove(0)
Ranger.append(int(doors))
for i in range(runs):
    fullrange=Ranger.copy()
    answer=int(random.choice(fullrange))
    guess=int(random.choice(fullrange))
    fullrange.remove(guess)
    if guess is not answer: fullrange.remove(answer)
    removed=int(random.choice(fullrange))
    choosefrom=Ranger.copy()
    choosefrom.remove(removed)
    choosefrom.remove(guess) #force switch
    reguess=int(random.choice(choosefrom))
    if reguess is answer:
        counter=counter+1
    #fullrange is the range of doors to pick from if switching is required

print("force switch",counter/runs)
switchcounter=0

for i in range(runs):
    fullrange=Ranger.copy()
    answer=int(random.choice(fullrange))
    guess=int(random.choice(fullrange))
    fullrange.remove(guess)
    if guess is not answer: fullrange.remove(answer)
    removed=int(random.choice(fullrange))
    choosefrom=Ranger.copy()
    choosefrom.remove(removed)
    reguess=int(random.choice(choosefrom))
    if reguess is answer:
        switchcounter=switchcounter+1
        
print("switchable",switchcounter/runs)
print("difference",(counter-switchcounter)/runs)
print("ratio",(counter-switchcounter)/counter)

