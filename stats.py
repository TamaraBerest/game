class Stats():
    # відслідковування статистики поточної гри

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        # статистика, яка змінюється під час гри
        self.guns_left = 2
        self.score = 0
