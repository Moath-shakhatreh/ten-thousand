from ten_thousand.game_logic import GameLogic


class Game(GameLogic):
  
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

# def play(roller,num_rounds):
#     Game.play(num_rounds)



