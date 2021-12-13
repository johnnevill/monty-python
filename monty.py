import random as rand
import pandas as pd
import numpy as np

wincounter = 0
gamecounter = 0
for i in range(5000):
    #set up game
    montypossibilities = {1:[0,0,1],2:[1,0,0],3:[0,1,0]}
    montydf = pd.DataFrame(montypossibilities[rand.randint(1,3)], columns=["door"])
    
    #choose a door, capture value
    chosendoor=np.random.choice(montydf.index, 1, replace=False)[0]
    chosendoorvalue = montydf.iloc[chosendoor,0]
    
    #remove a non-winning unchosen door
    unchosendoors = montydf.drop(chosendoor)
    removeddoor = np.random.choice(unchosendoors[unchosendoors["door"]==0].index, 1, replace=False)
    montydf2 = montydf.drop(removeddoor)
   
    #Switch the chosen door
    chosendoor2 = montydf2[montydf2.index != chosendoor].index[0]
    chosendoor2value = montydf.iloc[chosendoor2,0]
    
    #gory details:
    #print("Picked door " + str(chosendoor) + " with value " + str(chosendoorvalue) + "; Door " + str(removeddoor[0]) + " removed. Switched to door " + str(chosendoor2) + " with value: " + str(chosendoor2value))
    
    #capture games and wins
    gamecounter+=1
    if chosendoor2value == 1:
        wincounter+=1

#report findings:
print(str(gamecounter) + " games played\n" + str(wincounter) + " games won.\nWin percentage: " + str((wincounter/gamecounter)*100) + "%")
