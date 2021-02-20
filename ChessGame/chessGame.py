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
    boardFlip = True
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

    # Below is the largest function in the entire program(so far).
    # Calculates all the possible moves for a given piece and adds them
    # to the piece's list of possible moves.
    # The moves are calculated from the perspective of the piece,
    # so the 'friends' and 'enemies' parameters
    # help clarify who's doing what.
    # There are different move checking procedures for each piece.
    def getPossibleMoves(piece, friends, enemies):
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

        friendlyList = friends
        enemyList = enemies

        if friends[0].color == "white":
            friendlyKing = whiteKing
            enemyKing = blackKing
        else:
            friendlyKing = blackKing
            enemyKing = whiteKing

        piece.possibleMoves = []
        piece.isDefending = []

        piece.isChecking = False

        if piece.name == 'pawn':
            piece.doubleMoveLastTurn = False
            blockingSingleMove = False
            blockingDoubleMove = False
            offSetNum = -84
            if piece.color == 'black':
                offSetNum = 84
            for x in enemyList:
                # If an enemy piece is in front of the pawn and on a
                # diagonal(to the left or right of the square directly in front of the pawn),
                # add the enemies position to the pawn's possible move list.
                if (x.position[0] == piece.position[0] - 84 or x.position[0] == piece.position[0] + 84) and x.position[1] == piece.position[1] + offSetNum:
                    piece.possibleMoves.append(x.position)
                    # If that enemy is a king, the pawn is checking the king.
                    if x.name == 'king':
                        piece.isChecking = True
                # If an enemy piece is on the square directly in front of the pawn,
                # the pawn is prevented from moving to that square.
                if x.position == [piece.position[0], piece.position[1] + offSetNum]:
                    blockingSingleMove = True
                # If an enemy piece is two squares directly in front of the pawn,
                # the pawn is prevented from moving to that square.
                if x.position == [piece.position[0], piece.position[1] + offSetNum * 2]:
                    blockingDoubleMove = True
                # If the enemy piece in question is a pawn that moved two squares last turn,
                # and is directly to the left or right of this piece, add the square behind the enemy pawn to this
                # piece's possible move list(en pessant).
                if x.position[1] == piece.position[1] and (x.position[0] == piece.position[0] - 84 or x.position[0] == piece.position[0] + 84):
                    if x.name == 'pawn' and x.doubleMoveLastTurn:
                        piece.possibleMoves.append([x.position[0], x.position[1] + offSetNum])

            # Checks to see if a friendly piece is blocking this pawn's movement.
            for x in friendlyList:
                if x.position == [piece.position[0], piece.position[1] + offSetNum]:
                    blockingSingleMove = True
                if x.position == [piece.position[0], piece.position[1] + offSetNum * 2]:
                    blockingDoubleMove = True

            # If the piece has not reached the edge of the board, add the square directly in front to its possible
            # moves.
            if 0 < piece.position[1] < 588 and not blockingSingleMove:
                piece.possibleMoves.append([piece.position[0], piece.position[1] + offSetNum])

            # If the piece has not moved from its starting position and the square two squares ahead is clear,
            # add that square to its possible moves.
            if (piece.position[1] == 504 or piece.position[1] == 84) and (not blockingSingleMove and not blockingDoubleMove):
                piece.possibleMoves.append([piece.position[0], piece.position[1] + (offSetNum * 2)])

            # Add the pawn's capturing squares(squares where it can capture) to its list of defended squares.
            piece.isDefending.append([piece.position[0] - 84, piece.position[1] + offSetNum])
            piece.isDefending.append([piece.position[0] + 84, piece.position[1] + offSetNum])

        # This function handles move checking behavior for pieces that can move like the rook.
        def verticalHorizontalMoveChecking():
            closestPieceUp = None
            closestPieceDown = None
            closestPieceLeft = None
            closestPieceRight = None
            # The loop below finds the closest pieces to this piece.
            # If the piece is an allied piece it is added to this piece's defended list.
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

            # The code below checks to see if this piece is pinning a piece(a piece that prevents the enemy king from
            # being put in check and is unable to move as a result).
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
            # The if statements below add all the squares to this piece's possible move list where it should be able to
            # move. It does this by adding all squares including and before the closest pieces that are directly
            # up, left, right, and down, respective to the piece. If one of those pieces is the king, it is in check.
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
                        piece.isChecking = True
            else:
                xPosition = piece.position[0] + 84
                while xPosition <= 588:
                    piece.possibleMoves.append([xPosition, piece.position[1]])
                    xPosition += 84

        # The function defined above is able to calculate a rook's every possible move
        # so it is called if this piece is a rook.
        if piece.name == 'rook':
            verticalHorizontalMoveChecking()
            for x in piece.possibleMoves:
                piece.isDefending.append(x)

        # The code below just adds every possible movement a knight could make to this piece's possible move list.
        # We don't have to worry about these moves being out of bounds, because these moves will be removed later.
        # The noted code below used to do out of bounds checking, though it currently isn't necessary.
        if piece.name == 'knight':
            piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] - (84 * 2)])
            piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] - (84 * 2)])
            piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] + (84 * 2)])
            piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] + (84 * 2)])
            piece.possibleMoves.append([piece.position[0] - (84 * 2), piece.position[1] - 84])
            piece.possibleMoves.append([piece.position[0] - (84 * 2), piece.position[1] + 84])
            piece.possibleMoves.append([piece.position[0] + (84 * 2), piece.position[1] - 84])
            piece.possibleMoves.append([piece.position[0] + (84 * 2), piece.position[1] + 84])
            # if piece.position[1] >= 168:
            #     if piece.position[0] > 0:
            #         piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] - (84 * 2)])
            #     if piece.position[0] < 588:
            #         piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] - (84 * 2)])
            # if piece.position[1] <= 420:
            #     if piece.position[0] > 0:
            #         piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] + (84 * 2)])
            #     if piece.position[0] < 588:
            #         piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] + (84 * 2)])
            # if piece.position[0] >= 168:
            #     if piece.position[1] > 0:
            #         piece.possibleMoves.append([piece.position[0] - (84 * 2), piece.position[1] - 84])
            #     if piece.position[1] < 588:
            #         piece.possibleMoves.append([piece.position[0] - (84 * 2), piece.position[1] + 84])
            # if piece.position[0] <= 420:
            #     if piece.position[1] > 0:
            #         piece.possibleMoves.append([piece.position[0] + (84 * 2), piece.position[1] - 84])
            #     if piece.position[1] < 588:
            #         piece.possibleMoves.append([piece.position[0] + (84 * 2), piece.position[1] + 84])

            # Add's this piece's possible moves to its list of defended squares and removes possible moves that overlap
            # with friendly pieces.
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

        # This function is responsible for finding possible moves for pieces that can move like a bishop.
        # Similarly to the last function, it also looks for any pinned pieces.
        def diagonolMoveChecking():
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

        # Uses the function above to get possible moves for bishops.
        if piece.name == 'bishop':
            diagonolMoveChecking()
            for x in piece.possibleMoves:
                piece.isDefending.append(x)

        # Movement behavior for the queen is just a combination of the last two functions.
        if piece.name == 'queen':
            verticalHorizontalMoveChecking()
            for x in piece.possibleMoves:
                piece.isDefending.append(x)
            diagonolMoveChecking()
            for x in piece.possibleMoves:
                piece.isDefending.append(x)

        # The king has some tricky behavior to check.
        # For example: not being able to move onto squares where it would be in danger
        # or castling.
        if piece.name == 'king':
            piece.possibleMoves.append([piece.position[0] - 84, piece.position[1]])
            piece.possibleMoves.append([piece.position[0] + 84, piece.position[1]])
            piece.possibleMoves.append([piece.position[0], piece.position[1] - 84])
            piece.possibleMoves.append([piece.position[0], piece.position[1] + 84])
            piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] - 84])
            piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] - 84])
            piece.possibleMoves.append([piece.position[0] - 84, piece.position[1] + 84])
            piece.possibleMoves.append([piece.position[0] + 84, piece.position[1] + 84])
            for move in piece.possibleMoves:
                piece.isDefending.append(move)

            if not piece.hasMoved:
                yPosition = 0
                rook1 = blackRook1
                rook2 = blackRook2
                if piece.color == 'white':
                    yPosition = 588
                    rook1 = whiteRook1
                    rook2 = whiteRook2

                # The code below checks to see if another piece is preventing the king from castling(on either side).
                if not rook1.hasMoved:
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
                if not rook2.hasMoved:
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
                        removeList.append(x)
                        break

            # Removes any squares that an enemy piece is defending from the king's possible moves,
            # this prevents the king from putting itself in danger.
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

        # The code below checks to see if the piece is pinned, it's movement is restricted accordingly
        # (depending on the piece that has it pinned).
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

        # The code below removes any moves from each pieces list of possible moves that are out of bounds.
        # The canRemove boolean serves as a safeguard to ensure that the move being removed
        # is actually in the pieces move list.
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

    # The two loops below gives pieces their possible starting moves
    for x in whiteList:
        getPossibleMoves(x, whiteList, blackList)

    for x in blackList:
        getPossibleMoves(x, blackList, whiteList)

    # This function transforms a pawn into any requested piece.
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

    # This function checks to see if the game is over.
    # If a player has no moves, they've either tied or lost
    # depending on if they are in check or not.
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

        if whiteNoMoves and turn == 'white':
            for piece in blackList:
                if piece.isChecking:
                    whiteInCheck = True
            if whiteInCheck:
                print("Checkmate! Black Wins!")
                return True
            else:
                print("Stalemate! Nobody Wins!")
                return True

        if blackNoMoves and turn == 'black':
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

    # Creates a new set of pieces and lists containing those pieces. Also updates the game window.
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

    resetBoard()

    # The function below draws and displays every image on the window.
    # If a piece is selected, its possible moves become highlighted in gray.
    # Afterwards, the code draws each piece onto the screen.
    # The flip boolean draws each piece rotated 180 degrees.
    # If flip is false, it doesnt rotate at all(rotates 0 degrees).
    def redrawBoard(flip = False):
        win.blit(chessBoard, (0, 0))
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
            win.blit(pygame.transform.rotate(x.img, 180 * flip), (x.position[0], x.position[1]))

        for x in enemyList:
            win.blit(pygame.transform.rotate(x.img, 180 * flip), (x.position[0], x.position[1]))
        if flip:
            win.blit(pygame.transform.rotate(win, 180), (0, 0))
        pygame.display.update()
        return flip

    # Main game loop.
    while True:
        for event_var in pygame.event.get():
            # Terminates the program and closes the game window when the red X is clicked.
            if event_var.type == QUIT:
                pygame.quit()
                return
            # This code block will perform a variety of tasks depending on where a user clicks.
            elif event_var.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if turn == "white":
                    friendlyList = whiteList
                    enemyList = blackList
                else:
                    friendlyList = blackList
                    enemyList = whiteList
                flipped = boardFlip and turn == 'black'
                # add_flip_offset will evaluate to 0 if the board is not flipped and 588 if the board is flipped.
                # mult_flip_offset will evaluate to 1 if the board is flipped and -1 if the board is flipped
                add_flip_offset = 588 * flipped
                mult_flip_offset = (-1 * (not flipped)) + (1 * flipped)
                for piece in friendlyList:
                    if piece.isSelected:
                        previousPosition = []
                        # The code below checks whether or not the mouse clicked on a possible move.
                        # If the display of the board is flipped, add_flip_offset and mult_flip_offset allows the code to check a flipped version of the move.
                        # This is necessary because flipping the display of the board does not change the numerical position of the pieces.
                        for x in piece.possibleMoves:
                            # if the player clicked on one of the possible moves for a selected piece...
                            if add_flip_offset - x[0] * mult_flip_offset < mousePos[0] < (add_flip_offset - x[0] + (84 * mult_flip_offset)) * mult_flip_offset and add_flip_offset - x[1] * mult_flip_offset < mousePos[1] < (add_flip_offset - x[1] + (84 * mult_flip_offset)) * mult_flip_offset:
                                turnCount += 1
                                turn = enemyList[0].color
                                # This for loop checks if an enemy piece should be taken after a move.
                                for y in enemyList:
                                    # Remove any enemy piece that was on the same square as the selected move
                                    if y.position == x:
                                        x = y.position
                                        y.position = [-84, -84]
                                        enemyList.remove(y)
                                        break
                                    # Remove an enemy pawn if it was attacked by an en passant
                                    elif piece.name == 'pawn' and y.name == 'pawn' and y.doubleMoveLastTurn and (piece.position[0] - 84 == y.position[0] or piece.position[0] + 84 == y.position[0]) and piece.position[1] == y.position[1]:
                                        previousPosition = piece.position
                                        piece.position = x
                                        y.position = [-84, -84]
                                        enemyList.remove(y)
                                # If no enemy piece was taken, move the selected piece to the requested open square.
                                if piece.position != x:
                                    previousPosition = piece.position
                                    piece.position = x
                                piece.isSelected = False

                                if piece.name == 'rook':
                                    piece.hasMoved = True

                                # The code block below checks to see if the possible move was a castle.
                                # The pieces are moved accordingly.
                                if piece.name == 'king':
                                    piece.hasMoved = True
                                    rook1 = blackRook1
                                    rook2 = blackRook2
                                    if piece.color == 'white':
                                        rook1 = whiteRook1
                                        rook2 = whiteRook2

                                    # When castling in chess, the king moves two squares to the right or left.
                                    # The code checks to see if the king moved two squares to the right or left.
                                    # It also checks to see if the respective rooks are in the right positions.
                                    if previousPosition[0] == piece.position[0] + 168 and rook1.position[0] == piece.position[0] - 168:
                                        rook1.position[0] = piece.position[0] + 84
                                    elif previousPosition[0] == piece.position[0] - 168 and rook2.position[0] == piece.position[0] + 84:
                                        rook2.position[0] = piece.position[0] - 84

                                # If a pawn reaches the end of the board,
                                # convert the pawn into a desired piece
                                for y in friendlyList:
                                    if (y.position[1] == 0 or y.position[1] == 588) and y.name == 'pawn':
                                        pawnConversion(y)
                                    getPossibleMoves(y, friendlyList, enemyList)

                                # Check to see if the player moved a pawn two squares forward.
                                if (piece.position[1] - 168 == previousPosition[1] or piece.position[1] + 168 == previousPosition[1]) and piece.name == 'pawn':
                                    piece.doubleMoveLastTurn = True

                                # Get the possible moves for the the other player now that a piece has moved.
                                for y in enemyList:
                                    getPossibleMoves(y, enemyList, friendlyList)

                                # redraw the board to display new changes to piece positions.
                                redrawBoard(turn == 'black' and boardFlip)
                                print("Turn {}: {}".format(turnCount, turn))
                                askForReset = checkForEndgame()
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
                                                getPossibleMoves(x, whiteList, blackList)

                                            for x in blackList:
                                                getPossibleMoves(x, blackList, whiteList)
                                            break
                                        elif response == 'no' or response == 'n':
                                            break
                                        else:
                                            print('Invalid Input. Please try again.')
                    # The code below checks if a piece was clicked
                    elif add_flip_offset - piece.position[0] * mult_flip_offset < mousePos[0] < (add_flip_offset - piece.position[0] + (84 * mult_flip_offset)) * mult_flip_offset and add_flip_offset - piece.position[1] * mult_flip_offset < mousePos[1] < (add_flip_offset - piece.position[1] + (84 * mult_flip_offset)) * mult_flip_offset:
                        for x in friendlyList:
                            x.isSelected = False
                        piece.isSelected = True
                        redrawBoard(turn == 'black' and boardFlip)


print("Turn 1: white")  # //TODO Edit placement after creating a main menu screen.
main()
