# GameEngine Interface

# The gameEngine class holds the game state
# Call methods on an GameEngine object to change the game state

# methods
#  .placeStone(place)
#  .rotateStone(place, initial_place)
#  .flyingStone(place, initial_place)
#
#
# Varibles
#  .player_one_turn   - True if it is player ones turn
#  .stones_left_player_one
#  .stones_left_player_two
#  .player_one_phase  - placing stone = 1, rotating = 2, flying = 3
#  .player_two_phase  - placing stone = 1, rotating = 2, flying = 3

class GameEngine:
    player1_is_ai = False
    player2_is_ai = False
    is_game_done = ''
    nr_turns = 0
    timer = 0
    player_one_turn = True
    player_two_turn = False
    stones_left_player_one = 9
    stones_left_player_two = 9
    player_one_phase = 1 #placing stone 1, rotating 2, flying 3
    player_two_phase = 1 #placing stone 1, rotating 2, flying 3
    adjecent_list = [[1,9],[0,4,2],[1,14],[10,4],[1,3,7,5],
                     [4,13],[11,7],[4,6,8],[7,12],[0,21,10],
                     [3,9,11,18],[6,10,15],[8,13,17],[5,12,14,20],[2,13,23],
                     [11,16],[15,19,17],[12,16],[10,19],[16,18,20,22],
                     [13,19],[9,22],[19,21,23],[22,14]]


    possible_mills = [[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23],
                        [0,9,21],[3,10,18],[6,11,15],[1,4,7],[16,19,22],[8,12,17],[5,13,20],[2,14,23]]

    board = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',]


    def __init__(self, player1_is_ai, player2_is_ai):
        self.player1_is_ai = player1_is_ai
        self.player2_is_ai = player2_is_ai

        print("Created Game object")

    def getCurrentPlayerChar(self):
        if (self.player_one_turn):
            return 'X'
        else:
            return 'O'
    def getOpponentPlayerChar(self):
        if (self.player_one_turn):
            return 'O'
        else:
            return 'X'

    def countStones(self):
        char = self.getCurrentPlayerChar()
        counter = 0
        for i in self.board:
            if(i == char):
                counter += 1

        print("PRINT CURRENT STONES FOR"+char+":" + str(counter))
        return counter

    def checkIfMill(self,place):
        char = self.getCurrentPlayerChar()
        for mill in self.possible_mills:
            if place in mill:
                counter = 0
                for stone in mill:
                    if(self.board[stone] == char):
                        counter += 1

                if counter == 3:
                    return(True)
        return False

    def removeStone(self,place):
        print("removing:" + str(place))

        # Playet two turn --- It's turned
        # remove from player one
        if (self.player_one_turn):
            if(self.board[place] == 'X'):
                self.board[place] = '_'

                if(self.player_one_phase != 1):
                    if(self.countStones() == 3):
                        print("Chaging to phase 3")
                        self.player_one_phase = 3

                    if(self.countStones() < 3):
                        self.is_game_done = 'Player 1 looses'

                return True
        else:

            if(self.board[place] == 'O'):
                self.board[place] = '_'

                if(self.player_two_phase != 1):
                    if(self.countStones() == 3):
                        self.player_two_phase = 3

                    if(self.countStones() < 3):
                        self.is_game_done = 'Player 2 looses'

                return True

        return False

    #step 1 - PLACE
    def placeStone(self, place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
                 return ("not valid move")

        if(self.player_one_turn):
            if self.stones_left_player_one > 0:

                self.board[place] = "X"
                self.stones_left_player_one -= 1
                if self.stones_left_player_one == 0:
                    self.player_one_phase = 2
            else:
                return ("Can't place stone, no stones left")
        else:
            if self.stones_left_player_two > 0:

                self.board[place] = "O"
                self.stones_left_player_two -= 1
                if self.stones_left_player_two == 0:
                    self.player_two_phase = 2
            else:
                return ("no stones left")

        if(self.checkIfMill(place)):
            self.player_one_turn = not self.player_one_turn
            return('mill')
        else:
            self.player_one_turn = not self.player_one_turn
            return('')



    #Step 2 - ROTATE
    def rotateStone(self, place, initial_place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
            return ("not valid move")

        if place not in self.adjecent_list[initial_place]:
            return ("Not a adjecent node")

        if (self.player_one_turn):

            self.board[place] = "X"
            self.board[initial_place] = "_"

        else:

            self.board[place] = "O"
            self.board[initial_place] = "_"

        if(self.checkIfMill(place)):
            self.player_one_turn = not self.player_one_turn
            return('mill')
        else:
            self.player_one_turn = not self.player_one_turn
            return('')

    #Step 3 - Place
    def flyingStone(self, place, initial_place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
                 return ("not valid move")

        if (self.player_one_turn):
            print ("player1")
            self.board[place] = "X"
            self.board[initial_place] = "_"

        else:
            print ("player2")
            self.board[place] = "O"
            self.board[initial_place] = "_"

        if(self.checkIfMill(place)):
            self.player_one_turn = not self.player_one_turn
            return('mill')
        else:
            self.player_one_turn = not self.player_one_turn
            return('')



    def printBoard(self):
        print(self.board[0]+"(00)----------------------"+self.board[1]+"(01)----------------------"+self.board[2]+"(02)")
        print("|                           |                           |")
        print("|       "+self.board[3]+"(03)--------------"+self.board[4]+"(04)--------------"+self.board[5]+"(05)     |")
        print("|       |                   |                    |      |")
        print("|       |                   |                    |      |")
        print("|       |        "+self.board[6]+"(06)-----"+self.board[7]+"(7)-----"+self.board[8]+"(8)         |      |")
        print("|       |         |                   |          |      |")
        print("|       |         |                   |          |      |")
        print(self.board[9]+"(09)---"+self.board[10]+"(10)----"+self.board[11]+"(11)               "+self.board[12]+"(12)----"+self.board[13]+"(13)---"+self.board[14]+"(14)")
        print("|       |         |                   |          |      |")
        print("|       |         |                   |          |      |")
        print("|       |        "+self.board[15]+"(15)-----"+self.board[16]+"(16)-----"+self.board[17]+"(17)       |      |")
        print("|       |                   |                    |      |")
        print("|       |                   |                    |      |")
        print("|       "+self.board[18]+"(18)--------------"+self.board[19]+"(19)--------------"+self.board[20]+"(20)     |")
        print("|                           |                           |")
        print("|                           |                           |")
        print(self.board[21]+"(21)----------------------"+self.board[22]+"(22)----------------------"+self.board[23]+"(23)")
