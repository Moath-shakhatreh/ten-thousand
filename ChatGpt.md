### prompt-01 : 
> create a GameLgic class with python 

- result : 
```python
class GameLogic:
    def __init__(self):
        self.players = []
        self.current_player = None
        self.game_over = False
    
    def add_player(self, player_name):
        self.players.append(player_name)
    
    def start_game(self):
        if len(self.players) < 2:
            print("At least 2 players are required to start the game.")
            return
        
        self.current_player = self.players[0]
        self.game_over = False
        print("Game started. Current player: ", self.current_player)
    
    def next_turn(self):
        if self.game_over:
            print("The game is already over.")
            return
        
        current_player_index = self.players.index(self.current_player)
        next_player_index = (current_player_index + 1) % len(self.players)
        self.current_player = self.players[next_player_index]
        print("Next turn. Current player: ", self.current_player)
    
    def end_game(self):
        self.game_over = True
        print("Game over.")
In this example, the GameLogic class represents the logic and functionality of a game. It maintains a list of players, tracks the current player, and determines if the game is over or not.

You can create an instance of the GameLogic class and interact with its methods like this:

python
Copy code
game = GameLogic()
game.add_player("Player 1")
game.add_player("Player 2")
game.add_player("Player 3")

game.start_game()
game.next_turn()
game.next_turn()
game.end_game()
This will output:

sql
Copy code
Game started. Current player:  Player 1
Next turn. Current player:  Player 2
Next turn. Current player:  Player 3
Game over.
Note that this is a basic example, and you can expand upon it by adding more game-specific functionality and rules to the GameLogic class as per your requirements.


```

### prompt-02 :
> create empty  GameLogic class  with method roll_dic that generate tuple of 6 random number between 1 to 6.
- result :
```python
import random
class GameLogic:
    def __init__(self):
        pass
    def roll_dice(self):
        return tuple(random.randint(1, 6) for _ in range(6))
This class initializes with an empty constructor (__init__), but you can add any necessary attributes or methods to it as your game develops. The roll_dice method uses Pythons built-in random module to generate a tuple of 6 random integers between 1 and 6 using a list comprehension and the randint function.
```

### prompt-03 :
> Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.
- result :
```python
import random


class GameLogic:
    @staticmethod
    def calculate_score(roll):
            score = 0 counts = [roll.count(i) for i in range(1, 7)]
            # Check for three-of-a-kind or better
            if 3 in counts or 4 in counts or 5 in counts or 6 in counts:
                score += sum(roll)
            else:
            # Check for individual ones and fives
                score += counts[0] * 100 + counts[4] * 50
            # Check for specific combinations
            if counts == [1, 2, 3, 4, 5, 6]:
                score = 1500
            elif counts == [2, 2, 2, 2, 2, 2]:
                score = 2500
            return score
    def __init__(self):
         pass
    def roll_dice(self):
         return tuple(random.randint(1, 6) for _ in range(6))
This implementation adds a calculate_score static method to the GameLogic class. The method takes in a tuple roll that represents a dice roll and computes the score according to the rules of the game. The logic of the calculate_score method is based on common scoring rules for the dice game called "Farkle."
The __init__ and roll_dice methods remain unchanged from the previous example.
```