import pygame
import random
from datetime import datetime

pygame.init()

width = 700
height = 700

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Chess by Bekhruz S. Niyazov")

icon = pygame.image.load("png/icon.png")
chessboard = pygame.image.load("png/chessboard.jpg")
wpawn = pygame.image.load("png/wpawn.png")
wrook = pygame.image.load("png/wrook.png")
whorse = pygame.image.load("png/whorse.png")
wbishop = pygame.image.load("png/wbishop.png")
wqueen = pygame.image.load("png/wqueen.png")
wking = pygame.image.load("png/wking.png")
bpawn = pygame.image.load("png/bpawn.png")
brook = pygame.image.load("png/brook.png")
bhorse = pygame.image.load("png/bhorse.png")
bbishop = pygame.image.load("png/bbishop.png")
bqueen = pygame.image.load("png/bqueen.png")
bking = pygame.image.load("png/bking.png")

pygame.display.set_icon(icon)

vel = 75
p = ""
moving = False
playerMove = True
twoSpaces = [True for _ in range(8)]
game = ""
moveN = 1

board = []
for _ in range(8):
	board.append(f"a{_}")
for _ in range(8):
	board.append(f"b{_}")
for _ in range(8):
	board.append(f"c{_}")
for _ in range(8):
	board.append(f"d{_}")
for _ in range(8):
	board.append(f"e{_}")
for _ in range(8):
	board.append(f"f{_}")
for _ in range(8):
	board.append(f"g{_}")
for _ in range(8):
	board.append(f"h{_}")

board[0] = "wrook0"
board[1] = "wpawn0"
board[6] = "bpawn0"
board[7] = "brook0"
board[8] = "whorse0"
board[9] = "wpawn1"
board[14] = "bpawn1"
board[15] = "bhorse0"
board[16] = "wbishop0"
board[17] = "wpawn2"
board[22] = "bpawn2"
board[23] = "bbishop0"
board[24] = "wqueen0"
board[25] = "wpawn3"
board[30] = "bpawn3"
board[31] = "bqueen0"
board[32] = "wking0"
board[33] = "wpawn4"
board[38] = "bpawn4"
board[39] = "bking0"
board[40] = "wbishop1"
board[41] = "wpawn5"
board[46] = "bpawn5"
board[47] = "bbishop1"
board[48] = "whorse1"
board[49] = "wpawn6"
board[54] = "bpawn6"
board[55] = "bhorse1"
board[56] = "wrook1"
board[57] = "wpawn7"
board[62] = "bpawn7"
board[63] = "brook1"

date = datetime.now()
file_name = str(date).replace(":", "-")+"-game.txt"

def read(file_name):
	return open(file_name, "r").read()

def compMove():
	global moving, board, figures, playerMove

	if not playerMove:
		for p in board:
			if p == "e4":
				start_move()
				move("p", "b", 4, "e4", 2)
				end_move()
				return
		# if "e4" not in board:
		# 	if "f3" not in board:
		# 		start_move()
		# 		move("p", "b", 4, "f3")
		# 		end_move()
		# 		return

def start_move():
	global moving
	moving = True

