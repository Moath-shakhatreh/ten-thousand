import random


class GameLogic:

    def __init__(self):
        self.dice = ()
        self.roun = 1
        self.total = 0
        self.remaining = 6
        self.score2 = 0
        self.score1 = 0
        self.dices = ''


    def check_userInput_2(self):
        if self.userInput.isdigit() :
            self.userInput = input('> ')
            valid_input = ['q','b','r']
            while True:
                
                if self.userInput not in valid_input:
                    print('invalid input')
                    self.userInput = input('> ')
                else:
                    return
        else:
            self.userInput = input('> ')
            return  


    def check_userInput(self): 

        valid_input = ['y','n']
        # valid_input = ['1','2','3','4','5','6','q','b','r',' ','y','n']
        while True:
            for x in self.userInput:
                if x not in valid_input:
                    print('invalid input')
                    self.userInput = input('> ')
                    continue
                else:
                    return


    def roll_dice(number=6):
      '''
      return the result of throwing number of dices
      the nubmer of dices based on the input number  
      '''
      if number < 1 or number > 6:
            raise ValueError("Number of dice must be between 1 and 6.")
      if number:
        return tuple(random.randint(1, 6) for _ in range(number))
      
    @staticmethod
    def get_scorers(dice):
        # dice= tuple(dice)
        all_dice_score = GameLogic.calculate_score(dice)
        if all_dice_score == 0:
            return tuple()
        scorers = []
        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i+1:]
            sub_score = GameLogic.calculate_score(sub_roll)
            if sub_score != all_dice_score:
                scorers.append(val)
        return tuple(scorers)

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
    
    
    def string_to_tuple(self):
      """
    Converts a string of digits to a tuple of integers.

    Args:
        string (str): The string of digits.

    Returns:
        tuple: A tuple of integers converted from the string.

      """
      
      tuple_value = tuple(int(digit) for digit in self.userInput.strip())
      return tuple_value


    def re_rolling(self):
        if self.userInput.strip().lower() == "r" :
                        
            print(f"Rolling {self.remaining} dice...")
            self.dice = self.roll_dice(self.remaining)
            self.dices = "*** "
            for i in self.dice:
                self.dices += str(i) + " "
            self.dices += "***"
            
            if self.Zelch(self)==True:
                self.score2 = 0
                print(f"You banked {self.score2} points in round {self.roun}\nTotal score is {self.total} points")

                self.roun += 1
                self.remaining = 6

                print(f"Starting round {self.roun}\nRolling 6 dice...")
                self.dice = self.roll_dice()
                self.dices = "*** "
                for i in self.dice:
                    self.dices += str(i) + " "
                self.dices += "***"
                print(f"{self.dices}")
                print('Enter dice to keep, or (q)uit:')
            else:
                print(f"{self.dices}")
                print('Enter dice to keep, or (q)uit:')   
            return True
        return
    
 
    def Zelch(self):
        '''
        check the dices if they are winning dices
        '''
        if self.calculate_score(self.dice) == 0 :
            self.dices = "*** "
            for i in self.dice:
                self.dices += str(i) + " "
            self.dices += "***"
            print(f"{self.dices}")
            print('''
****************************************
**        Zilch!!! Round over         **
****************************************
            ''')
            return True
        

    def validate_keepers(dice,input_1):
        '''
        check if the user is cheating or not by
        comparing between the user input and 
        the dices
        '''
        for x in input_1 :
            if input_1.count(x) > dice.count(x):
                return False
            else:
                return True


    def starting(self):
        if self.remaining == 6 and self.userInput.isdigit() == False and self.userInput != 'r':
                        
            print(f"Starting round {self.roun}")
            print('Rolling 6 dice...')
            self.dice = self.roll_dice()
            self.dices = "*** "
            for i in self.dice:
                self.dices += str(i) + " "
            self.dices += "***"
            print(f"{self.dices}")
            print("Enter dice to keep, or (q)uit:")
            if self.Zelch(self)==True:
                self.score2 = 0
                print(f"You banked {self.score2} points in round {self.roun}\nTotal score is {self.total} points")
                self.roun += 1
                self.remaining = 6
                return True
            
    
    def check(self):
        input_1 = self.string_to_tuple(self)
                       
        if self.validate_keepers(self.dice,input_1) is True:
            pass

        else:
            while self.validate_keepers(self.dice,input_1) is False:
                print("\nCheater!!! Or possibly made a typo...\n")
                print(f"{self.dices}")
                print("Enter dice to keep, or (q)uit:")
                self.userInput = input('> ')
                if self.userInput is 'q':
                    break
                input_1 = self.string_to_tuple(self)
            
        if self.userInput != 'q':
            self.score1 = self.calculate_score(input_1)
            self.remaining -= len(input_1)
            self.score2 += self.score1
            if self.remaining != 0 :
                print(f"You have {self.score2} unbanked points and {self.remaining} dice remaining")
                print(f"(r)oll again, (b)ank your points or (q)uit:")
            else:
                self.remaining = 6
                print(f"You have {self.score2} unbanked points and {self.remaining} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")


    def mock_roller(self):
        '''
        we use this function to test these two result
        in first two rolling after that the rsult of 
        rolling the dices will be random
        '''
        rolls = [(3,2,5,4,3,3),(5,2,3,2,1,4)]
        return rolls.pop(0) if rolls else GameLogic.roll_dice(6)


    @classmethod
    def play(self,num_rounds = 20):
        """
        Starts the Ten Thousand game.
        The method prompts the user to play the game or decline. If the user chooses to play,
        it initializes the game variables and starts the game loop. The loop allows the player
        to roll dice, keep dice, bank points, and continue playing until they decide to quit.
        Returns:
            None
        Raises:
            None
        """
        print("Welcome to Ten Thousand")
        print('(y)es to play or (n)o to decline')
        self.userInput = input('> ')
        self.check_userInput(self)
        
        while self.userInput != 'q':
            if self.userInput.strip().lower() == 'y':
                self.roun = 1
                self.total = 0
                self.remaining = 6
                self.score2 = 0
                self.userInput = ''


                while True :
                    self.score1 = 0

                    if self.roun > num_rounds :
                        print(f"Thanks for playing. You earned {self.total} points")
                        return

                    if self.starting(self) == True:
                        continue
 
                    self.check_userInput_2(self)

                    if self.userInput.strip().lower() == 'q':
                        print(f"Thanks for playing. You earned {self.total} points")
                        break
                    if self.userInput.strip().lower() == 'b' and self.score2 == 0:
                        print('\nYou have no points to bank \nEnter dice to Play or (q)uit\n')
                        continue
                    if self.userInput.strip().lower() == "r" and self.score2 == 0:
                        print("\nYou have to select a dice to re-roll first or (q)uit\n")
                        continue

                    if self.re_rolling(self) == True:
                        continue

                    if self.userInput.strip().lower() == 'b':
                        self.total += self.score2
                        print(f"You banked {self.score2} points in round {self.roun}\nTotal score is {self.total} points")
                        self.score2 = 0
                        self.roun += 1
                        self.remaining = 6
                        continue

                    if self.userInput.isdigit():
                        self.check(self)
                   
                        if self.userInput.strip().lower() == 'q':
                            print(f"Thanks for playing. You earned {self.total} points")
                            break
                    else:
                        print("\nInvalid input. Try again.\n")

            else:
                print("OK. Maybe another time")
                break


if __name__ == '__main__':

    GameLogic.play()

        
      

      
      






