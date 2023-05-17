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
        # print(counts)
    
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
      string = string.strip()
      tuple_value = tuple(int(digit) for digit in string)
      return tuple_value


    @classmethod
    def startGame(cls):
         
        print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline you can't enter other thing")
        userInputs = input(' >')

        while userInputs != 'q':

            if userInputs == 'y':
                roun = 0
                total = 0
                
            
            roun += 1
            dice=cls.roll_dice()
            dices="*** "
            for i in dice:
                dices+=str(i)+" "
            dices = dices + '***'
                
            
            print(f"Starting round {roun}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")

            userInputs=input("> ")
            
            if userInputs != 'q' :
                iinput=cls.string_to_tuple(userInputs.strip())   
                score1= cls.calculate_score(iinput)
                print(f"You have {score1} unbanked points and {6-len(iinput)} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
                userInputs = input(' >')
                remaining = 6-len(iinput)
          
            if userInputs == 'b' :
                total = total + score1 
                print(f"You banked {score1} points in round {roun}\nTotal score is {total} points\n")

            while userInputs == 'r':
                if remaining == 0 :
                    break
                
                dice=cls.roll_dice(remaining)
                dices="*** "
                for i in dice:
                    dices+=str(i)+" "
                dices = dices + '***'

                print(f"You have {score1} unbanked points and {remaining} dice remaining \n{dices}\nEnter dice to keep, or roll again or (q)uit:")
                userInputs = input(' >') 
                if userInputs != 'r' and userInputs != 'q' and userInputs != 'f':        
                    iinput=cls.string_to_tuple(userInputs.strip())   
                    score1=score1 + cls.calculate_score(iinput)  
                    total = total + score1
                    remaining = remaining - len(iinput)
                    print(f"You have {score1} unbanked points and {remaining} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
                    userInputs = input('> ')

                if userInputs == 'b' :
                    print(f"You banked {score1} points in round {roun}\nTotal score is {total} points\n")
                

            
      
        print (f"Thanks for playing. You earned {total} points")
        return  

        
    def mock_roller(self):
            rolls = [(3,2,5,4,3,3),(5,2,3,2,1,4)]
            return rolls.pop(0) if rolls else GameLogic.roll_dice(6)


if __name__ == '__main__':
    

    GameLogic.startGame()
    # x= GameLogic.roll_dice(6)
    # print(x)
    # print(GameLogic.calculate_score(x))
    # print(GameLogic.string_to_tuple('5568 '))
    # print(GameLogic.calculate_score((5,5)))

    # rolls = [(5,6),(6,1),(1,1),(1,2)]
    # play_dice(mock_roller)

