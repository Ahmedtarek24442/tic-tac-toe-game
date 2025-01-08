class board:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def display_board(self):
        for row in self.board:
            print("-" * 19)
            for i,col in enumerate(row):
                if i == 0:
                    print("| ",col, " ", end="|")
                else:
                    print(" ",col, " ", end="|")

            print()
        print("-" * 19)
