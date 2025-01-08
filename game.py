import board
import menu
import players
import os
class game:
    def __init__(self):
        self.board = board.board()
        self.menu = menu.menu()
        #check info of player1
        name1 = input("Enter player1 name: ")
        while not name1.isalpha():
            print("name must contain only characters")
            name1 = input("Enter player1 name: ")
        sympol1 = input("Enter player1 sympol: ")
        while not (sympol1 == "X" or sympol1 == "O" or sympol1 == "x" or sympol1 == "o"):
            print("Invalid sympol")
            sympol1 = input("Enter player1 sympol: ")
        self.player1 = players.players(name1,sympol1)
        #check info of player2
        name2 = input("Enter player2 name: ")
        while not name2.isalpha():
            print("name must contain only characters")
            name2 = input("Enter player2 name: ")
        sympol2 = input("Enter player2 sympol: ")
        while not ((sympol2 == "X" or sympol2 == "O" or sympol2 == "x" or sympol2 == "o") and sympol2 != sympol1.lower() and sympol2 != sympol1.upper()):
            print("Invalid sympol")
            sympol2 = input("Enter player2 sympol: ")
        self.player2 = players.players(name2,sympol2)
        #start the game
        self.start_game()

    def start_game(self):
        
        choice = self.menu.main_menu()
        if choice == "1":
            os.system("cls")
            self.play_game()
        elif choice == "2":
            os.system("cls")
            
            self.show_players()
            self.start_game()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice")
            self.start_game()

    def play_game(self):
        menu.menu.welcome_message(self)
        player1 = self.player1.getname_name()
        player2 = self.player2.getname_name()
        player1_sympol = self.player1.get_sympol()
        player2_sympol = self.player2.get_sympol()
        player1_turn = True
        player2_turn = False
        self.board.display_board()
        while not self.check_win() and not self.check_draw():
            if player1_turn:
                
                x = 0
                #check if the cell is empty or invalid input
                while x == 0:
                    try:
                        pos = int(input(f"{player1}, select a cell (1-9): ").strip())
                        if pos < 1 or pos > 9:
                            print("Invalid position")
                            continue
                        self.board.board[(pos - 1) // 3][((pos - 1) % 3)] = player1_sympol
                        player1_turn = False
                        player2_turn = True
                        os.system("cls")
                        menu.menu.welcome_message(self)
                        self.board.display_board()
                        x = 1
                    except:
                        x = 0
                        print("Invalid input")

            elif player2_turn:
                #check if the cell is empty or invalid input
                x = 0
                while x == 0:       
                    try:
                        pos = int(input(f"{player2}, select a cell (1-9): ").strip())
                        if pos < 1 or pos > 9:
                            print("Invalid position")
                            continue
                        self.board.board[(pos - 1) // 3][((pos - 1) % 3)] = player2_sympol
                        player1_turn = True
                        player2_turn = False
                        os.system("cls")
                        menu.menu.welcome_message(self)
                        self.board.display_board()
                        x = 1
                    except:
                        x = 0
                        print("Invalid input")
        
        self.board.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        #Do you wont to play again
        choice = self.menu.end_game_menu()
        if choice == "1":    
            os.system("cls")
            self.play_game()
        elif choice == "2":
            os.system("cls")
            self.show_players()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice")
            exit()

    def check_win(self):
        boardElements = self.board.board
        player1_sympol = self.player1.get_sympol()
        player2_sympol = self.player2.get_sympol()
        #check rows
        for row in boardElements:
            if row[0] == row[1] == row[2] == player1_sympol:
                print("Congrats ",self.player1.getname_name(),", you win!")
                self.player1.score += 1
                return True
            elif row[0] == row[1] == row[2] == player2_sympol:
                print("Congrats ",self.player2.getname_name(),", you win!")
                self.player2.score += 1
                return True
        #check columns
        for col in range(3):
            if boardElements[0][col] == boardElements[1][col] == boardElements[2][col] == player1_sympol:
                print("Congrats ",self.player1.getname_name(),", you win!")
                self.player1.score += 1
                return True
            elif boardElements[0][col] == boardElements[1][col] == boardElements[2][col] == player2_sympol:
                print("Congrats ",self.player2.getname_name(),", you win!")
                self.player2.score += 1
                return True
        #check diagonals
        if boardElements[0][0] == boardElements[1][1] == boardElements[2][2] == player1_sympol:
            print("Congrats ",self.player1.getname_name(),", you win!")
            self.player1.score += 1
            return True
        elif boardElements[0][0] == boardElements[1][1] == boardElements[2][2] == player2_sympol:
            print("Congrats ",self.player2.getname_name(),", you win!")
            self.player2.score += 1
            return True
        if boardElements[0][2] == boardElements[1][1] == boardElements[2][0] == player1_sympol:
            print("Congrats ",self.player1.getname_name(),", you win!")
            self.player1.score += 1
            return True
        elif boardElements[0][2] == boardElements[1][1] == boardElements[2][0] == player2_sympol:
            print("Congrats ",self.player2.getname_name(),", you win!")
            self.player2.score += 1
            return True

    def check_draw(self):
        boardElements = self.board.board
        for row in boardElements:
            for col in row:
                if col == "1" or col == "2" or col == "3" or col == "4" or col == "5" or col == "6" or col == "7" or col == "8" or col == "9":
                    return False
        print("It's a Draw!")
        return True
    
    def show_players(self):
        menu.menu.welcome_message(self)
        print("Player1: ", self.player1.getname_name())
        print("Symbol: ", self.player1.get_sympol())
        print("Score: ", self.player1.get_score())
        print("Player2: ", self.player2.getname_name())
        print("Symbol: ", self.player2.get_sympol())
        print("Score: ", self.player2.get_score())
        self.start_game()