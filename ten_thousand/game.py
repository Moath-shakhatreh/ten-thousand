from ten_thousand.game_logic import GameLogic


class Game(GameLogic):
  
    def play(self):
        GameLogic.startGame()


# def play(roller=GameLogic.roll_dice, num_rounds=20):

#     game = Game(roller, num_rounds)
#     game.play()
    
# if __name__ == "__main__":
#     Play()