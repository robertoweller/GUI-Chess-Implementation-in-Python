'''
This function's main goal is to translate the coordinates of the mouse into what position of the chessboard the mouse is in
This was a repetative implementation, there might (most likely) another way to implement this that is more effecient both in the run time,
and the time it took to code

IF YOU DON'T KNOW THE CHESS POSITIONS: http://www.chess-poster.com/english/learn_chess/notation/images/coordinates_2.gif
'''
import Data_Conversion.tela

# Facilitar o movimento das peças
x = Data_Conversion.tela.tam()

class find_position:

    def chess_position(self, pos):
        if pos[0] <= 102.5/x and pos[1] <= 100/x:
            return "a1"
        elif pos[0] <= 205/x and pos[1] <= 100/x:
            return "b1"
        elif pos[0] <= 307.5/x and pos[1] <= 100/x:
            return "c1"
        elif pos[0] <= 410/x and pos[1] <= 100/x:
            return "d1"
        elif pos[0] <= 512.5/x and pos[1] <= 100/x:
            return "e1"
        elif pos[0] <= 615/x and pos[1] <= 100/x:
            return "f1"
        elif pos[0] <= 717.5/x and pos[1] <= 100/x:
            return "g1"
        elif pos[0] <= 820/x and pos[1] <= 100/x:
            return "h1"
        elif pos[0] <= 102.5/x and pos[1] <= 200/x:
            return "a2"
        elif pos[0] <= 205/x and pos[1] <= 200/x:
            return "b2"
        elif pos[0] <= 307.5/x and pos[1] <= 200/x:
            return "c2"
        elif pos[0] <= 410/x and pos[1] <= 200/x:
            return "d2"
        elif pos[0] <= 512.5/x and pos[1] <= 200/x:
            return "e2"
        elif pos[0] <= 615/x and pos[1] <= 200/x:
            return "f2"
        elif pos[0] <= 717.5/x and pos[1] <= 200/x:
            return "g2"
        elif pos[0] <= 820/x and pos[1] <= 200/x:
            return "h2"
        elif pos[0] <= 102.5/x and pos[1] <= 300/x:
            return "a3"
        elif pos[0] <= 205/x and pos[1] <= 300/x:
            return "b3"
        elif pos[0] <= 307.5/x and pos[1] <= 300/x:
            return "c3"
        elif pos[0] <= 410/x and pos[1] <= 300/x:
            return "d3"
        elif pos[0] <= 512.5/x and pos[1] <= 300/x:
            return "e3"
        elif pos[0] <= 615/x and pos[1] <= 300/x:
            return "f3"
        elif pos[0] <= 717.5/x and pos[1] <= 300/x:
            return "g3"
        elif pos[0] <= 820/x and pos[1] <= 300/x:
            return "h3"
        elif pos[0] <= 102.5/x and pos[1] <= 400/x:
            return "a4"
        elif pos[0] <= 205/x and pos[1] <= 400/x:
            return "b4"
        elif pos[0] <= 307.5/x and pos[1] <= 400/x:
            return "c4"
        elif pos[0] <= 410/x and pos[1] <= 400/x:
            return "d4"
        elif pos[0] <= 512.5/x and pos[1] <= 400/x:
            return "e4"
        elif pos[0] <= 615/x and pos[1] <= 400/x:
            return "f4"
        elif pos[0] <= 717.5/x and pos[1] <= 400/x:
            return "g4"
        elif pos[0] <= 820/x and pos[1] <= 400/x:
            return "h4"
        elif pos[0] <= 102.5/x and pos[1] <= 500/x:
            return "a5"
        elif pos[0] <= 205/x and pos[1] <= 500/x:
            return "b5"
        elif pos[0] <= 307.5/x and pos[1] <= 500/x:
            return "c5"
        elif pos[0] <= 410/x and pos[1] <= 500/x:
            return "d5"
        elif pos[0] <= 512.5/x and pos[1] <= 500/x:
            return "e5"
        elif pos[0] <= 615/x and pos[1] <= 500/x:
            return "f5"
        elif pos[0] <= 717.5/x and pos[1] <= 500/x:
            return "g5"
        elif pos[0] <= 820/x and pos[1] <= 500/x:
            return "h5"
        elif pos[0] <= 102.5/x and pos[1] <= 600/x:
            return "a6"
        elif pos[0] <= 205/x and pos[1] <= 600/x:
            return "b6"
        elif pos[0] <= 307.5/x and pos[1] <= 600/x:
            return "c6"
        elif pos[0] <= 410/x and pos[1] <= 600/x:
            return "d6"
        elif pos[0] <= 512.5/x and pos[1] <= 600/x:
            return "e6"
        elif pos[0] <= 615/x and pos[1] <= 600/x:
            return "f6"
        elif pos[0] <= 717.5/x and pos[1] <= 600/x:
            return "g6"
        elif pos[0] <= 820/x and pos[1] <= 600/x:
            return "h6"
        elif pos[0] <= 102.5/x and pos[1] <= 700/x:
            return "a7"
        elif pos[0] <= 205/x and pos[1] <= 700/x:
            return "b7"
        elif pos[0] <= 307.5/x and pos[1] <= 700/x:
            return "c7"
        elif pos[0] <= 410/x and pos[1] <= 700/x:
            return "d7"
        elif pos[0] <= 512.5/x and pos[1] <= 700/x:
            return "e7"
        elif pos[0] <= 615/x and pos[1] <= 700/x:
            return "f7"
        elif pos[0] <= 717.5/x and pos[1] <= 700/x:
            return "g7"
        elif pos[0] <= 820/x and pos[1] <= 700/x:
            return "h7"
        elif pos[0] <= 102.5/x and pos[1] <= 800/x:
            return "a8"
        elif pos[0] <= 205/x and pos[1] <= 800/x:
            return "b8"
        elif pos[0] <= 307.5/x and pos[1] <= 800/x:
            return "c8"
        elif pos[0] <= 410/x and pos[1] <= 800/x:
            return "d8"
        elif pos[0] <= 512.5/x and pos[1] <= 800/x:
            return "e8"
        elif pos[0] <= 615/x and pos[1] <= 800/x:
            return"f8"
        elif pos[0] <= 717.5/x and pos[1] <= 800/x:
            return "g8"
        elif pos[0] <= 820/x and pos[1] <= 800/x:
            return "h8"
