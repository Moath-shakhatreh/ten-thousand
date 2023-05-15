import random
from collections import Counter

    

class GameLogic:

    def __init__(self):
        pass

    def roll_dice(number=0):
      '''
      return the result of throwing number of dices
      the nubmer of dices based on the input number  
      '''
      if number==0:
        return 0
      else:
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
        print(counts)
    
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

    
        
