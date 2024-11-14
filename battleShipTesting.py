# import battleShip as ship

# board = ship.createBoard(3)
# ship.addShip(board,5)
# print(ship.checkSetUpError(3,3)) #returns False
# print(ship.checkSetUpError(4,10)) #returns False
# print(ship.checkSetUpError(5,28)) #returns True
# print(ship.checkSetUpError(3,10)) #returns True

# ship.displayBoard(board,round=False)

# #returns True if hit and False if miss
# # print(ship.fireShot(board,1,1)) 
# # print(ship.fireShot(board,2,2))
# # print(ship.fireShot(board,3,3))
# print(ship.checkFireError(board,1,1)) #returns False
# print(ship.checkFireError(board,1,4)) #returns True
# print(ship.checkFireError(board,-1,3)) #returns True

# print(ship.fireShot(board,2,2)) 
# print(ship.checkFireError(board,2,2)) #SHOULD return True

# ship.displayBoard(board)

# ship.playRound(board,5)