def move(figure, color, index, pos, steps=1):
	global moving, board, playerMove, game, moveN, file_name, date

	f = open(file_name, "w")

	if moving:
		if color == "w" and playerMove:
			color = "whites"
		if color == "b":
			color = "blacks"

		if figure == "p":
			figure = "pawns"
			if color == "whites":
				if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]):
					figures[color][figure][index]["y"] -= vel*steps
					figures[color][figure][index]["x"] += vel*steps
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					game += f"{moveN}. {position0}-{position1}\t"
					f.write(game)
					moveN += 1
					board[board.index(f"wpawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"wpawn{index}"
					board[board.index(f"{color[0]}pawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}pawn{index}"
				if ord(pos[0]) == ord(figures[color][figure][index]["p"][0]):
					figures[color][figure][index]["y"] -= vel*steps
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					game += f"{moveN}. {position0}-{position1}\t"
					f.write(game)
					moveN += 1
					board[board.index(f"wpawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"wpawn{index}"
				if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]):
					figures[color][figure][index]["y"] -= vel*steps
					figures[color][figure][index]["x"] -= vel*steps
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					game += f"{moveN}. {position0}-{position1}\t"
					f.write(game)
					moveN += 1
					board[board.index(f"wpawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"wpawn{index}"
					board[board.index(f"{color[0]}pawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}pawn{index}"
			if color == "blacks":
				if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]):
					figures[color][figure][index]["y"] += vel*steps
					figures[color][figure][index]["x"] += vel*steps
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"wpawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"wpawn{index}"
					board[board.index(f"{color[0]}pawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}pawn{index}"
				if ord(pos[0]) == ord(figures[color][figure][index]["p"][0]):
					figures[color][figure][index]["y"] += vel*steps
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"wpawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"wpawn{index}"
				if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]):
					figures[color][figure][index]["y"] += vel*steps
					figures[color][figure][index]["x"] -= vel*steps
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"wpawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"wpawn{index}"
					board[board.index(f"{color[0]}pawn{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}pawn{index}"

		if figure == "r":
			figure = "rooks"
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]):
				figures[color][figure][index]["x"] -= vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}rook{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}rook{index}"
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]):
				figures[color][figure][index]["x"] += vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}rook{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}rook{index}"
			if int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}rook{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}rook{index}"
			if int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel*steps
				board[board.index(f"{color[0]}rook{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}rook{index}"

		if figure == "h":
			figure = "horses"
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]) and int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				if ord(figures[color][figure][index]["p"][0]) - ord(pos[0]) == 1:
					figures[color][figure][index]["x"] -= vel
					figures[color][figure][index]["y"] -= vel*2
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					if color == "whites":
						game += f"{moveN}. {position0}-{position1}\t"
						moveN += 1
					if color == "blacks":
						game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"{color[0]}horse{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}horse{index}"
				else:
					figures[color][figure][index]["x"] -= vel*2
					figures[color][figure][index]["y"] -= vel
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					if color == "whites":
						game += f"{moveN}. {position0}-{position1}\t"
						moveN += 1
					if color == "blacks":
						game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"{color[0]}horse{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}horse{index}"

			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]) and int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				if ord(figures[color][figure][index]["p"][0]) - ord(pos[0]) == 2:
					figures[color][figure][index]["x"] -= vel*2
					figures[color][figure][index]["y"] += vel
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					if color == "whites":
						game += f"{moveN}. {position0}-{position1}\t"
						moveN += 1
					if color == "blacks":
						game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"{color[0]}horse{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}horse{index}"
				else:
					figures[color][figure][index]["x"] -= vel
					figures[color][figure][index]["y"] += vel*2
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					if color == "whites":
						game += f"{moveN}. {position0}-{position1}\t"
						moveN += 1
					if color == "blacks":
						game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"{color[0]}horse{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}horse{index}"
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]) and int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				if ord(pos[0]) - ord(figures[color][figure][index]["p"][0]) == 1:
					figures[color][figure][index]["x"] += vel
					figures[color][figure][index]["y"] -= vel*2
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					if color == "whites":
						game += f"{moveN}. {position0}-{position1}\t"
						moveN += 1
					if color == "blacks":
						game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"{color[0]}horse{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}horse{index}"
				else:
					figures[color][figure][index]["x"] += vel*2
					figures[color][figure][index]["y"] -= vel
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					if color == "whites":
						game += f"{moveN}. {position0}-{position1}\t"
						moveN += 1
					if color == "blacks":
						game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"{color[0]}horse{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}horse{index}"
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]) and int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				if ord(pos[0]) - ord(figures[color][figure][index]["p"][0]) == 1:
					figures[color][figure][index]["x"] += vel
					figures[color][figure][index]["y"] += vel*2
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					if color == "whites":
						game += f"{moveN}. {position0}-{position1}\t"
						moveN += 1
					if color == "blacks":
						game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"{color[0]}horse{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}horse{index}"
				else:
					figures[color][figure][index]["x"] += vel*2
					figures[color][figure][index]["y"] += vel
					position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
					position1 = pos[0]+str(int(pos[1])+1)
					if color == "whites":
						game += f"{moveN}. {position0}-{position1}\t"
						moveN += 1
					if color == "blacks":
						game += f"{position0}-{position1}\n"
					f.write(game)
					board[board.index(f"{color[0]}horse{index}")] = figures[color][figure][index]["p"]
					board[board.index(pos)] = f"{color[0]}horse{index}"


		if figure == "b":
			figure = "bishops"
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]) and int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel*steps
				figures[color][figure][index]["x"] -= vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}bishop{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}bishop{index}"
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]) and int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel*steps
				figures[color][figure][index]["x"] += vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}bishop{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}bishop{index}"
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]) and int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel*steps
				figures[color][figure][index]["x"] -= vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}bishop{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}bishop{index}"
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]) and int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel*steps
				figures[color][figure][index]["x"] += vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}bishop{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}bishop{index}"

		if figure == "q":
			figure = "queen"
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]) and int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel*steps
				figures[color][figure][index]["x"] -= vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}queen{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}queen{index}"
				return
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]) and int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel*steps
				figures[color][figure][index]["x"] += vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}queen{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}queen{index}"
				return
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]) and int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel*steps
				figures[color][figure][index]["x"] -= vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}queen{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}queen{index}"
				return
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]) and int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel*steps
				figures[color][figure][index]["x"] += vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}queen{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}queen{index}"
				return
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]):
				figures[color][figure][index]["x"] -= vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}queen{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}queen{index}"
				return
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]):
				figures[color][figure][index]["x"] += vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}queen{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}queen{index}"
				return
			if int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}queen{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}queen{index}"
				return
			if int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel*steps
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}queen{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}queen{index}"
				return

		if figure == "k":
			figure = "king"
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]) and int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel
				figures[color][figure][index]["x"] -= vel
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}king{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}king{index}"
				return
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]) and int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel
				figures[color][figure][index]["x"] += vel
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}king{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}king{index}"
				return
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]) and int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel
				figures[color][figure][index]["x"] -= vel
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}king{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}king{index}"
				return
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]) and int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel
				figures[color][figure][index]["x"] += vel
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}king{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}king{index}"
				num = str(int(figures[color][figure][index]["p"][1])-1)
				letter = chr(ord(figures[color][figure][index]["p"][0])+1)
				figures[color][figure][index]["p"] = letter+num
				return
			if ord(pos[0]) < ord(figures[color][figure][index]["p"][0]):
				figures[color][figure][index]["x"] -= vel
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}king{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}king{index}"
				return
			if ord(pos[0]) > ord(figures[color][figure][index]["p"][0]):
				figures[color][figure][index]["x"] += vel
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}king{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}king{index}"
				return
			if int(pos[1]) > int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] -= vel
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}king{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}king{index}"
				return
			if int(pos[1]) < int(figures[color][figure][index]["p"][1]):
				figures[color][figure][index]["y"] += vel
				position0 = figures[color][figure][index]["p"][0]+str(int(figures[color][figure][index]["p"][1])+1)
				position1 = pos[0]+str(int(pos[1])+1)
				if color == "whites":
					game += f"{moveN}. {position0}-{position1}\t"
					moveN += 1
				if color == "blacks":
					game += f"{position0}-{position1}\n"
				f.write(game)
				board[board.index(f"{color[0]}king{index}")] = figures[color][figure][index]["p"]
				board[board.index(pos)] = f"{color[0]}king{index}"
				return

