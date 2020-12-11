import pygame
from pygame.locals import *

pygame.init()


class Piece(object):
    def __init__(self, color, name, position, img, isSelected=False, isChecking=False, pinningPiece=None,
                 possibleMoves=[], isDefending=[]):
        self.color = color
        self.name = name
        self.position = position
        self.img = img
        self.isSelected = isSelected
        self.isChecking = isChecking
        self.pinningPiece = pinningPiece
        self.possibleMoves = possibleMoves
        self.isDefending = isDefending


class Pawn(Piece):
    def __init__(self, color, name, position, img, isSelected=False, isChecking=False, pinningPiece=None,
                 possibleMoves=[], isDefending=[], doubleMoveLastTurn=False):
        super().__init__(color, name, position, img, isSelected, isChecking, pinningPiece, possibleMoves, isDefending)
        self.doubleMoveLastTurn = doubleMoveLastTurn


class Rook(Piece):
    def __init__(self, color, name, position, img, isSelected=False, isChecking=False, pinningPiece=None,
                 possibleMoves=[], isDefending=[], hasMoved=False):
        super().__init__(color, name, position, img, isSelected, isChecking, pinningPiece, possibleMoves, isDefending)
        self.hasMoved = hasMoved


class King(Piece):
    def __init__(self, color, name, position, img, isSelected=False, isChecking=False, pinningPiece=None,
                 possibleMoves=[], isDefending=[], hasMoved=False):
        super().__init__(color, name, position, img, isSelected, isChecking, pinningPiece, possibleMoves, isDefending)
        self.hasMoved = hasMoved


