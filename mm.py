import random
from collections import Counter

    

class GameLogic:

    def __init__(self):
        pass

    
      
    def roll_dice(number=6):
        '''
        return the result of throwing number of dices
        the nubmer of dices based on the input number  
        '''
        return tuple(random.randint(1, 6) for _ in range(number))
      

    @staticmethod
    def calculate_score(roll):
        """
        Calculates the score based on the given roll.
    
        Args:
            roll (tuple): A tuple representing the dice roll.
    
        Returns:
            int: The calculated score.
    
        """
        score = 0
        counts = [roll.count(i) for i in range(1, 7)]
    
        if counts == [1, 1, 1, 1, 1, 1]:
            # Check for a straight (1, 2, 3, 4, 5, 6)
            score = 1500
            return score
    
        if counts.count(2) == 3:
            # Check for three pairs
            score += 1500
            return score
    
        if counts[0] <= 2:
            # Check for individual 1s
            score += counts[0] * 100
    
        if counts[4] <= 2:
            # Check for individual 5s
            score += counts[4] * 50
    
        if 3 in counts:
            # Check for three of a kind
            if counts.count(3) == 2:
                # Two sets of three of a kind
                location = counts.index(3) + 1
                location2 = counts[location::1].index(3) + location + 1
                if location == 1:
                    score += location * 1000
                else:
                    score += location * 100
                score += location2 * 100
            else:
                location = counts.index(3) + 1
                if location == 1:
                    score += location * 1000
                else:
                    score += location * 100
    
        elif 4 in counts or 5 in counts or 6 in counts:
            # Check for four, five, or six of a kind
            maxx = max(counts)
            a = 0
            location = counts.index(maxx) + 1
            if location == 1:
                for i in range(3, maxx + 1):
                    a += 1000
            else:
                for i in range(3, maxx + 1):
                    a += (location * 100)
            score += a
    
        return score
    
    
    def string_to_tuple(string):
      '''
      this finction transfer user unputs when he choose the dices 
      that he want to calculat its score to a tupile 
      '''
      string = string.strip()
      tuple_value = tuple(int(digit) for digit in string)
      return tuple_value


    
    def mock_roller():
            '''
            this function have two default then it will lunch 
            roll_dice function ,we willuse it to match the scenario  
            '''
            rolls = [(3,2,5,4,3,3),(5,2,3,2,1,4)]
            return rolls.pop(0) if rolls else GameLogic.roll_dice(6)
    


    @classmethod
    def startGame(cls):
        '''
        this function will lunch the game Ten Thousend
        based on some algorethims
        '''
         
        print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline you can't enter other thing")
        userInputs = input(' >')

        while userInputs != 'q':
            # initilaise two variables for rounds number and the total score 
            if userInputs.lower() == 'y':
                roun = 0
                total = 0
            elif userInputs.lower() == 'n': 
                print("OK. Maybe another time")
                return 

                                 
            roun += 1
            while True:
                dice=cls.mock_roller()                # insert the result of throwing 6 dices inside a variable
                dices="*** "                         
                for i in dice:
                    dices+=str(i)+" "
                dices = dices + '***'                # showing the result as a string
                print(f"Starting round {roun}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
                userInputs=input("> ")
                while userInputs == 'b':              # in case if the user inter b in the first(when he don't have any points to bank)
                    print('you have no points to bank \nEnter dice to keep or (q)uit')
                    userInputs=input("> ")
                if userInputs != 'r' :
                    break
                    
                
     
            if userInputs.lower() != 'q' and userInputs !='r' :
                input_1=cls.string_to_tuple(userInputs.strip())     # transfeer user inputs to tupile
                score= cls.calculate_score(input_1)                 # calculate the choiced dices
                print(f"You have {score} unbanked points and {6-len(input_1)} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
                userInputs = input(' >')
                remaining = 6-len(input_1)                          # calculate number of remaining dices
          

            if userInputs.lower() == 'b' :
                total = total + score
                print(f"You banked {score} points in round {roun}\nTotal score is {total} points\n")


            while userInputs.lower() == 'r':

                if remaining == 0 :                                  # number in case there is no more dices to reroll
                    break
                dice=cls.roll_dice(remaining)
                dices="*** "
                for i in dice:
                    dices+=str(i)+" "
                dices = dices + '***'                                # showing the result as a string
                print(f"You have {score} unbanked points and {remaining} dice remaining \n{dices}\nEnter dice to keep, or roll again or (q)uit:")
                userInputs = input(' >') 

                if userInputs.lower() != 'r' and userInputs.lower() != 'q' and userInputs.lower() != 'b':        
                    input_1=cls.string_to_tuple(userInputs.strip())   
                    score=score + cls.calculate_score(input_1)           # calculate the choiced dices
                    remaining = remaining - len(input_1)
                    print(f"You have {score} unbanked points and {remaining} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
                    userInputs = input('> ')
                    total = total + score

                

                if userInputs.lower() == 'b' :
                    print(f"You banked {score} points in round {roun}\nTotal score is {total} points\n")

            
        print (f"Thanks for playing. You earned {total} points")
        return






if __name__ == '__main__':
    

    GameLogic.startGame()
    # x= GameLogic.roll_dice(6)
    # print(x)
    # print(GameLogic.calculate_score(x))
    # print(GameLogic.string_to_tuple('5568 '))
    # print(GameLogic.calculate_score((5,5)))

    # rolls = [(5,6),(6,1),(1,1),(1,2)]
    # play_dice(mock_roller)

