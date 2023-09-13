board = ["__", "__", "__", "__", "__", "__", "__", "__", "__"]
#board_raw = ["__", "__", "__", "__", "__", "__", "__", "__", "__"]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#new_game = ['y', 'n', 'yes', 'no']


player_mark = "X"
position = 0
game_running = True
#reset_board()
#start_game()
def show_board(board):
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("___________")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("___________")
  print(board[6] + " | " + board[7] + " | " + board[8])

#choose sympol
#def player_input():
#  global player_mark
  # try:
  #     player_mark = (input("Enter Your sympol : ")).upper()
  #     if player_mark != "X" and player_mark != "O":
  #       player_mark = "__"
  #       raise ValueError
  #     else:
  #       place_input()
  # except ValueError:
  #   print("Unvalid sympol")
  

#inplace sympols
def place_input(board):
  global position
  try:
      position = int(input("Choose your position between 1 --> 9 : "))
      if position not in index:
          position = None
          raise ValueError
      else:
          position = position
  except ValueError:
      print("Not valid index on board")
  if position is not None:
      board[position - 1] = player_mark
#____________________________________________________________
def switch_player():
    global player_mark
    if player_mark == "X":
        player_mark = "O"
    else:
        player_mark = "X"
#____________________________________________________________

def check_win(board):
    global game_running       
  #checking rows
    for i in range(3):
              if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != "__":
                  print(f"Player {board[i*3]} Won !!")
     # return True
                  game_running = False

       #checking column
    for i in range(3):
          if board[i] == board[i + 3] == board[i + 6] and board[i] != "__":
              print(f"Player {board[i]} Won !!")
     # return True
              game_running = False
  #checking diagonals
          if board[0] == board[4] == board[8] and board[0] != "__":
              print(f"Player {board[0]} Won !!")
      #  return True
          if board[2] == board[4] == board[6] and board[2] != "__":
              print(f"Player {board[2]} Won !!")
       # return True
              game_running = False
#____________________________________________________________
def check_tie(board):
    global game_running
    if "__" not in board:
            show_board(board)
            print("It is a tie!")
            game_running = False
    

#def check_place(board):
    
#____________________________________________________________





while game_running:
        show_board(board)
        place_input(board)
   #     check_place(board)
        check_win(board)
        check_tie(board)
        switch_player()
     #   check_win(board)
     #   check_tie(board)
    

