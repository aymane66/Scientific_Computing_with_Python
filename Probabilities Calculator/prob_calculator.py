import copy
import random

class Hat:
    def __init__(self, **user_input):
        self.contents = []
        for key, value in user_input.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        balls_drawn = []
        if number >= len(self.contents):
            return self.contents

        for i in range(number):
            ball_picked = random.choice(self.contents)
            balls_drawn.append(ball_picked)
            self.contents.pop(self.contents.index(ball_picked))

        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_result = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        actual = hat_copy.draw(num_balls_drawn)
        actual_dict = {ball: actual.count(ball) for ball in actual}

        result = True
        for key, value in expected_balls.items():
            if actual_dict.get(key, 0) < value:
                result = False
                break

        if result:
            num_result += 1

    return num_result / num_experiments
