import random
ucl_Teams=['Ballyhale', 'Bennettsbridge', 'Clara', 'Dicksboro', 'Erins Own', 'GBC', 'Glenmore', 'James Stephens', 'Lisdowney', 'Mvat', 'OLG', 'Tullaroan']


    
    print ("Teams: ", ucl_Teams) # prints out the teams in alphabetical order
    random.shuffle(ucl_Teams) # shuffles the teams (this is effectively the "draw")

    
    print('\nThe two groups are: \n')
    print (ucl_Teams[0:6])
    print (ucl_Teams[6:])

def championship_draw():
    random.shuffle(ucl_Teams)

    print('\nChampionship Draw \n')       
    print ('Match 1',(ucl_Teams[0:2]))
    print ('Match 2',(ucl_Teams[2:4]))
    print ('Match 3',(ucl_Teams[4:6]))
    print ('Match 4',(ucl_Teams[6:8]))
    print ('Match 5',(ucl_Teams[8:10]))
    print ('Match 6',(ucl_Teams[10:]))
    

championship_draw()
