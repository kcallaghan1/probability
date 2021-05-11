# import required modules
import random      
import sys
  
# function to generate dice throws    
def diceNumber():
    
      
    # this will enable to select a 
    # random number from 1 to 6
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
      
    # returns the diceNumber values 
    # in the form of tuple
    return (die1, die2)  
  
# function to get dice sum  
def twoDice(dices):
    die1, die2 = dices
    print("player- the sum of numbers you have got in die 1 and die 2 are {} + {} = {}".format(die1, die2, sum(dices)))
  
def play(): 
    # calling the diceNumber function to get a value
    # return the roll and then store that 
    # value in value.
    value = diceNumber()
    twoDice(value)
    
    # using the sum function in value to 
    # find the sum of two outcomes.
    sum_of_dices = sum(value)
    
    
    # find if sum of dices is 7 or 11 to determine the result.
    if sum_of_dices in (7, 11):
        result = 1
    
    # find if sum of dices is 2 , 3 , 12 to determine the result.
    elif sum_of_dices in (2, 3, 12):
        result = -1
        
    # if none of the cases worked above now we will 
    # play continously until we win or lose.    
    else:  
        result = 0
        currentpoint = sum_of_dices
    
    
    # game continues if you have not scored a 
    # total of 2 , 3 , 7 , 11 , 12 this will 
    # enable the game to continue in a loop until
    # the outcome is win or lose
    while result == 0:
        value = diceNumber()
        twoDice(value)
        sum_of_dices = sum(value)
        
        if sum_of_dices == currentpoint:
            result = 1
            
        elif sum_of_dices == 7:
            result = -1
    
    # when the outcome is clear,this will produce the 
    # outcome of the game
    if result == "congratulations you won":
        print("congratulations,you won")
        
    else:
        print("you lost, \ntry again next time")
    return result * 100



results = []
for i in range(1, 1000):
    results.append(play())
print(results)
print("Average: ", sum(results)/len(results))