from os import path
from random import choice


class RockPaperScissors:
    def __init__(self):
        self.default_options = ['paper', 'scissors', 'rock']
        self.score = 0
        self.user_name = ''
        self.file_name = 'rating.txt'

    def open_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                name, score = line.split()
                if name == self.user_name:
                    self.score = int(score)

    def start_game(self):
        self.user_name = input("Enter your name: ")
        print(f"Hello, {self.user_name.title()}")
        if path.exists(self.file_name):
            self.open_file(self.file_name)
        custom_options = input("Enter list of options. " \
                               "If you want to play choosing default ones, press Enter")
        if custom_options:
            self.default_options = custom_options.split(',')
        print("Enter !exit to exit, !rating to see rating or one of the following options to play:")
        print(*self.default_options)
        while True:
            user_input = input()
            if user_input == '!exit':
                print("Bye!")
                break
            elif user_input == '!rating':
                print(f"Your rating: {self.score}")
                continue
            elif user_input not in self.default_options:
                print("Invalid input")
                continue
            else:
                user_index = self.default_options.index(user_input)
                modified_list = self.default_options[user_index + 1:] + self.default_options[:user_index]
                half_list = len(modified_list) // 2
                pc_input = choice(self.default_options)
                if user_input == pc_input:
                    print(f"There is a draw ({pc_input})")
                    self.score += 50
                elif pc_input in modified_list[half_list:]:
                    print(f"Well done. The computer chose {pc_input} and failed")
                    self.score += 100
                else:
                    print(f"Sorry, but the computer chose {pc_input}")


if __name__ == '__main__':
    game = RockPaperScissors()
    game.start_game()
