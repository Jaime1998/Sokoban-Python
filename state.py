#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Integrantes:
Jaime Cuartas Granada-1632664
Emily Esmeralda Carvajal Camelo-1630436
Luis David Restrepo Hoyos-1427086
'''

class State():
    
    #player coordintate (#,#)

    #boxes list of coordintates into a dict ((#,#):# , (#,#):#, ...)
    #movement (0,1) or (1,0) or (0,-1) or (-1,0)
    
    def __init__(self, player, boxes, movement):
        self.player = player
        self.boxes = boxes
        self.movement = movement
        
    
    def __eq__(self, otherState):
        return self.player == otherState.player and self.boxes == otherState.boxes

    def __hash__(self):
        return hash((self.player, tuple(self.boxes )))
    
    def possibleMoves(self, storages, obstacles):
        possibleMoves = []
        #move into up, down, rigth and left
        for directions in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            newPlayerPos = (self.player[0]+directions[0], self.player[1]+directions[1])
            if (newPlayerPos in obstacles):
                continue

            #self.boxes is a dict
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
            
            newState = State(newPlayerPos, newBoxesPos, directions)
            
            possibleMoves.append(newState)
        return possibleMoves

    #return True if is a deadlock, False in otherwise
    def isDeadLock(self, storagesIn, obstaclesIn):
        for coordinateBox in self.boxes:
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
                if (r in obstaclesIn) and (up in obstaclesIn):
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
        return False        

    def isGoalState(self, storagesIn):
        for box in self.boxes:
            if box not in storagesIn:
                return False
        return True
    
    def getMap(self, obstaclesIn, storagesIn, highIn, widthIn):
        matrix = [[' ' for col in range(widthIn)] for row in range(highIn)]
        for obstacles in obstaclesIn:
            matrix[obstacles[0]][obstacles[1]] = 'w'
        for storages in storagesIn:
            matrix[storages[0]][storages[1]] = 'x'
        for box in self.boxes:
            matrix[box[0]][box[1]] = 'b'
        matrix[self.player[0]][self.player[1]] = 'I'

        return matrix


class Node():

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    def getPath(self):
        #Return the path of movements takes to this state
        path = [self.state.movement]
        actual = self.parent
        while actual:
            path.append(actual.state.movement)
            actual = actual.parent
        path.reverse()
        return path

    def getMoves(self):
        path = self.getPath()
        nameOfMoves = {(0,0): '', (0,-1): 'L', (1,0): 'D', (0,1): 'R', (-1,0): 'U'}

        formatMoves = ''
        for moves in path:
            formatMoves += nameOfMoves[moves]
        
        return formatMoves

    def getPathMaps(self, obstaclesIn, storagesIn, highIn, widthIn):
        #Return an array of matrixes 
        pathOfStates=[self.state.getMap(obstaclesIn, storagesIn, highIn, widthIn)]
        
        actual = self.parent
        while actual:
            pathOfStates.append(actual.state.getMap(obstaclesIn, storagesIn, highIn, widthIn))
            actual = actual.parent
        pathOfStates.reverse()
        return pathOfStates

    def isParent(self):
        #Return True if we look a state iqual on this path
        
        last = self.parent
        actual = self.state
        while last:
            if (last.state.boxes == actual.boxes) and (last.state.player == actual.player):
                return True
            last = last.parent
        return False
    
   
class NodeDepth(Node):
    def __init__(self, state, parent, depth):
        Node.__init__(self, state, parent)
        self.depth = depth




    


