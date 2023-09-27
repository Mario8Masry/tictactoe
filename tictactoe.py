board = ["__", "__", "__", "__", "__", "__", "__", "__", "__"]
board_raw = ["__", "__", "__", "__", "__", "__", "__", "__", "__"]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9]



player_mark = "X"
position = 0
game_running = True

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
    global player_mark
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
        try:          
            if board[position - 1] == "__":
                    board[position - 1] = player_mark
                  
            else:
                switch_player()
                print("Position already taken, Try another one <3")
        except:
            pass
      

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
                  return

       #checking column
    for i in range(3):
          if board[i] == board[i + 3] == board[i + 6] and board[i] != "__":
              print(f"Player {board[i]} Won !!")
     # return True
              game_running = False
              return
  #checking diagonals
    if board[0] == board[4] == board[8] and board[0] != "__":
              print(f"Player {board[0]} Won !!")
              game_running = False
              return
      #  return True
    if board[2] == board[4] == board[6] and board[2] != "__":
              print(f"Player {board[2]} Won !!")
       # return True
              game_running = False
              return
#____________________________________________________________
def check_tie(board):
    global game_running
    if "__" not in board:
            show_board(board)
            print("It is a tie!")
            game_running = False
    

#def check_place(board):
    
#____________________________________________________________
# def restart(board):
#     global game_running
#    # global board
#     global board_raw
#     if play_again():
#         if check_win(board) or check_tie(board):
#             board = board_raw.copy()
#             game_running = True
def restart(board):
     global game_running
     global board_raw
     if play_again():
         board[:] = board_raw.copy()
         game_running = True   
        
#____________________________________________________________
def play_again():
    dec = input("Do you want to play again ? Yes or No ").lower()
    if dec in ["yes", "y"]:
        return True
    elif dec in ["no", "n"]:
        return False
         
    else:
        print("Not valid option")
        return play_again()




while game_running:
        show_board(board)
        place_input(board)
        check_win(board)
        check_tie(board)
        if game_running:
            switch_player()
        else:
            if play_again():
                restart(board)
            else:
                break
     #   switch_player()
   #     show_board(board)
   #     play_again()
   #     restart(board)
     #   check_win(board)
     #   check_tie(board)
        