def end_move():
	global moving
	moving = False
	playerMove = False

def get_cor(color, figure, index):
	if color == "w":
		try: return (figures["whites"][figure][index]["x"], figures["whites"][figure][index]["y"])
		except: print("Can't find the x and y values.")
	elif color == "b":
		try: return (figures["blacks"][figure][index]["x"], figures["blacks"][figure][index]["y"])
		except: print("Can't find the x and y values.")
	else: print("Invalid color.")

def get_pos(pos):
	p = ""
	if pos[0] > 20 and pos[0] < 100:
		if pos[1] > 580 and pos[1] < 660: p = "a0"
		if pos[1] > 500 and pos[1] < 580: p = "a1"
		if pos[1] > 420 and pos[1] < 500: p = "a2"
		if pos[1] > 340 and pos[1] < 420: p = "a3"
		if pos[1] > 260 and pos[1] < 340: p = "a4"
		if pos[1] > 180 and pos[1] < 260: p = "a5"
		if pos[1] > 100 and pos[1] < 180: p = "a6"
		if pos[1] > 20 and pos[1] < 100: p = "a7"

	if pos[0] > 100 and pos[0] < 180:
		if pos[1] > 580 and pos[1] < 660: p = "b0"
		if pos[1] > 500 and pos[1] < 580: p = "b1"
		if pos[1] > 420 and pos[1] < 500: p = "b2"
		if pos[1] > 340 and pos[1] < 420: p = "b3"
		if pos[1] > 260 and pos[1] < 340: p = "b4"
		if pos[1] > 180 and pos[1] < 260: p = "b5"
		if pos[1] > 100 and pos[1] < 180: p = "b6"
		if pos[1] > 20 and pos[1] < 100: p = "b7"

	if pos[0] > 180 and pos[0] < 260:
		if pos[1] > 580 and pos[1] < 660: p = "c0"
		if pos[1] > 500 and pos[1] < 580: p = "c1"
		if pos[1] > 420 and pos[1] < 500: p = "c2"
		if pos[1] > 340 and pos[1] < 420: p = "c3"
		if pos[1] > 260 and pos[1] < 340: p = "c4"
		if pos[1] > 180 and pos[1] < 260: p = "c5"
		if pos[1] > 100 and pos[1] < 180: p = "c6"
		if pos[1] > 20 and pos[1] < 100: p = "c7"

	if pos[0] > 260 and pos[0] < 340:
		if pos[1] > 580 and pos[1] < 660: p = "d0"
		if pos[1] > 500 and pos[1] < 580: p = "d1"
		if pos[1] > 420 and pos[1] < 500: p = "d2"
		if pos[1] > 340 and pos[1] < 420: p = "d3"
		if pos[1] > 260 and pos[1] < 340: p = "d4"
		if pos[1] > 180 and pos[1] < 260: p = "d5"
		if pos[1] > 100 and pos[1] < 180: p = "d6"
		if pos[1] > 20 and pos[1] < 100: p = "d7"

	if pos[0] > 340 and pos[0] < 420:
		if pos[1] > 580 and pos[1] < 660: p = "e0"
		if pos[1] > 500 and pos[1] < 580: p = "e1"
		if pos[1] > 420 and pos[1] < 500: p = "e2"
		if pos[1] > 340 and pos[1] < 420: p = "e3"
		if pos[1] > 260 and pos[1] < 340: p = "e4"
		if pos[1] > 180 and pos[1] < 260: p = "e5"
		if pos[1] > 100 and pos[1] < 180: p = "e6"
		if pos[1] > 20 and pos[1] < 100: p = "e7"

	if pos[0] > 420 and pos[0] < 500:
		if pos[1] > 580 and pos[1] < 660: p = "f0"
		if pos[1] > 500 and pos[1] < 580: p = "f1"
		if pos[1] > 420 and pos[1] < 500: p = "f2"
		if pos[1] > 340 and pos[1] < 420: p = "f3"
		if pos[1] > 260 and pos[1] < 340: p = "f4"
		if pos[1] > 180 and pos[1] < 260: p = "f5"
		if pos[1] > 100 and pos[1] < 180: p = "f6"
		if pos[1] > 20 and pos[1] < 100: p = "f7"

	if pos[0] > 500 and pos[0] < 580:
		if pos[1] > 580 and pos[1] < 660: p = "g0"
		if pos[1] > 500 and pos[1] < 580: p = "g1"
		if pos[1] > 420 and pos[1] < 500: p = "g2"
		if pos[1] > 340 and pos[1] < 420: p = "g3"
		if pos[1] > 260 and pos[1] < 340: p = "g4"
		if pos[1] > 180 and pos[1] < 260: p = "g5"
		if pos[1] > 100 and pos[1] < 180: p = "g6"
		if pos[1] > 20 and pos[1] < 100: p = "g7"

	if pos[0] > 580 and pos[0] < 660:
		if pos[1] > 580 and pos[1] < 660: p = "h0"
		if pos[1] > 500 and pos[1] < 580: p = "h1"
		if pos[1] > 420 and pos[1] < 500: p = "h2"
		if pos[1] > 340 and pos[1] < 420: p = "h3"
		if pos[1] > 260 and pos[1] < 340: p = "h4"
		if pos[1] > 180 and pos[1] < 260: p = "h5"
		if pos[1] > 100 and pos[1] < 180: p = "h6"
		if pos[1] > 20 and pos[1] < 100: p = "h7"

	return p