def main():
    width = 672
    height = 672
    turn = "white"
    boardFlip = False
    turnCount = 1
    whiteInCheck = False
    blackInCheck = False
    win = pygame.display.set_mode((width, height))
    chessBoard = pygame.image.load('Chess Board.png')
    blackPawnImg = pygame.image.load('Black Pawn.png')
    blackRookImg = pygame.image.load('Black Rook.png')
    blackKnightImg = pygame.image.load('Black Knight.png')
    blackBishopImg = pygame.image.load('Black Bishop.png')
    blackKingImg = pygame.image.load('Black King.png')
    blackQueenImg = pygame.image.load('Black Queen.png')

    whitePawnImg = pygame.image.load('White Pawn.png')
    whiteRookImg = pygame.image.load('White Rook.png')
    whiteKnightImg = pygame.image.load('White Knight.png')
    whiteBishopImg = pygame.image.load('White Bishop.png')
    whiteKingImg = pygame.image.load('White King.png')
    whiteQueenImg = pygame.image.load('White Queen.png')

    blackPawn1 = Pawn('black', 'pawn', [0, 84], blackPawnImg)
    blackPawn2 = Pawn('black', 'pawn', [84, 84], blackPawnImg)
    blackPawn3 = Pawn('black', 'pawn', [168, 84], blackPawnImg)
    blackPawn4 = Pawn('black', 'pawn', [252, 84], blackPawnImg)
    blackPawn5 = Pawn('black', 'pawn', [336, 84], blackPawnImg)
    blackPawn6 = Pawn('black', 'pawn', [420, 84], blackPawnImg)
    blackPawn7 = Pawn('black', 'pawn', [504, 84], blackPawnImg)
    blackPawn8 = Pawn('black', 'pawn', [588, 84], blackPawnImg)

    blackRook1 = Rook('black', 'rook', [0, 0], blackRookImg)
    blackRook2 = Rook('black', 'rook', [588, 0], blackRookImg)

    blackKnight1 = Piece('black', 'knight', [84, 0], blackKnightImg)
    blackKnight2 = Piece('black', 'knight', [504, 0], blackKnightImg)

    blackBishop1 = Piece('black', 'bishop', [168, 0], blackBishopImg)
    blackBishop2 = Piece('black', 'bishop', [420, 0], blackBishopImg)

    blackQueen = Piece('black', 'queen', [252, 0], blackQueenImg)
    blackKing = King('black', 'king', [336, 0], blackKingImg)

    blackList = [blackPawn1, blackPawn2, blackPawn3, blackPawn4, blackPawn5,
                 blackPawn6, blackPawn7, blackPawn8, blackRook1, blackRook2,
                 blackKnight1, blackKnight2, blackBishop1, blackBishop2, blackQueen,
                 blackKing]

    whitePawn1 = Pawn('white', 'pawn', [0, 504], whitePawnImg)
    whitePawn2 = Pawn('white', 'pawn', [84, 504], whitePawnImg)
    whitePawn3 = Pawn('white', 'pawn', [168, 504], whitePawnImg)
    whitePawn4 = Pawn('white', 'pawn', [252, 504], whitePawnImg)
    whitePawn5 = Pawn('white', 'pawn', [336, 504], whitePawnImg)
    whitePawn6 = Pawn('white', 'pawn', [420, 504], whitePawnImg)
    whitePawn7 = Pawn('white', 'pawn', [504, 504], whitePawnImg)
    whitePawn8 = Pawn('white', 'pawn', [588, 504], whitePawnImg)

    whiteRook1 = Rook('white', 'rook', [0, 588], whiteRookImg)
    whiteRook2 = Rook('white', 'rook', [588, 588], whiteRookImg)

    whiteKnight1 = Piece('white', 'knight', [84, 588], whiteKnightImg)
    whiteKnight2 = Piece('white', 'knight', [504, 588], whiteKnightImg)

    whiteBishop1 = Piece('white', 'bishop', [168, 588], whiteBishopImg)
    whiteBishop2 = Piece('white', 'bishop', [420, 588], whiteBishopImg)

    whiteQueen = Piece('white', 'queen', [252, 588], whiteQueenImg)
    whiteKing = King('white', 'king', [336, 588], whiteKingImg)

    whiteList = [whitePawn1, whitePawn2, whitePawn3, whitePawn4, whitePawn5,
                 whitePawn6, whitePawn7, whitePawn8, whiteRook1, whiteRook2,
                 whiteKnight1, whiteKnight2, whiteBishop1, whiteBishop2, whiteQueen,
                 whiteKing]

    def getPossibleMoves(piece):
        global whiteInCheck
        global blackInCheck

        if turnCount == 1:
            whiteInCheck = False
            blackInCheck = False
        else:
            if turn == 'white':
                blackInCheck = False
            if turn == 'black':
                whiteInCheck = False

        friendlyList = []
        enemyList = []

        friendlyKing = None
        enemyKing = None

        piece.possibleMoves = []
        piece.isDefending = []

        piece.isChecking = False

        if piece.color == 'white':
            friendlyList = whiteList
            enemyList = blackList
            friendlyKing = whiteKing
            enemyKing = blackKing
        else:
            friendlyList = blackList
            enemyList = whiteList
            friendlyKing = blackKing
            enemyKing = whiteKing

        if piece.name == 'pawn':
            piece.doubleMoveLastTurn = False
            blockingSingleMove = False
            blockingDoubleMove = False
            offSetNum = -84
            if piece.color == 'black' and not boardFlip:
                offSetNum = 84
            for x in enemyList:
                if (x.position[0] == piece.position[0] - 84 or x.position[0] == piece.position[0] + 84) and x.position[1] == piece.position[1] + offSetNum:
                    piece.possibleMoves.append(x.position)
                    if x.name == 'king':
                        piece.isChecking = True
                if x.position == [piece.position[0], piece.position[1] + offSetNum]:
                    blockingSingleMove = True
                if x.position == [piece.position[0], piece.position[1] + offSetNum * 2]:
                    blockingDoubleMove = True
                if x.position[1] == piece.position[1] and (x.position[0] == piece.position[0] - 84 or x.position[0] == piece.position[0] + 84):
                    if x.name == 'pawn' and x.doubleMoveLastTurn:
                        piece.possibleMoves.append([x.position[0], x.position[1] + offSetNum])

            for x in friendlyList:
                if x.position == [piece.position[0], piece.position[1] + offSetNum]:
                    blockingSingleMove = True
                if x.position == [piece.position[0], piece.position[1] + offSetNum * 2]:
                    blockingDoubleMove = True

            if 0 < piece.position[1] < 588 and not blockingSingleMove:
                piece.possibleMoves.append([piece.position[0], piece.position[1] + offSetNum])

            if (piece.position[1] == 504 or piece.position[1] == 84) and (not blockingSingleMove and not blockingDoubleMove):
                piece.possibleMoves.append([piece.position[0], piece.position[1] + (offSetNum * 2)])

            for x in friendlyList:
                if (x.position[0] == piece.position[0] - 84 or x.position[0] == piece.position[0] + 84) and x.position[1] == piece.position[1] + offSetNum:
                    piece.isDefending.append(x.position)

            piece.isDefending.append([piece.position[0] - 84, piece.position[1] + offSetNum])
            piece.isDefending.append([piece.position[0] + 84, piece.position[1] + offSetNum])

        def verticalHorizontalMoveChecking():
            closestPieceUp = None
            closestPieceDown = None
            closestPieceLeft = None
            closestPieceRight = None
            for x in friendlyList:
                if x.position[0] == piece.position[0] and x != piece:
                    if x.position[1] < piece.position[1]:
                        if closestPieceUp is None or closestPieceUp.position[1] < x.position[1]:
                            closestPieceUp = x
                            piece.isDefending.append(x.position)
                    elif x.position[1] > piece.position[1]:
                        if closestPieceDown is None or closestPieceDown.position[1] > x.position[1]:
                            closestPieceDown = x
                            piece.isDefending.append(x.position)
                if x.position[1] == piece.position[1] and x != piece:
                    if x.position[0] < piece.position[0]:
                        if closestPieceLeft is None or closestPieceLeft.position[0] < x.position[0]:
                            closestPieceLeft = x
                            piece.isDefending.append(x.position)
                    elif x.position[0] > piece.position[0]:
                        if closestPieceRight is None or closestPieceRight.position[0] > x.position[0]:
                            closestPieceRight = x
                            piece.isDefending.append(x.position)
            for x in enemyList:
                if x.position[0] == piece.position[0]:
                    if x.position[1] < piece.position[1]:
                        if closestPieceUp is None or closestPieceUp.position[1] < x.position[1]:
                            closestPieceUp = x
                    elif x.position[1] > piece.position[1]:
                        if closestPieceDown is None or closestPieceDown.position[1] > x.position[1]:
                            closestPieceDown = x
                if x.position[1] == piece.position[1]:
                    if x.position[0] < piece.position[0]:
                        if closestPieceLeft is None or closestPieceLeft.position[0] < x.position[0]:
                            closestPieceLeft = x
                    elif x.position[0] > piece.position[0]:
                        if closestPieceRight is None or closestPieceRight.position[0] > x.position[0]:
                            closestPieceRight = x

            pinnedPiece = None
            if enemyKing.position[0] == piece.position[0]:
                if enemyKing.position[1] < piece.position[1]:
                    breakLoop = False
                    yPosition = piece.position[1] - 84
                    while yPosition > enemyKing.position[1]:
                        for x in enemyList:
                            if x.position == [piece.position[0], yPosition]:
                                if pinnedPiece is None:
                                    pinnedPiece = x
                                    pinnedPiece.pinningPiece = piece
                                    break
                                else:
                                    pinnedPiece.pinningPiece = None
                                    pinnedPiece = None
                                    break
                        for x in friendlyList:
                            if x.position == [piece.position[0], yPosition]:
                                if pinnedPiece is not None:
                                    pinnedPiece.pinningPiece = None
                                    pinnedPiece = None
                                    breakLoop = True
                                    break
                        if breakLoop:
                            break
                        yPosition -= 84
                    if pinnedPiece is None:
                        yPosition -= 84
                        while yPosition >= 0:
                            piece.isDefending.append([piece.position[0], yPosition])
                            yPosition -= 84

                elif enemyKing.position[1] > piece.position[1]:
                    breakLoop = False
                    yPosition = piece.position[1] + 84
                    while yPosition < enemyKing.position[1]:
                        for x in enemyList:
                            if x.position == [piece.position[0], yPosition]:
                                if pinnedPiece is None:
                                    pinnedPiece = x
                                    pinnedPiece.pinningPiece = piece
                                    break
                                else:
                                    pinnedPiece.pinningPiece = None
                                    pinnedPiece = None
                                    break
                        for x in friendlyList:
                            if x.position == [piece.position[0], yPosition]:
                                if pinnedPiece is not None:
                                    pinnedPiece.pinningPiece = None
                                    pinnedPiece = None
                                    breakLoop = True
                                    break
                        if breakLoop:
                            break
                        yPosition += 84
                    if pinnedPiece is None:
                        yPosition += 84
                        while yPosition <= 588:
                            piece.isDefending.append([piece.position[0], yPosition])
                            yPosition += 84

            elif enemyKing.position[1] == piece.position[1]:
                if enemyKing.position[0] < piece.position[0]:
                    breakLoop = False
                    xPosition = piece.position[0] - 84
                    while xPosition > enemyKing.position[0]:
                        for x in enemyList:
                            if x.position == [xPosition, piece.position[1]]:
                                if pinnedPiece is None:
                                    pinnedPiece = x
                                    pinnedPiece.pinningPiece = piece
                                else:
                                    pinnedPiece.pinningPiece = None
                                    pinnedPiece = None
                                    break
                        for x in friendlyList:
                            if x.position == [xPosition, piece.position[1]]:
                                if pinnedPiece is not None:
                                    pinnedPiece.pinningPiece = None
                                    pinnedPiece = None
                                    breakLoop = True
                                    break
                        if breakLoop:
                            break
                        xPosition -= 84
                    if pinnedPiece is None:
                        xPosition -= 84
                        while xPosition >= 0:
                            piece.isDefending.append([xPosition, piece.position[1]])
                            xPosition -= 84

                elif enemyKing.position[0] > piece.position[0]:
                    breakLoop = False
                    xPosition = piece.position[0] + 84
                    while xPosition < enemyKing.position[0]:
                        for x in enemyList:
                            if x.position == [xPosition, piece.position[1]]:
                                if pinnedPiece is None:
                                    pinnedPiece = x
                                    pinnedPiece.pinningPiece = piece
                                else:
                                    pinnedPiece.pinningPiece = None
                                    pinnedPiece = None
                                    break
                        for x in friendlyList:
                            if x.position == [xPosition, piece.position[1]]:
                                if pinnedPiece is not None:
                                    pinnedPiece.pinningPiece = None
                                    pinnedPiece = None
                                    breakLoop = True
                                    break
                        if breakLoop:
                            break
                        xPosition += 84
                    if pinnedPiece is None:
                        xPosition += 84
                        while xPosition <= 588:
                            piece.isDefending.append([xPosition, piece.position[1]])
                            xPosition += 84

            if closestPieceUp is not None:
                yPosition = piece.position[1] - 84
                while yPosition > closestPieceUp.position[1]:
                    piece.possibleMoves.append([piece.position[0], yPosition])
                    yPosition -= 84
                if closestPieceUp.color == enemyList[0].color:
                    piece.possibleMoves.append(closestPieceUp.position)
                    if closestPieceUp.name == "king":
                        piece.isChecking = True
            else:
                yPosition = piece.position[1] - 84
                while yPosition >= 0:
                    piece.possibleMoves.append([piece.position[0], yPosition])
                    yPosition -= 84

            if closestPieceDown is not None:
                yPosition = piece.position[1] + 84
                while yPosition < closestPieceDown.position[1]:
                    piece.possibleMoves.append([piece.position[0], yPosition])
                    yPosition += 84
                if closestPieceDown.color == enemyList[0].color:
                    piece.possibleMoves.append(closestPieceDown.position)
                    if closestPieceDown.name == "king":
                        blackInCheck = True
                        piece.isChecking = True
            else:
                yPosition = piece.position[1] + 84
                while yPosition <= 588:
                    piece.possibleMoves.append([piece.position[0], yPosition])
                    yPosition += 84

            if closestPieceLeft is not None:
                xPosition = piece.position[0] - 84
                while xPosition > closestPieceLeft.position[0]:
                    piece.possibleMoves.append([xPosition, piece.position[1]])
                    xPosition -= 84
                if closestPieceLeft.color == enemyList[0].color:
                    piece.possibleMoves.append(closestPieceLeft.position)
                    if closestPieceLeft.name == "king":
                        blackInCheck = True
                        piece.isChecking = True
            else:
                xPosition = piece.position[0] - 84
                while xPosition >= 0:
                    piece.possibleMoves.append([xPosition, piece.position[1]])
                    xPosition -= 84

            if closestPieceRight is not None:
                xPosition = piece.position[0] + 84
                while xPosition < closestPieceRight.position[0]:
                    piece.possibleMoves.append([xPosition, piece.position[1]])
                    xPosition += 84
                if closestPieceRight.color == enemyList[0].color:
                    piece.possibleMoves.append(closestPieceRight.position)
                    if closestPieceRight.name == "king":
                        blackInCheck = True
                        piece.isChecking = True
            else:
                xPosition = piece.position[0] + 84
                while xPosition <= 588:
                    piece.possibleMoves.append([xPosition, piece.position[1]])
                    xPosition += 84

        if piece.name == 'rook':
            verticalHorizontalMoveChecking()
            for x in piece.possibleMoves:
                piece.isDefending.append(x)

        if piece.name == 'knight':
            if piece.position[1] >= 168:
                if piece.position[0] > 0:
                    piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] - (84 * 2)])
                if piece.position[0] < 588:
                    piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] - (84 * 2)])
            if piece.position[1] <= 420:
                if piece.position[0] > 0:
                    piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] + (84 * 2)])
                if piece.position[0] < 588:
                    piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] + (84 * 2)])
            if piece.position[0] >= 168:
                if piece.position[1] > 0:
                    piece.possibleMoves.append([piece.position[0] - (84 * 2), piece.position[1] - 84])
                if piece.position[1] < 588:
                    piece.possibleMoves.append([piece.position[0] - (84 * 2), piece.position[1] + 84])
            if piece.position[0] <= 420:
                if piece.position[1] > 0:
                    piece.possibleMoves.append([piece.position[0] + (84 * 2), piece.position[1] - 84])
                if piece.position[1] < 588:
                    piece.possibleMoves.append([piece.position[0] + (84 * 2), piece.position[1] + 84])

            removeList = []
            for x in piece.possibleMoves:
                piece.isDefending.append(x)
                if enemyKing.position == x:
                    blackInCheck = True
                    piece.isChecking = True
                for y in friendlyList:
                    if y.position == x and removeList.count(x) < 1:
                        removeList.append(x)
                        break

            for x in removeList:
                canRemove = False
                for y in piece.possibleMoves:
                    if y == x:
                        canRemove = True
                if canRemove:
                    piece.possibleMoves.remove(x)

        def diagnolMoveChecking():
            xPosition = piece.position[0] - 84
            yPosition = piece.position[1] - 84
            loneEnemyPiece = None
            breakLoop = False
            while xPosition >= 0 and yPosition >= 0:
                for x in friendlyList:
                    if x.position == [xPosition, yPosition]:
                        piece.isDefending.append(x.position)
                        breakLoop = True
                        break
                if breakLoop:
                    break
                for x in enemyList:
                    if x.position == [xPosition, yPosition]:
                        if loneEnemyPiece is None:
                            loneEnemyPiece = x
                            piece.possibleMoves.append(loneEnemyPiece.position)
                            if loneEnemyPiece.name == "king":
                                piece.isChecking = True
                        elif x.name == "king" and loneEnemyPiece is not None:
                            piece.possibleMoves.append(loneEnemyPiece.position)
                            if loneEnemyPiece != enemyKing:
                                loneEnemyPiece.pinningPiece = piece
                        elif loneEnemyPiece is not None:
                            if x.name != 'king':
                                breakLoop = True
                            break
                if breakLoop:
                    break

                if loneEnemyPiece is None:
                    piece.possibleMoves.append([xPosition, yPosition])
                elif loneEnemyPiece.name == 'king' and [xPosition, yPosition] != loneEnemyPiece.position:
                    piece.isDefending.append([xPosition, yPosition])

                xPosition -= 84
                yPosition -= 84

            xPosition = piece.position[0] + 84
            yPosition = piece.position[1] - 84
            loneEnemyPiece = None
            breakLoop = False
            while xPosition <= 588 and yPosition >= 0:
                for x in friendlyList:
                    if x.position == [xPosition, yPosition]:
                        piece.isDefending.append(x.position)
                        breakLoop = True
                        break
                if breakLoop:
                    break
                for x in enemyList:
                    if x.position == [xPosition, yPosition]:
                        if loneEnemyPiece is None:
                            loneEnemyPiece = x
                            piece.possibleMoves.append(loneEnemyPiece.position)
                            if loneEnemyPiece.name == "king":
                                piece.isChecking = True
                        elif x.name == "king" and loneEnemyPiece is not None:
                            piece.possibleMoves.append(loneEnemyPiece.position)
                            if loneEnemyPiece != enemyKing:
                                loneEnemyPiece.pinningPiece = piece
                        elif loneEnemyPiece is not None:
                            if x.name != 'king':
                                breakLoop = True
                            break
                if breakLoop:
                    break

                if loneEnemyPiece is None:
                    piece.possibleMoves.append([xPosition, yPosition])
                elif loneEnemyPiece.name == 'king' and [xPosition, yPosition] != loneEnemyPiece.position:
                    piece.isDefending.append([xPosition, yPosition])

                xPosition += 84
                yPosition -= 84

            xPosition = piece.position[0] - 84
            yPosition = piece.position[1] + 84
            loneEnemyPiece = None
            breakLoop = False
            while xPosition >= 0 and yPosition <= 588:
                for x in friendlyList:
                    if x.position == [xPosition, yPosition]:
                        piece.isDefending.append(x.position)
                        breakLoop = True
                        break
                if breakLoop:
                    break
                for x in enemyList:
                    if x.position == [xPosition, yPosition]:
                        if loneEnemyPiece is None:
                            loneEnemyPiece = x
                            piece.possibleMoves.append(loneEnemyPiece.position)
                            if loneEnemyPiece.name == "king":
                                piece.isChecking = True
                        elif x.name == "king" and loneEnemyPiece is not None:
                            piece.possibleMoves.append(loneEnemyPiece.position)
                            if loneEnemyPiece != enemyKing:
                                loneEnemyPiece.pinningPiece = piece
                        elif loneEnemyPiece is not None:
                            if x.name != 'king':
                                breakLoop = True
                            break
                if breakLoop:
                    break

                if loneEnemyPiece is None:
                    piece.possibleMoves.append([xPosition, yPosition])
                elif loneEnemyPiece.name == 'king' and [xPosition, yPosition] != loneEnemyPiece.position:
                    piece.isDefending.append([xPosition, yPosition])

                xPosition -= 84
                yPosition += 84

            xPosition = piece.position[0] + 84
            yPosition = piece.position[1] + 84
            loneEnemyPiece = None
            breakLoop = False
            while xPosition <= 588 and yPosition <= 588:
                for x in friendlyList:
                    if x.position == [xPosition, yPosition]:
                        piece.isDefending.append(x.position)
                        breakLoop = True
                        break
                if breakLoop:
                    break
                for x in enemyList:
                    if x.position == [xPosition, yPosition]:
                        if loneEnemyPiece is None:
                            loneEnemyPiece = x
                            piece.possibleMoves.append(loneEnemyPiece.position)
                            if loneEnemyPiece.name == "king":
                                piece.isChecking = True
                        elif x.name == "king" and loneEnemyPiece is not None:
                            piece.possibleMoves.append(loneEnemyPiece.position)
                            if loneEnemyPiece != enemyKing:
                                loneEnemyPiece.pinningPiece = piece
                        elif loneEnemyPiece is not None:
                            if x.name != 'king':
                                breakLoop = True
                            break
                if breakLoop:
                    break

                if loneEnemyPiece is None:
                    piece.possibleMoves.append([xPosition, yPosition])
                elif loneEnemyPiece.name == 'king' and [xPosition, yPosition] != loneEnemyPiece.position:
                    piece.isDefending.append([xPosition, yPosition])

                xPosition += 84
                yPosition += 84

        if piece.name == 'bishop':
            diagnolMoveChecking()
            for x in piece.possibleMoves:
                piece.isDefending.append(x)

        if piece.name == 'queen':
            verticalHorizontalMoveChecking()
            for x in piece.possibleMoves:
                piece.isDefending.append(x)
            diagnolMoveChecking()
            for x in piece.possibleMoves:
                piece.isDefending.append(x)

        if piece.name == 'king':
            piece.possibleMoves.append([piece.position[0] - 84, piece.position[1]])
            piece.possibleMoves.append([piece.position[0] + 84, piece.position[1]])
            piece.possibleMoves.append([piece.position[0], piece.position[1] - 84])
            piece.possibleMoves.append([piece.position[0], piece.position[1] + 84])
            piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] - 84])
            piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] - 84])
            piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] + 84])
            piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] + 84])

            if not piece.hasMoved:
                yPosition = 0
                rook1 = blackRook1
                rook2 = blackRook2
                if piece.color == 'white':
                    yPosition = 588
                    rook1 = whiteRook1
                    rook2 = whiteRook2
                if not rook1.hasMoved and piece.color == rook1.color:
                    castleBlocked = False
                    for x in friendlyList:
                        if rook1.position[0] < x.position[0] < piece.position[0] and x.position[1] == yPosition:
                            castleBlocked = True
                            break
                    for x in enemyList:
                        if rook1.position[0] < x.position[0] < piece.position[0] and x.position[1] == yPosition:
                            castleBlocked = True
                            break
                        breakLoop = False
                        for y in x.possibleMoves:
                            if (rook1.position[0] < y[0] < piece.position[0] and y[1] == yPosition) or y == piece.position:
                                castleBlocked = True
                                breakLoop = True
                                break
                        if breakLoop:
                            break
                    if not castleBlocked:
                        piece.possibleMoves.append([piece.position[0] - 168, yPosition])
                if not rook2.hasMoved and piece.color == rook2.color:
                    castleBlocked = False
                    for x in friendlyList:
                        if rook2.position[0] > x.position[0] > piece.position[0] and x.position[1] == yPosition:
                            castleBlocked = True
                            break
                    for x in enemyList:
                        if rook2.position[0] > x.position[0] > piece.position[0] and x.position[1] == yPosition:
                            castleBlocked = True
                            break
                        breakLoop = False
                        for y in x.possibleMoves:
                            if (rook2.position[0] > y[0] > piece.position[0] and y[1] == yPosition) or y == piece.position:
                                castleBlocked = True
                                breakLoop = True
                                break
                        if breakLoop:
                            break
                    if not castleBlocked:
                        piece.possibleMoves.append([piece.position[0] + 168, yPosition])

            removeList = []
            for x in piece.possibleMoves:
                for y in friendlyList:
                    if y.position == x and removeList.count(x) < 1:
                        piece.isDefending.append(x)
                        removeList.append(x)
                        break

            for x in removeList:
                canRemove = False
                for y in piece.possibleMoves:
                    if y == x:
                        canRemove = True
                if canRemove:
                    piece.possibleMoves.remove(x)
            removeList.clear()

            for x in piece.possibleMoves:
                for y in enemyList:
                    for z in y.isDefending:
                        if z == x:
                            if removeList.count(x) < 1:
                                removeList.append(x)
                                break

            for x in removeList:
                canRemove = False
                for y in piece.possibleMoves:
                    if y == x:
                        canRemove = True
                if canRemove:
                    piece.possibleMoves.remove(x)

        if piece.pinningPiece is not None:
            removeList = []
            pinningLikeRook = False
            if piece.pinningPiece.name == "rook" or piece.pinningPiece.name == "queen":
                if piece.pinningPiece.position[0] == piece.position[0]:
                    pinningLikeRook = True
                    if friendlyKing.position[0] != piece.position[0] or (not (friendlyKing.position[1] < piece.position[1] < piece.pinningPiece.position[1])) and not (piece.pinningPiece.position[1] < piece.position[1] < friendlyKing.position[1]):
                        piece.pinningPiece = None
                elif piece.pinningPiece.position[1] == piece.position[1]:
                    pinningLikeRook = True
                    if friendlyKing.position[1] != piece.position[1] or (not (friendlyKing.position[0] < piece.position[0] < piece.pinningPiece.position[0])) and not (piece.pinningPiece.position[0] < piece.position[0] < friendlyKing.position[0]):
                        piece.pinningPiece = None
            if piece.pinningPiece is not None and (piece.pinningPiece.name == "bishop" or piece.pinningPiece.name == "queen") and not pinningLikeRook:
                pieceIsPinned = False
                if piece.pinningPiece.position[0] < piece.position[0]:
                    if piece.pinningPiece.position[1] > piece.position[1]:
                        xPosition = piece.pinningPiece.position[0] + 84
                        yPosition = piece.pinningPiece.position[1] - 84
                        breakLoop = False
                        while xPosition <= 588 and yPosition >= 0:
                            for x in enemyList:
                                if x.position == [xPosition, yPosition]:
                                    breakLoop = True
                                    break
                            if breakLoop:
                                break
                            for x in friendlyList:
                                if x.position == [xPosition, yPosition] and x != piece:
                                    if x.name == "king":
                                        pieceIsPinned = True
                                        breakLoop = True
                                        break
                                    else:
                                        breakLoop = True
                                        break
                            if breakLoop:
                                break
                            xPosition += 84
                            yPosition -= 84
                    elif piece.pinningPiece.position[1] < piece.position[1]:
                        xPosition = piece.pinningPiece.position[0] + 84
                        yPosition = piece.pinningPiece.position[1] + 84
                        breakLoop = False
                        while xPosition <= 588 and yPosition <= 588:
                            for x in enemyList:
                                if x.position == [xPosition, yPosition]:
                                    breakLoop = True
                                    break
                            if breakLoop:
                                break
                            for x in friendlyList:
                                if x.position == [xPosition, yPosition] and x != piece:
                                    if x.name == "king":
                                        pieceIsPinned = True
                                        breakLoop = True
                                        break
                                    else:
                                        breakLoop = True
                                        break
                            if breakLoop:
                                break
                            xPosition += 84
                            yPosition += 84
                elif piece.pinningPiece.position[0] > piece.position[0]:
                    if piece.pinningPiece.position[1] > piece.position[1]:
                        xPosition = piece.pinningPiece.position[0] - 84
                        yPosition = piece.pinningPiece.position[1] - 84
                        breakLoop = False
                        while xPosition >= 0 and yPosition >= 0:
                            for x in enemyList:
                                if x.position == [xPosition, yPosition]:
                                    breakLoop = True
                                    break
                            if breakLoop:
                                break
                            for x in friendlyList:
                                if x.position == [xPosition, yPosition] and x != piece:
                                    if x.name == "king":
                                        pieceIsPinned = True
                                        breakLoop = True
                                        break
                                    else:
                                        breakLoop = True
                                        break
                            if breakLoop:
                                break
                            xPosition -= 84
                            yPosition -= 84
                    elif piece.pinningPiece.position[1] < piece.position[1]:
                        xPosition = piece.pinningPiece.position[0] - 84
                        yPosition = piece.pinningPiece.position[1] + 84
                        breakLoop = False
                        while xPosition >= 0 and yPosition <= 588:
                            for x in enemyList:
                                if x.position == [xPosition, yPosition]:
                                    breakLoop = True
                                    break
                            if breakLoop:
                                break
                            for x in friendlyList:
                                if x.position == [xPosition, yPosition] and x != piece:
                                    if x.name == "king":
                                        pieceIsPinned = True
                                        breakLoop = True
                                        break
                                    else:
                                        breakLoop = True
                                        break
                            if breakLoop:
                                break
                            xPosition -= 84
                            yPosition += 84

                if not pieceIsPinned:
                    piece.pinningPiece = None

            if piece.pinningPiece is not None:
                for x in piece.possibleMoves:
                    if piece.pinningPiece.name == "rook":
                        if piece.pinningPiece.position[0] == piece.position[0]:
                            if x[0] != piece.position[0] and removeList.count(x) < 1:
                                removeList.append(x)
                        elif piece.pinningPiece.position[1] == piece.position[1]:
                            if x[1] != piece.position[1] and removeList.count(x) < 1:
                                removeList.append(x)
                    elif piece.pinningPiece.name == "bishop":
                        canMove = False
                        if piece.pinningPiece.position[0] > piece.position[0]:
                            if piece.pinningPiece.position[1] < piece.position[1]:
                                for y in piece.pinningPiece.possibleMoves:
                                    if y[0] < piece.pinningPiece.position[0] and y[1] > piece.pinningPiece.position[1]:
                                        if x == y:
                                            canMove = True
                            elif piece.pinningPiece.position[1] > piece.position[1]:
                                for y in piece.pinningPiece.possibleMoves:
                                    if y[0] < piece.pinningPiece.position[0] and y[1] < piece.pinningPiece.position[1]:
                                        if x == y:
                                            canMove = True
                        elif piece.pinningPiece.position[0] < piece.position[0]:
                            if piece.pinningPiece.position[1] < piece.position[1]:
                                for y in piece.pinningPiece.possibleMoves:
                                    if y[0] > piece.pinningPiece.position[0] and y[1] > piece.pinningPiece.position[1]:
                                        if x == y:
                                            canMove = True
                            elif piece.pinningPiece.position[1] > piece.position[1]:
                                for y in piece.pinningPiece.possibleMoves:
                                    if y[0] > piece.pinningPiece.position[0] and y[1] < piece.pinningPiece.position[1]:
                                        if x == y:
                                            canMove = True

                        if not canMove and x != piece.pinningPiece.position and removeList.count(x) < 1:
                            removeList.append(x)

                    elif piece.pinningPiece.name == "queen":
                        canMove = False
                        if piece.pinningPiece.position[0] > piece.position[0]:
                            if piece.pinningPiece.position[1] < piece.position[1]:
                                for y in piece.pinningPiece.possibleMoves:
                                    if y[0] < piece.pinningPiece.position[0] and y[1] > piece.pinningPiece.position[1]:
                                        if x == y:
                                            canMove = True
                            elif piece.pinningPiece.position[1] > piece.position[1]:
                                for y in piece.pinningPiece.possibleMoves:
                                    if y[0] < piece.pinningPiece.position[0] and y[1] < piece.pinningPiece.position[1]:
                                        if x == y:
                                            canMove = True
                        elif piece.pinningPiece.position[0] < piece.position[0]:
                            if piece.pinningPiece.position[1] < piece.position[1]:
                                for y in piece.pinningPiece.possibleMoves:
                                    if y[0] > piece.pinningPiece.position[0] and y[1] > piece.pinningPiece.position[1]:
                                        if x == y:
                                            canMove = True
                            elif piece.pinningPiece.position[1] > piece.position[1]:
                                for y in piece.pinningPiece.possibleMoves:
                                    if y[0] > piece.pinningPiece.position[0] and y[1] < piece.pinningPiece.position[1]:
                                        if x == y:
                                            canMove = True

                        if not canMove and x != piece.pinningPiece.position and removeList.count(x) < 1:
                            removeList.append(x)

                        if piece.pinningPiece.position[0] == piece.position[0]:
                            if x[0] != piece.position[0] and removeList.count(x) < 1:
                                removeList.append(x)
                        elif piece.pinningPiece.position[1] == piece.position[1]:
                            if x[1] != piece.position[1] and removeList.count(x) < 1:
                                removeList.append(x)

            for x in removeList:
                canRemove = False
                for y in piece.possibleMoves:
                    if y == x:
                        canRemove = True
                if canRemove:
                    piece.possibleMoves.remove(x)

        for x in enemyList:
            if x.isChecking:
                if friendlyList[0].color == 'white':
                    whiteInCheck = True
                else:
                    blackInCheck = True

        if ((whiteInCheck and friendlyKing.color == 'white') or (blackInCheck and friendlyKing.color == 'black')) and piece != friendlyKing:
            loneChecker = None
            for x in enemyList:
                if x.isChecking:
                    if loneChecker is None:
                        loneChecker = x
                    else:
                        loneChecker = None
                        for y in friendlyList:
                            if y != friendlyKing:
                                y.possibleMoves = []
                                break
            removeList = []
            if loneChecker is not None:
                if loneChecker.name == 'pawn':
                    for x in piece.possibleMoves:
                        if x != loneChecker.position and removeList.count(x) < 1:
                            removeList.append(x)

                elif loneChecker.name == 'rook':
                    for x in piece.possibleMoves:
                        if loneChecker.position == x:
                            continue
                        elif loneChecker.position[0] < friendlyKing.position[0]:
                            if (x[1] != loneChecker.position[1] or x[0] >= friendlyKing.position[0] or x[0] < loneChecker.position[0]) and removeList.count(x) < 1:
                                removeList.append(x)
                        elif loneChecker.position[0] > friendlyKing.position[0]:
                            if (x[1] != loneChecker.position[1] or x[0] <= friendlyKing.position[0] or x[0] > loneChecker.position[0]) and removeList.count(x) < 1:
                                removeList.append(x)
                        elif loneChecker.position[1] < friendlyKing.position[1]:
                            if (x[0] != loneChecker.position[0] or x[1] >= friendlyKing.position[1] or x[1] < loneChecker.position[1]) and removeList.count(x) < 1:
                                removeList.append(x)
                        elif loneChecker.position[1] > friendlyKing.position[1]:
                            if (x[0] != loneChecker.position[0] or x[1] <= friendlyKing.position[1] or x[1] > loneChecker.position[1]) and removeList.count(x) < 1:
                                removeList.append(x)
                elif loneChecker.name == 'knight':
                    for x in piece.possibleMoves:
                        if x != loneChecker.position and removeList.count(x) < 1:
                            removeList.append(x)
                elif loneChecker.name == 'bishop':
                    for x in piece.possibleMoves:
                        canMove = False
                        if loneChecker.position[0] > friendlyKing.position[0]:
                            if loneChecker.position[1] < friendlyKing.position[1]:
                                for y in loneChecker.possibleMoves:
                                    if y[0] < loneChecker.position[0] and y[1] > loneChecker.position[1]:
                                        if x == y:
                                            canMove = True
                            elif loneChecker.position[1] > friendlyKing.position[1]:
                                for y in loneChecker.possibleMoves:
                                    if y[0] < loneChecker.position[0] and y[1] < loneChecker.position[1]:
                                        if x == y:
                                            canMove = True
                        elif loneChecker.position[0] < friendlyKing.position[0]:
                            if loneChecker.position[1] < friendlyKing.position[1]:
                                for y in loneChecker.possibleMoves:
                                    if y[0] > loneChecker.position[0] and y[1] > loneChecker.position[1]:
                                        if x == y:
                                            canMove = True
                            elif loneChecker.position[1] > friendlyKing.position[1]:
                                for y in loneChecker.possibleMoves:
                                    if y[0] > loneChecker.position[0] and y[1] < loneChecker.position[1]:
                                        if x == y:
                                            canMove = True

                        if not canMove and x != loneChecker.position and removeList.count(x) < 1:
                            removeList.append(x)

                elif loneChecker.name == 'queen':
                    checkingLikeRook = False
                    if loneChecker.position[0] == friendlyKing.position[0] or loneChecker.position[1] == friendlyKing.position[1]:
                        checkingLikeRook = True
                    if not checkingLikeRook:
                        for x in piece.possibleMoves:
                            canMove = False
                            if loneChecker.position[0] > friendlyKing.position[0]:
                                if loneChecker.position[1] < friendlyKing.position[1]:
                                    for y in loneChecker.possibleMoves:
                                        if y[0] < loneChecker.position[0] and y[1] > loneChecker.position[1]:
                                            if x == y:
                                                canMove = True
                                elif loneChecker.position[1] > friendlyKing.position[1]:
                                    for y in loneChecker.possibleMoves:
                                        if y[0] < loneChecker.position[0] and y[1] < loneChecker.position[1]:
                                            if x == y:
                                                canMove = True
                            elif loneChecker.position[0] < friendlyKing.position[0]:
                                if loneChecker.position[1] < friendlyKing.position[1]:
                                    for y in loneChecker.possibleMoves:
                                        if y[0] > loneChecker.position[0] and y[1] > loneChecker.position[1]:
                                            if x == y:
                                                canMove = True
                                elif loneChecker.position[1] > friendlyKing.position[1]:
                                    for y in loneChecker.possibleMoves:
                                        if y[0] > loneChecker.position[0] and y[1] < loneChecker.position[1]:
                                            if x == y:
                                                canMove = True

                            if not canMove and x != loneChecker.position and removeList.count(x) < 1:
                                removeList.append(x)
                    else:
                        for x in piece.possibleMoves:
                            if loneChecker.position == x:
                                continue
                            elif loneChecker.position[0] < friendlyKing.position[0] and removeList.count(x) < 1:
                                if x[1] != loneChecker.position[1] or x[0] >= friendlyKing.position[0] or x[0] < loneChecker.position[0]:
                                    removeList.append(x)
                            elif loneChecker.position[0] > friendlyKing.position[0] and removeList.count(x) < 1:
                                if x[1] != loneChecker.position[1] or x[0] <= friendlyKing.position[0] or x[0] > loneChecker.position[0]:
                                    removeList.append(x)
                            elif loneChecker.position[1] < friendlyKing.position[1] and removeList.count(x) < 1:
                                if x[0] != loneChecker.position[0] or x[1] >= friendlyKing.position[1] or x[1] < loneChecker.position[1]:
                                    removeList.append(x)
                            elif loneChecker.position[1] > friendlyKing.position[1] and removeList.count(x) < 1:
                                if x[0] != loneChecker.position[0] or x[1] <= friendlyKing.position[1] or x[1] > loneChecker.position[1]:
                                    removeList.append(x)

                for x in removeList:
                    canRemove = False
                    for y in piece.possibleMoves:
                        if y == x:
                            canRemove = True
                    if canRemove:
                        piece.possibleMoves.remove(x)

        removeList = []
        for x in piece.possibleMoves:
            if x[0] < 0 or x[0] > 588 or x[1] < 0 or x[1] > 588:
                removeList.append(x)

        for x in removeList:
            canRemove = False
            for y in piece.possibleMoves:
                if y == x:
                    canRemove = True
            if canRemove:
                piece.possibleMoves.remove(x)

    for x in whiteList:
        getPossibleMoves(x)

    for x in blackList:
        getPossibleMoves(x)

    def pawnConversion(pawn):
        while True:
            conversionType = input("Would you like a 'queen', 'rook', 'knight', or 'bishop'?\n").casefold()
            if conversionType == 'queen':
                piece.name = conversionType
                if piece.color == 'white':
                    piece.img = whiteQueenImg
                else:
                    piece.img = blackQueenImg
                break
            elif conversionType == 'rook':
                piece.name = conversionType
                if piece.color == 'white':
                    piece.img = whiteRookImg
                else:
                    piece.img = blackRookImg
                break
            elif conversionType == 'knight':
                piece.name = conversionType
                if piece.color == 'white':
                    piece.img = whiteKnightImg
                else:
                    piece.img = blackKnightImg
                break
            elif conversionType == 'bishop':
                piece.name = conversionType
                if piece.color == 'white':
                    piece.img = whiteBishopImg
                else:
                    piece.img = blackBishopImg
                break
            else:
                print('Invalid Input, please try again\n')

    def checkForEndgame():
        whiteNoMoves = True
        blackNoMoves = True
        for piece in whiteList:
            if len(piece.possibleMoves) > 0:
                whiteNoMoves = False
                break

        for piece in blackList:
            if len(piece.possibleMoves) > 0:
                blackNoMoves = False
                break

        if whiteNoMoves and turn == 'black':
            for piece in blackList:
                if piece.isChecking:
                    whiteInCheck = True
            if whiteInCheck:
                print("Checkmate! Black Wins!")
                return True
            else:
                print("Stalemate! Nobody Wins!")
                return True

        if blackNoMoves and turn == 'white':
            for piece in whiteList:
                if piece.isChecking:
                    blackInCheck = True
            if blackInCheck:
                print("Checkmate! White Wins!")
                return True
            else:
                print("Stalemate! Nobody Wins!")
                return True

        return False

    def resetBoard():
        win.fill((255, 255, 255))
        win.blit(chessBoard, (0, 0))

        blackPawn1 = Pawn('black', 'pawn', [0, 84], blackPawnImg, False, False, None, [], [], False)
        blackPawn2 = Pawn('black', 'pawn', [84, 84], blackPawnImg, False, False, None, [], [], False)
        blackPawn3 = Pawn('black', 'pawn', [168, 84], blackPawnImg, False, False, None, [], [], False)
        blackPawn4 = Pawn('black', 'pawn', [252, 84], blackPawnImg, False, False, None, [], [], False)
        blackPawn5 = Pawn('black', 'pawn', [336, 84], blackPawnImg, False, False, None, [], [], False)
        blackPawn6 = Pawn('black', 'pawn', [420, 84], blackPawnImg, False, False, None, [], [], False)
        blackPawn7 = Pawn('black', 'pawn', [504, 84], blackPawnImg, False, False, None, [], [], False)
        blackPawn8 = Pawn('black', 'pawn', [588, 84], blackPawnImg, False, False, None, [], [], False)

        for x in range(0, 8):
            win.blit(blackPawnImg, (84 * x, 84))

        blackRook1 = Rook('black', 'rook', [0, 0], blackRookImg, False, False, None, [], [], False)
        blackRook2 = Rook('black', 'rook', [588, 0], blackRookImg, False, False, None, [], [], False)

        win.blit(blackRookImg, blackRook1.position)
        win.blit(blackRookImg, blackRook2.position)

        blackKnight1 = Piece('black', 'knight', [84, 0], blackKnightImg, False, False, None, [], [])
        blackKnight2 = Piece('black', 'knight', [504, 0], blackKnightImg, False, False, None, [], [])

        win.blit(blackKnightImg, blackKnight1.position)
        win.blit(blackKnightImg, blackKnight2.position)

        blackBishop1 = Piece('black', 'bishop', [168, 0], blackBishopImg, False, False, None, [], [])
        blackBishop2 = Piece('black', 'bishop', [420, 0], blackBishopImg, False, False, None, [], [])

        win.blit(blackBishopImg, blackBishop1.position)
        win.blit(blackBishopImg, blackBishop2.position)

        blackQueen = Piece('black', 'queen', [252, 0], blackQueenImg, False, False, None, [], [])
        blackKing = King('black', 'king', [336, 0], blackKingImg, False, False, None, [], [], False)

        win.blit(blackQueenImg, blackQueen.position)
        win.blit(blackKingImg, blackKing.position)

        blackList = [blackPawn1, blackPawn2, blackPawn3, blackPawn4, blackPawn5,
                     blackPawn6, blackPawn7, blackPawn8, blackRook1, blackRook2,
                     blackKnight1, blackKnight2, blackBishop1, blackBishop2, blackQueen,
                     blackKing]

        whitePawn1 = Pawn('white', 'pawn', [0, 504], whitePawnImg, False, False, None, [], [], False)
        whitePawn2 = Pawn('white', 'pawn', [84, 504], whitePawnImg, False, False, None, [], [], False)
        whitePawn3 = Pawn('white', 'pawn', [168, 504], whitePawnImg, False, False, None, [], [], False)
        whitePawn4 = Pawn('white', 'pawn', [252, 504], whitePawnImg, False, False, None, [], [], False)
        whitePawn5 = Pawn('white', 'pawn', [336, 504], whitePawnImg, False, False, None, [], [], False)
        whitePawn6 = Pawn('white', 'pawn', [420, 504], whitePawnImg, False, False, None, [], [], False)
        whitePawn7 = Pawn('white', 'pawn', [504, 504], whitePawnImg, False, False, None, [], [], False)
        whitePawn8 = Pawn('white', 'pawn', [588, 504], whitePawnImg, False, False, None, [], [], False)

        for x in range(0, 8):
            win.blit(whitePawnImg, (84 * x, 504))

        whiteRook1 = Rook('white', 'rook', [0, 588], whiteRookImg, False, False, None, [], [], False)
        whiteRook2 = Rook('white', 'rook', [588, 588], whiteRookImg, False, False, None, [], [], False)

        win.blit(whiteRookImg, whiteRook1.position)
        win.blit(whiteRookImg, whiteRook2.position)

        whiteKnight1 = Piece('white', 'knight', [84, 588], whiteKnightImg, False, False, None, [], [])
        whiteKnight2 = Piece('white', 'knight', [504, 588], whiteKnightImg, False, False, None, [], [])

        win.blit(whiteKnightImg, whiteKnight1.position)
        win.blit(whiteKnightImg, whiteKnight2.position)

        whiteBishop1 = Piece('white', 'bishop', [168, 588], whiteBishopImg, False, False, None, [], [])
        whiteBishop2 = Piece('white', 'bishop', [420, 588], whiteBishopImg, False, False, None, [], [])

        win.blit(whiteBishopImg, whiteBishop1.position)
        win.blit(whiteBishopImg, whiteBishop2.position)

        whiteQueen = Piece('white', 'queen', [252, 588], whiteQueenImg, False, False, None, [], [])
        whiteKing = King('white', 'king', [336, 588], whiteKingImg, False, False, None, [], [], False)

        win.blit(whiteQueenImg, whiteQueen.position)
        win.blit(whiteKingImg, whiteKing.position)

        whiteList = [whitePawn1, whitePawn2, whitePawn3, whitePawn4, whitePawn5,
                     whitePawn6, whitePawn7, whitePawn8, whiteRook1, whiteRook2,
                     whiteKnight1, whiteKnight2, whiteBishop1, whiteBishop2, whiteQueen,
                     whiteKing]

        pygame.display.update()

        return [whiteList, blackList]

    def flipBoard():
        for x in whiteList:
            x.position[1] = 588 - x.position[1]
        for x in blackList:
            x.position[1] = 588 - x.position[1]

    resetBoard()

    def redrawBoard():
        win.blit(chessBoard, (0, 0))
        friendlyList = []
        enemyList = []
        if turn == 'white':
            friendlyList = whiteList
            enemyList = blackList
        else:
            friendlyList = blackList
            enemyList = whiteList
        for x in friendlyList:
            if x.isSelected:
                pygame.draw.rect(win, Color(222, 218, 9), Rect(x.position[0], x.position[1], 84, 84))
                for y in x.possibleMoves:
                    pygame.draw.rect(win, Color(172, 172, 172), Rect(y[0] + 2, y[1] + 2, 80, 80))
            win.blit(x.img, (x.position[0], x.position[1]))

        for x in enemyList:
            if x.isSelected:
                pygame.draw.rect(win, Color(222, 218, 9), Rect(x.position[0], x.position[1], 84, 84))
                for y in x.possibleMoves:
                    pygame.draw.rect(win, Color(172, 172, 172), Rect(y[0] + 2, y[1] + 2, 80, 80))
            win.blit(x.img, (x.position[0], x.position[1]))
        pygame.display.update()

    while True:
        for event_var in pygame.event.get():
            if event_var.type == QUIT:
                pygame.quit()
                return

            elif event_var.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                friendlyList = []
                enemyList = []
                if turn == "white":
                    friendlyList = whiteList
                    enemyList = blackList
                else:
                    friendlyList = blackList
                    enemyList = whiteList

                for piece in friendlyList:
                    if piece.position[0] < mousePos[0] < piece.position[0] + 84 and piece.position[1] < mousePos[1] < piece.position[1] + 84:
                        for x in friendlyList:
                            x.isSelected = False
                        piece.isSelected = True
                        redrawBoard()
                    elif piece.isSelected:
                        previousPosition = []
                        for x in piece.possibleMoves:
                            if x[0] < mousePos[0] < x[0] + 84 and x[1] < mousePos[1] < x[1] + 84:
                                for y in enemyList:
                                    if y.position == x:
                                        x = y.position
                                        y.position = [-84, -84]
                                        enemyList.remove(y)
                                        break
                                    elif piece.name == 'pawn' and y.name == 'pawn' and y.doubleMoveLastTurn and (piece.position[0] - 84 == y.position[0] or piece.position[0] + 84) and piece.position[1] == y.position[1]:
                                        previousPosition = piece.position
                                        piece.position = x
                                        y.position = [-84, -84]
                                        enemyList.remove(y)
                                if piece.position != x:
                                    previousPosition = piece.position
                                    piece.position = x
                                piece.isSelected = False

                                if piece.name == 'rook':
                                    piece.hasMoved = True

                                if piece.name == 'king':
                                    piece.hasMoved = True
                                    rook1 = blackRook1
                                    rook2 = blackRook2
                                    if piece.color == 'white':
                                        rook1 = whiteRook1
                                        rook2 = whiteRook2

                                    if previousPosition[0] == piece.position[0] + 168 and rook1.position[0] == piece.position[0] - 168:
                                        rook1.position[0] = piece.position[0] + 84
                                    elif previousPosition[0] == piece.position[0] - 168 and rook2.position[0] == piece.position[0] + 84:
                                        rook2.position[0] = piece.position[0] - 84

                                if boardFlip: flipBoard()
                                for y in friendlyList:
                                    if (y.position[1] == 0 or y.position[1] == 588) and y.name == 'pawn':
                                        pawnConversion(y)
                                    getPossibleMoves(y)

                                if (piece.position[1] - 168 == previousPosition[1] or piece.position[1] + 168 == previousPosition[1]) and piece.name == 'pawn':
                                    piece.doubleMoveLastTurn = True

                                for y in enemyList:
                                    getPossibleMoves(y)

                                turnCount += 1
                                askForReset = checkForEndgame()
                                turn = enemyList[0].color
                                redrawBoard()
                                if askForReset:
                                    while True:
                                        response = input(
                                            "Would you like to reset the board? 'Yes' or 'no'\n").casefold()
                                        if response == 'yes' or response == 'y':
                                            turn = 'white'
                                            turnCount = 1
                                            listHolder = resetBoard()
                                            whiteList = listHolder[0]
                                            blackList = listHolder[1]
                                            for x in whiteList:
                                                getPossibleMoves(x)

                                            for x in blackList:
                                                getPossibleMoves(x)
                                            break
                                        elif response == 'no' or response == 'n':
                                            break
                                        else:
                                            print('Invalid Input. Please try again.')


main()
