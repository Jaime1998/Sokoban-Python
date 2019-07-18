#!/usr/bin/python
# -*- coding: utf-8 -*-




class State():
    
    #player coordintate (#,#)

    #boxes list of coordintates into a dict ((#,#):# , (#,#):#, ...)
    #storages list of coordintates into a dict ((#,#):#, (#,#):#, ...)
    #obstacles list of coordintates ((#,#), (#,#), ...)
    def __init__(self, player, boxes):
        
        self.player = player
        self.boxes = boxes
        
    
    def __hash__(self):
        return hash(self.player, self.boxes)
    
    def possibleMoves(self, storages, obstacles):
        possibleMoves = []
        #move into up, right, down and left
        for directions in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newPlayerPos = (self.player[0]+directions[0], self.player[1]+directions[1])
            if (newPlayerPos in obstacles):
                continue
            
            newBoxesPos = dict(self.boxes)
            if (newPlayerPos in self.boxes):
                newBoxPos = (newPlayerPos[0]+directions[0], newPlayerPos[1]+directions[1])
                if(newBoxPos in obstacles):
                    continue
                if(newBoxPos in self.boxes):
                    continue
                #Get the index of the coordinate of box and remove from de dictionary
                i = newBoxesPos.pop(newPlayerPos)
                #Add to the dictionary the coordinate and asociate again with the same index
                #As result we actualizate the pos, removing and adding at the same index
                newBoxesPos[newBoxPos] = i
            
            newState = State(newPlayerPos, newBoxesPos)
            print ('Las cajas están en: ')
            print (newState.boxes)
            print ('El jugador está en: ')
            print (newState.player)
            possibleMoves.append(newState)
                

def goalState(stateIn, storages):
    for box in stateIn.boxes:
        if box not in storages:
            return False
    return True


obstacles = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,4), (1,5), (2,0), (2,5), (3,0), (3,5), (4,0), (4,5), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]
storages = {(2,1): 0, (2,3):1}
stateObj = State((1,2), {(2,2):0, (2,3):1})
stateObj.possibleMoves(storages, obstacles)
    