def available_moves(color, figure, pos, index):
	global board, win, vel, figures
	available_moves = []

	x = figures[color][figure][index]["x"] + 33
	y = figures[color][figure][index]["y"] - 35

	if figure == "pawns":
		if color == "whites":
			for p in board:
				if pos[0]+str(int(pos[1])+1) == p:
					available_moves.append(p)
				if pos[0]+str(int(pos[1])+2) == p and twoSpaces[index]:
					available_moves.append(p)
			if str(ord(pos[0])+1)+str(int(pos[1])+1) not in board:
					available_moves.append(str(ord(pos[0])+1)+str(int(pos[1])+1))
			if str(ord(pos[0])-1)+str(int(pos[1])+1) not in board:
				available_moves.append(str(ord(pos[0])-1)+str(int(pos[1])+1))
		else:
			for p in board:
				if pos[0]+str(int(pos[1])-1) == p:
					available_moves.append(p)
				if pos[0]+str(int(pos[1])-2) == p and twoSpaces[index]:
					available_moves.append(p)
			if str(ord(pos[0])+1)+str(int(pos[1]-1)) not in board:
				available_moves.append(str(ord(pos[0])+1)+str(int(pos[1])-1))
			if str(str(ord(pos[0])-1))+str(int(pos[1])-1) not in board:
				available_moves.append(str(pos[0])-1)+str(int(pos[1])-1)

	if figure == "rooks":
		for p in board:
			for i in range(8):
				if pos[0]+str(int(pos[1])+i) == p: available_moves.append(p)
				if pos[0]+str(int(pos[1])-i) == p: available_moves.append(p)
				if chr(ord(pos[0])+i)+pos[1] == p: available_moves.append(p)
				if chr(ord(pos[0])-i)+pos[1] == p: available_moves.append(p)

	if figure == "horses":
		for p in board:
			if chr(ord(pos[0])+1)+str(int(pos[1])+2) == p:
				available_moves.append(p)
			if chr(ord(pos[0])-1)+str(int(pos[1])+2) == p:
				available_moves.append(p)
			if chr(ord(pos[0])+1)+str(int(pos[1])-2) == p:
				available_moves.append(p)
			if chr(ord(pos[0])-1)+str(int(pos[1])-2) == p:
				available_moves.append(p)
			if chr(ord(pos[0])+2)+str(int(pos[1])+1) == p:
				available_moves.append(p)
			if chr(ord(pos[0])-2)+str(int(pos[1])+1) == p:
				available_moves.append(p)
			if chr(ord(pos[0])+2)+str(int(pos[1])-1) == p:
				available_moves.append(p)
			if chr(ord(pos[0])-2)+str(int(pos[1])-1) == p:
				available_moves.append(p)

	if figure == "bishops":
		for p in board:
			for i in range(8):
				if chr(ord(pos[0])-i)+str(int(pos[1])+i) == p: available_moves.append(p)
				if chr(ord(pos[0])+i)+str(int(pos[1])+i) == p: available_moves.append(p)
				if chr(ord(pos[0])-i)+str(int(pos[1])-i) == p: available_moves.append(p)
				if chr(ord(pos[0])+i)+str(int(pos[1])-i) == p: available_moves.append(p)

	if figure == "queen":
		for p in board:
			for i in range(8):
				if pos[0]+str(int(pos[1])+i) == p: available_moves.append(p)
				if pos[0]+str(int(pos[1])-i) == p: available_moves.append(p)
				if chr(ord(pos[0])+i)+pos[1] == p: available_moves.append(p)
				if chr(ord(pos[0])-i)+pos[1] == p: available_moves.append(p)
				if chr(ord(pos[0])-i)+str(int(pos[1])+i) == p: available_moves.append(p)
				if chr(ord(pos[0])+i)+str(int(pos[1])+i) == p: available_moves.append(p)
				if chr(ord(pos[0])-i)+str(int(pos[1])-i) == p: available_moves.append(p)
				if chr(ord(pos[0])+i)+str(int(pos[1])-i) == p: available_moves.append(p)

	if figure == "king":
		for p in board:
			if pos[0]+str(int(pos[1])+1) == p: available_moves.append(p)
			if pos[0]+str(int(pos[1])-1) == p: available_moves.append(p)
			if chr(ord(pos[0])+1)+pos[1] == p: available_moves.append(p)
			if chr(ord(pos[0])-1)+pos[1] == p: available_moves.append(p)
			if chr(ord(pos[0])-1)+str(int(pos[1])+1) == p: available_moves.append(p)
			if chr(ord(pos[0])+1)+str(int(pos[1])+1) == p: available_moves.append(p)
			if chr(ord(pos[0])-1)+str(int(pos[1])-1) == p: available_moves.append(p)
			if chr(ord(pos[0])+1)+str(int(pos[1])-1) == p: available_moves.append(p)

	pygame.display.update()
	available_moves.append("")
	return available_moves

