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
     userInputs = ''
     print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline you can't enter other thing")
     userInputs = input(' >')
     while userInputs != 'q':
    #    print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline you can't enter other thing")
    #    userInputs=input("> ")
       roun=0
       if userInputs.strip()=="y":                  
        roun+=1
        dice=cls.roll_dice()
        dices="*** "
        for i in dice:
          dices+=str(i)+" "
        else:
          dices+="***"
        print(f"Starting round {roun}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
        userInputs=input("> ")
        total=0

        while userInputs.strip()!="q":
          iinput=cls.string_to_tuple(userInputs.strip())   
          score1=cls.calculate_score(iinput)
          print(f"You have {score1} unbanked points and {6-len(iinput)} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
          userInputs = input(' >')
          remaining = 6-len(iinput)
          

          if userInputs == 'b' :
             total = total + score1 
             print(f"You banked {score1} points in round {roun}\nTotal score is {total} points\nStarting round {roun+1}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
             break  

          while userInputs != 'b' and userInputs != 'q':
            if remaining == 0 :
                  break
            else:
              dice=cls.roll_dice(remaining)
              dices="*** "
              for i in dice:
               dices+=str(i)+" "
              print(f"You have {score1} unbanked points and {6-len(iinput)} dice remaining \n{dices}\nEnter dice to keep, or roll again or (q)uit:")
              userInputs = input(' >')             
              iinput=cls.string_to_tuple(userInputs.strip())   
              score1=score1 + cls.calculate_score(iinput)
            
              remaining = remaining - len(iinput)

              print(f"You have {score1} unbanked points and {remaining} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")

              userInputs = input('> ')

      
     print (f"Thanks for playing. You earned {score1} points")
     return 
        
       
      

              


          
        # if userInputs.strip()=="r":  
        #     dice=cls.roll_dice(remaining_dices)
        #     dices="*** "
        #     for i in dice:
        #       dices+=str(i)+" "
        #     else:
        #       dices+="***"
        #       score1=cls.calculate_score(dice)
        #     print(f"Starting round {roun}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
        #     userInputs=input("> ")
        #   if not userInputs.strip().isdigit():
        #     print(f"You can't enter any thing untile the dices")
        #     userInputs=input("> ")
        #   else:
            

            # if score2<=score1:
            #   print(f"You have {score1} unbanked points and {6-len(iinput)} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
            #   userInputs=input("> ")
            #   if userInputs.strip()=="b":
            #     total+=score1
            #     dice=cls.roll_dice()
            #     dices="*** "
            #     for i in dice:
            #       dices+=str(i)+" "
            #     else:
            #       dices+="***"
            #     print(f"You banked {score1} points in round {roun}\nTotal score is {total} points\nStarting round {roun+1}\nRolling 6 dice...\n{dices}\nEnter dice to keep, or (q)uit:")
            #     roun+=1
            #     userInputs=input("> ")
        
    # 

    

    # def play_dice(self,rolls = roll_dice()):
    
    #       while True:
    #           print("Enter r to roll or q to quit")
    #           choice = input("> ")
      
    #           if choice == "q":
    #               print("OK, bye")
    #               break
    #           else:
    #               roll = rolls(6)
    #               roll_str = ""
    #               for num in roll:
    #                   roll_str += str(num) + " "
    #               print(f"*** {roll_str}***")


    
        
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

      
    

    # @staticmethod
    # def calculate_score(dice):
    #     score = 0
    #     counter = Counter(dice)

    #     # Check for four of a kind
    #     for num, count in counter.items():
    #         if count >= 4:
    #             score += num * 200
    #             counter.subtract({num: 4})


    #     # Check for combinations
    #     if counter[1] >= 3:
    #         score += 1000
    #         counter.subtract({1: 3})

    #     for num in range(2, 7):
    #         if counter[num] >= 3:
    #             score += num * 100
    #             counter.subtract({num: 3})

    #     score += counter[1] * 100
    #     score += counter[5] * 50

    #     # Check for straight
    #     if len(counter) == 6:
    #         if set(counter.keys()) == {1, 2, 3, 4, 5, 6}:
    #             score = 1500

    #     return score
    
if __name__ == '__main__':
    pass
    # print(GameLogic.calculate_score())



    # def calculate_score(dice):
    #     score = 0
    #     counter = Counter(dice)

    #     # Check for combinations
    #     if counter[1] >= 3:
    #         score += 1000
    #         counter.subtract({1: 3})

    #     for num in range(2, 7):
    #         if counter[num] >= 3:
    #             score += num * 100
    #             counter.subtract({num: 3})

    #     score += counter[1] * 100
    #     score += counter[5] * 50

    #     return score

    
        
