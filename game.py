from random import choice


class TicTacToe:
    def __init__(self):
        self.game_list = ['paper', 'scissors', 'rock']
        self.win = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        self.score = 0
        self.user_name = ''

    def open_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.split()
                if data[0] == self.user_name:
                    self.score = int(data[1])

    def start_game(self):
        self.user_name = input("Enter your name: ")
        print(f"Hello, {self.user_name}")
        self.open_file('rating.txt')
        options = input()
        if options:
            self.game_list = options.split(',')
        print("Okay, let's start")
        while True:
            user_input = input()
            if user_input == '!exit':
                print("Bye!")
                break
            elif user_input == '!rating':
                print(f"Your rating: {self.score}")
                continue
            elif user_input not in self.game_list:
                print("Invalid input")
                continue
            else:
                user_index = self.game_list.index(user_input)
                new_list = self.game_list[user_index + 1:] + self.game_list[:user_index]
                half = len(new_list) // 2
                pc_input = choice(self.game_list)
                if user_input == pc_input:
                    print(f"There is a draw ({pc_input})")
                    self.score += 50
                elif pc_input in new_list[half:]:
                    print(f"Well done. The computer chose {pc_input} and failed")
                    self.score += 100
                elif pc_input in new_list[:half]:
                    print(f"Sorry, but the computer chose {pc_input}")


if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()
