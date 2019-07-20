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
        return possibleMoves

    #return True if is a deadlock, False in otherwise
    def isDeadLock(storagesIn, obstaclesIn):
        for coordinateBox in self.box:
            if coordinateBox in storagesIn:
                continue
            else:
                
                l = tuple(map(int.__add__, coordinateBox, (0,-1)))
                r = tuple(map(int.__add__, coordinateBox, (0,1)))
                up = tuple(map(int.__add__, coordinateBox, (-1,0)))
                bot = tuple(map(int.__add__, coordinateBox, (1,0)))

                #diagonals
                #up and right
                dur = tuple(map(int.__add__, coordinateBox, (-1,1)))
                #up and left
                dul = tuple(map(int.__add__, coordinateBox, (-1,-1)))
                #bot and right
                dbr = tuple(map(int.__add__, coordinateBox, (1,1)))
                #bot and left
                dbl = tuple(map(int.__add__, coordinateBox, (1,-1)))

                #################################
                #            box  w
                #             w  any
                if (r in obstaclesIn) and (bot in obstaclesIn):
                    return True

                #################################
                #             w  box
                #            any  w
                if (l in obstaclesIn) and (bot in obstaclesIn):
                    return True
                
                #################################
                #            any  w
                #             w  box
                if (l in obstaclesIn) and (up in obstaclesIn):
                    return True
                
                #################################
                #             w  any
                #            box  w
                if (r in obstaclesIn) and (up in obstaclesIn:):
                    return True
                

                #################################
                # Type of deadblock, right place
                #            box  box/w
                #           box/w box/w
                if (r in obstaclesIn) or (r in self.boxes):
                    if (bot in obstaclesIn) or (bot in self.boxes):
                        if (dbr in obstaclesIn) or (dbr in self.boxes):
                            return True
                    if (up in obstaclesIn) or (up in self.boxes):
                        if (dur in obstaclesIn) or (dur in self.boxes):
                            return True
                #################################
                # Type of deadblock, left place
                #           box/w  box
                #           box/w box/w
                if (l in obstaclesIn) or (l in self.boxes):
                    if (bot in obstaclesIn) or (bot in self.boxes):
                        if (dbl in obstaclesIn) or (dbl in self.boxes):
                            return True
                    if (up in obstaclesIn) or (up in self.boxes):
                        if (dul in obstaclesIn) or (dul in self.boxes):
                            return True
        rerturn False        

    def isGoalState(storagesIn):
        for box in self.boxes:
            if box not in storagesIn:
                return False
        return True

class Node():

    def __init__(self, player, boxes, movement, parent):
        self.stateNode = State(player, boxes)
        self.movement = movement
        self.parent = parent
    
    




"""
obstacles = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,4), (1,5), (2,0), (2,5), (3,0), (3,5), (4,0), (4,5), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]
storages = {(2,1): 0, (2,3):1}
stateObj = State((1,2), {(2,2):0, (2,3):1})
stateObj.possibleMoves(storages, obstacles)"""
    



