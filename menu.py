class menu:
    def main_menu(self):
        print ("choose an option:")
        print("1. Start game")
        print("2. Show players list")
        print("3. Exit")
        choice = input("Enter your choice: ")
        return choice
    def end_game_menu(self):
        print ("choose an option:")
        print("1. Play again")
        print("2. Show players list")
        print("3. Exit")
        choice = input("Enter your choice: ")
        return choice
    
    def welcome_message(self):
        print ("Welcome to tic-tac-toe game")
        print ("----------------------------")
        print ("")