class Question:
    def __init__(self, Que : str, ans : str):
        self.que = Que
        self.ans = ans
    def check(self, answer):
        if answer == self.ans:
            return True
        else:
            return False
q1 = Question("2 + 2 = 5\n", "true")
print(q1.check(input(q1.que)))