def redrawWindow(surface):
	surface.blit(chessboard, (0, 0))

	for _ in range(8):
		surface.blit(wpawn, get_cor("w", "pawns", _))
		surface.blit(bpawn, get_cor("b", "pawns", _))
	for _ in range(2):
		surface.blit(wrook, get_cor("w", "rooks", _))
		surface.blit(brook, get_cor("b", "rooks", _))
		surface.blit(whorse, get_cor("w", "horses", _))
		surface.blit(bhorse, get_cor("b", "horses", _))
		surface.blit(wbishop, get_cor("w", "bishops", _))
		surface.blit(bbishop, get_cor("b", "bishops", _))

	surface.blit(wking, get_cor("w", "king", 0))
	surface.blit(bking, get_cor("b", "king", 0))
	surface.blit(wqueen, get_cor("w", "queen", 0))
	surface.blit(bqueen, get_cor("b", "queen", 0))

	pygame.display.update()

figures = {
	"whites": {"pawns": {0: {"x": 60, "y": 500, "p": "a1"}, 1: {"x": 135, "y": 500, "p": "b1"}, 2: {"x": 210, "y": 500, "p": "c1"}, 3: {"x": 285, "y": 500, "p": "d1"}, \
				4: {"x": 360, "y": 500, "p": "e1"}, 5: {"x": 435, "y": 500, "p": "f1"}, 6: {"x": 510, "y": 500, "p": "g1"}, 7: {"x": 585, "y": 500, "p": "h1"}},
				"rooks": {0: {"x": 60, "y": 580, "p": "a0"}, 1: {"x": 585, "y": 580, "p": "h0"}},
				"horses": {0: {"x": 135, "y": 580, "p": "b0"}, 1: {"x": 510, "y": 580, "p": "g0"}},
				"bishops": {0: {"x": 210, "y": 580, "p": "c0"}, 1: {"x": 435, "y": 580, "p": "f0"}},
				"queen": {0: {"x": 285, "y": 580, "p": "d0"}},
				"king": {0: {"x": 360, "y": 580, "p": "e0"}}},
	"blacks": {"pawns": {0: {"x": 60, "y": 125, "p": "a6"}, 1: {"x": 135, "y": 125, "p": "b6"}, 2: {"x": 210, "y": 125, "p": "c6"}, 3: {"x": 285, "y": 125, "p": "d6"}, \
				4: {"x": 360, "y": 125, "p": "e6"}, 5: {"x": 435, "y": 125, "p": "f6"}, 6: {"x": 510, "y": 125, "p": "g6"}, 7: {"x": 585, "y": 125, "p": "h6"}},
				"rooks": {0: {"x": 60, "y": 50, "p": "a7"}, 1: {"x": 585, "y": 50, "p": "h7"}},
				"horses": {0: {"x": 135, "y": 50, "p": "b7"}, 1: {"x": 510, "y": 50, "p": "g7"}},
				"bishops": {0: {"x": 210, "y": 50, "p": "c7"}, 1: {"x": 435, "y": 50, "p": "f7"}},
				"queen": {0: {"x": 285, "y": 50, "p": "d7"}},
				"king": {0: {"x": 360, "y": 50, "p": "e7"}}}
}

