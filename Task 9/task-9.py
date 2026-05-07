class tictactoe:
    def __init__(self):
        self.board=[" " for _ in range(9)]
        self.human_p="O"
        self.ai_p="X"
    def print_board(self):
        for i in range(0,9,3):
            print(f' {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ')
            if i<6:
                print("-----------")
    def available_move(self):
        return[i for i, spot in enumerate(self.board) if spot==" "]
    def make_move(self,position,player):
        if self.board[position]==" ":
            self.board[position]=player
            return True
        return False
    def is_board_full(self):
        return " " not in self.board    
    def check_winner(self):
        for i in range(0,9,3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]
        for i in range(3):
            if self.board[i] == self.board[3] == self.board[6] != " ":
                return self.board[i]
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]
        return None

game=tictactoe()
# game.available_moves()
# [0,1,2,3,4,5,6,7,8]
# game.print_board()
# game.make_move(0,"X")
# game.make_move(1,"O")
# game.print_board()  
# game.available_move()
# [2,3,4,5,6,7,8]


                        #Winning moves
# game.make_move(0,"X")
# game.make_move(1,"X")
# game.make_move(2,"X")
# game.print_board()
# print(f' Winner Winner Chicken Dinner : {game.check_winner()} ')
                        #Non winning moves

game.make_move(0, "X")
game.make_move(1, "O")
game.make_move(2, "O")
game.make_move(3, "X")
game.print_board