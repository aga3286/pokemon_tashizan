import random
class Calculator:
    def __init__(self):
        self.answered_list = []
        self.displayed_combination = [0, 0]
        self.displayed_answer = 0
        self.true_or_false = []

    def get_formula(self):
        duplicated = True
        while duplicated:
            i = random.randint(1, 9)
            j = random.randint(1, 9)
            if not {i, j} in self.answered_list:
                duplicated = False
                print(self.answered_list)
        self.displayed_combination[0] = i
        self.displayed_combination[1] = j
        self.displayed_answer = i + j
        if self.displayed_answer < 10:
            return f"{i} + {j} =   "
        else:
            return f"{i} + {j} =     "

    def check_answer(self, input_number):
        if self.displayed_answer == input_number:
            self.answered_list.append(set(self.displayed_combination))
        self.true_or_false.append(self.displayed_answer == input_number)