while True:
	if pygame.event.get(pygame.QUIT):
		break

	keys = pygame.key.get_pressed()

	if keys[pygame.K_ESCAPE]:
		break

	if playerMove:
		p = ""
		if pygame.mouse.get_pressed()[2]:
			pos = pygame.mouse.get_pos()
			p = get_pos(pos)

		for _ in range(8):
			if p == figures["whites"]["pawns"][_]["p"]:
				pygame.event.get()
				while not pygame.mouse.get_pressed()[0]:
					available_moves("whites", "pawns", p, _)
					pygame.event.get()
					if pygame.mouse.get_pressed()[0]:
						position = pygame.mouse.get_pos()
						position = get_pos(position)
						if position in available_moves("whites", "pawns", figures["whites"]["pawns"][_]["p"], _):
							start_move()
							if position == available_moves("whites", "pawns", figures["whites"]["pawns"][_]["p"], _)[1] and twoSpaces[_]:
								move("p", "w", _, position, steps=2)
							else:
								move("p", "w", _, position)
							figures["whites"]["pawns"][_]["p"] = position
							twoSpaces[_] = False
							end_move()
							playerMove = False
							break

		for _ in range(2):
			if p == figures["whites"]["rooks"][_]["p"]:
				pygame.event.get()
				while not pygame.mouse.get_pressed()[0]:
					available_moves("whites", "rooks", p, _)
					pygame.event.get()
					if pygame.mouse.get_pressed()[0]:
						position = pygame.mouse.get_pos()
						position = get_pos(position)
						if position in available_moves("whites", "rooks", figures["whites"]["rooks"][_]["p"], _):
							steps = 0
							if position[0] == figures["whites"]["rooks"][_]["p"][0]:
								if int(position[1]) > int(figures["whites"]["rooks"][_]["p"][1]):
									steps = int(position[1]) - int(figures["whites"]["rooks"][_]["p"][1])
								else:
									steps = int(figures["whites"]["rooks"][_]["p"][1]) - int(position[1])
							else:
								if ord(position[0]) > ord(figures["whites"]["rooks"][_]["p"][0]):
									steps = ord(position[0]) - ord(figures["whites"]["rooks"][_]["p"][0])
								else:
									steps = ord(figures["whites"]["rooks"][_]["p"][0]) - ord(position[0])
							start_move()
							move("r", "w", _, position, steps=steps)
							figures["whites"]["rooks"][_]["p"] = position
							end_move()
							playerMove = False
							break

		for _ in range(2):
			if p == figures["whites"]["horses"][_]["p"]:
				pygame.event.get()
				while not pygame.mouse.get_pressed()[0]:
					available_moves("whites", "horses", p, _)
					pygame.event.get()
					if pygame.mouse.get_pressed()[0]:
						position = pygame.mouse.get_pos()
						position = get_pos(position)
						if position in available_moves("whites", "horses", figures["whites"]["horses"][_]["p"], _):
							steps = 0
							if position[0] == figures["whites"]["horses"][_]["p"][0]:
								if int(position[1]) > int(figures["whites"]["horses"][_]["p"][1]):
									steps = int(position[1]) - int(figures["whites"]["horses"][_]["p"][1])
								else:
									steps = int(figures["whites"]["horses"][_]["p"][1]) - int(position[1])
							else:
								if ord(position[0]) > ord(figures["whites"]["horses"][_]["p"][0]):
									steps = ord(position[0]) - ord(figures["whites"]["horses"][_]["p"][0])
								else:
									steps = ord(figures["whites"]["horses"][_]["p"][0]) - ord(position[0])
							start_move()
							move("h", "w", _, position)
							figures["whites"]["horses"][_]["p"] = position
							end_move()
							playerMove = False
							break

		for _ in range(2):
			if p == figures["whites"]["bishops"][_]["p"]:
				pygame.event.get()
				while not pygame.mouse.get_pressed()[0]:
					available_moves("whites", "bishops", p, _)
					pygame.event.get()
					if pygame.mouse.get_pressed()[0]:
						position = pygame.mouse.get_pos()
						position = get_pos(position)
						if position in available_moves("whites", "bishops", figures["whites"]["bishops"][_]["p"], _):
							steps = 0
							if position[0] == figures["whites"]["bishops"][_]["p"][0]:
								if int(position[1]) > int(figures["whites"]["bishops"][_]["p"][1]):
									steps = int(position[1]) - int(figures["whites"]["bishops"][_]["p"][1])
								else:
									steps = int(figures["whites"]["bishops"][_]["p"][1]) - int(position[1])
							else:
								if ord(position[0]) > ord(figures["whites"]["bishops"][_]["p"][0]):
									steps = ord(position[0]) - ord(figures["whites"]["bishops"][_]["p"][0])
								else:
									steps = ord(figures["whites"]["bishops"][_]["p"][0]) - ord(position[0])
							start_move()
							move("b", "w", _, position, steps=steps)
							figures["whites"]["bishops"][_]["p"] = position
							end_move()
							playerMove = False
							break

		if p == figures["whites"]["queen"][0]["p"]:
			pygame.event.get()
			while not pygame.mouse.get_pressed()[0]:
				available_moves("whites", "queen", p, 0)
				pygame.event.get()
				if pygame.mouse.get_pressed()[0]:
					position = pygame.mouse.get_pos()
					position = get_pos(position)
					if position in available_moves("whites", "queen", figures["whites"]["queen"][0]["p"], 0):
						steps = 0
						if position[0] == figures["whites"]["queen"][0]["p"][0]:
							if int(position[1]) > int(figures["whites"]["queen"][0]["p"][1]):
								steps = int(position[1]) - int(figures["whites"]["queen"][0]["p"][1])
							else:
								steps = int(figures["whites"]["queen"][0]["p"][1]) - int(position[1])
						else:
							if ord(position[0]) > ord(figures["whites"]["queen"][0]["p"][0]):
								steps = ord(position[0]) - ord(figures["whites"]["queen"][0]["p"][0])
							else:
								steps = ord(figures["whites"]["queen"][0]["p"][0]) - ord(position[0])
						start_move()
						move("q", "w", 0, position, steps=steps)
						figures["whites"]["queen"][0]["p"] = position
						end_move()
						playerMove = False
						break

		if p == figures["whites"]["king"][0]["p"]:
			pygame.event.get()
			while not pygame.mouse.get_pressed()[0]:
				available_moves("whites", "king", p, 0)
				pygame.event.get()
				if pygame.mouse.get_pressed()[0]:
					position = pygame.mouse.get_pos()
					position = get_pos(position)
					if position in available_moves("whites", "king", figures["whites"]["king"][0]["p"], 0):
						start_move()
						move("k", "w", 0, position)
						figures["whites"]["king"][0]["p"] = position
						end_move()
						playerMove = False
						break

	else:
		compMove()
		playerMove = True

	redrawWindow(win)

exit()
