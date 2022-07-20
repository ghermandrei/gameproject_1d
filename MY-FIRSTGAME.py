
from os import system

 
robot= 3
lenght = 20 
bomb = 8
bomb2 = 2
explosion = 0
roboHEALT= 100
roboBatery= 100
heart = 18
option= " "
start_over = " "
coins = 5
treasure = 0
########### GAME LOOP###########
while True:
    system("cls")
    print ("\n")
    ############ DRAWING MAP##########3 

    for i in range (-1,lenght+1):
       if i==robot:     ##### ROBOT INITIAL PLACE########
        print (" ♞ ",end=" ")
       elif i==bomb:
        print ('💣',end=" ")
       elif i== bomb2:
        print('💣',end="")
       elif i == heart:
        print('💚',end=" ") 
       elif i ==coins:
        print('💰',end="") 

       else :
    
        print ('*',end=" ")  

    print()

    print("\nRH",   roboHEALT)
    print("RB",     roboBatery,"%")
    print ("US", treasure,"$" )
    print (" \n")        

#############  DECIDE##############
    option = input (">>>  ")
############ DecidE #############


####### bomb damage  #######
    if robot == bomb or robot ==bomb2:
    
        roboHEALT -=10
    
    if roboHEALT == 0:
        system("cls")  
        print( "GAME OVER")  
        break
#######################################

##### Heart HP points ##########

    if robot == heart:
        roboHEALT +=10
#########################################

############ COINS ##############
    if robot == coins:
        treasure += 25
####################################


    if option == "a" and robot>-1: # move left
      robot -=1 
      roboBatery -=1 # battery consomption


    if option == "d" and robot < 20: #move right
      robot +=1
      roboBatery -=1 # battery consumption 

############### battery is out#########
    if roboBatery == 0:
        system("cls")
        print ('YOU ARE OUT OF BATTERY\nGAME OVER!!!')
        start_over= input("want to play again ? yes/no   ")
        if start_over == "yes":
         print("SORRY THIS IS ONE TIME GAME\nIF YOU WANT TO PLAY MORE\nBUY FROM ONLINE STORE " )
         break
        if start_over == "no" :
         print ("Thank you ")    
         break   

################################################d


       
    
    if option == "x"  :  ### stop game
        system("cls")
        print("thank you")
        break