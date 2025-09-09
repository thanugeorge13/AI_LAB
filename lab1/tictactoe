import random

def display(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-------")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-------")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def player(board):
  while True:
      move = int(input("\nenter move(1 to 9):\t"))
      if board[move - 1] == " ":
        board[move - 1] = "X"
        break
      else:
        print("invalid move")

def computer(board):
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = "O"
            break

def check_win(board, sign):
  win_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
  for i in win_combo:
    if board[i[0]] == board[i[1]] == board[i[2]] == sign:
      return True
  return False

def check_tie(board):
    for i in range(9):
        if board[i] == " ":
            return False
    return True


board = [" "] * 9

while True:
  print("Tic Tac Toe")
  while True:
    display(board)
    player(board)
    display(board)
    if check_win(board, "X"):
      print("player won")
      break
    if check_tie(board):
      print("It's a tie")
      break
    computer(board)
    print("\ncomputer turn")
    if check_win(board, "O"):
      display(board)
      print("computer won")
      break
    if check_tie(board):
      display(board)
      print("It's a tie")
      break
  ans=input("\n\nsay yes for new round\t")
  if ans=="yes":
    board = [" "] * 9
  else:
    break
