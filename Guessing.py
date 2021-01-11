import random
#Variables Intialization 
user_entry=0
playgame='y'
trail_numbers=0
secret_number=0
#loop through user choices 
while playgame.lower()=='y':
    # if user want to play the trials_number should be 0
    if trail_numbers==0 and playgame.lower()=='y' :
        # generate the secret 
        secret_number=random.randint(0,10)
         # for first time app will ask user the trails numbers
        trail_numbers=int(input('Please enter the number of trails 0-10 '))
        # if user want the app to give him random number of trails.
        if trail_numbers==0:
            trail_numbers=random.randint(0,10)
            print('You have ', trail_numbers , ' trails. ')
    # if there is trials available
    if trail_numbers>0 and trail_numbers<=10:
            user_entry=int(input('Enter the secrete number '))
            trail_numbers-=1
            if trail_numbers==0:
                print('Huh! You loose... Game Over!')
                print ('The secret Number is ', secret_number)
                playgame=input('Would you like to play again Y/N ? ')
            #check user guessing
            if user_entry==secret_number:
                print('You catch me! The secrete number is ', secret_number)
                trail_numbers=0
                playgame=input('Would you like to play again Y/N ? ')
    else:
        #user enter wrong trail numbers
        trail_numbers=int(input('OOps...Please enter the number of trails 0-10 '))