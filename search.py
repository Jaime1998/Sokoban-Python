#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Integrantes:
Jaime Cuartas Granada-1632664
Emily Esmeralda Carvajal Camelo-1630436
Luis David Restrepo Hoyos-1427086
'''

from state import *
from collections import deque

#Depth-First Search
def DFS(stateObj, obstacles, storages):
    #Start a node with the state given and no parent
    startNode = Node (stateObj, None)
    #Add the node to a queue
    tree = deque([startNode])
    
    #https://wiki.python.org/moin/TimeComplexity
    #Make taboo the states that i have already reviewed, maybe for anothers paths
    #Pick set for complexity O(1) on average case for operation x E taboo (E: Pertenece)
    taboo = set()
    
    while tree :
        #Get the last node added and maked taboo in the future
        currentNode = tree.pop()
        taboo.add(currentNode.state)
        #Check if we get a sate irresolvable then we ignore that node and continue
        if currentNode.state.isDeadLock(storages, obstacles):
            continue
        else:
            #Check if we get a goal state
            if(currentNode.state.isGoalState(storages)):
                return currentNode
            #Get the possible moves to generate new child nodes and turn reverse to push later sin order to check UDRL
            validMovesStates = currentNode.state.possibleMoves(storages, obstacles)
            validMovesStates.reverse()
            #Create a new node for each move and add to the tree if there is no a taboo state
            for childState in validMovesStates:
                childNode = Node(childState, currentNode)
                if childNode.state in taboo:
                    continue
                else:
                    tree.append(childNode)

    return None

#Breadth-First Search
def BFS(stateObj, obstacles, storages):
    #Start a node with the state given and no parent
    startNode = Node (stateObj, None)
    #Add the node to a queue
    tree = deque([startNode])
    
    #https://wiki.python.org/moin/TimeComplexity
    #Make taboo the states that i have already reviewed, maybe for anothers paths
    #Pick set for complexity O(1) on average case for operation x E taboo (E: Pertenece)
    taboo = set()
    
    while tree :
        #Get the first node added and maked taboo in the future
        currentNode = tree.popleft()
        taboo.add(currentNode.state)
        #Check if we get a sate irresolvable then we ignore that node and continue
        if currentNode.state.isDeadLock(storages, obstacles):
            continue
        else:
            #Check if we get a goal state
            if(currentNode.state.isGoalState(storages)):
                return currentNode
            #Get the possible moves to generate new child nodes
            validMovesStates = currentNode.state.possibleMoves(storages, obstacles)
            #Create a new node for each move and add to the tree if there is no a taboo state
            for childState in validMovesStates:
                childNode = Node(childState, currentNode)
                if childNode.state in taboo:
                    continue
                else:
                    tree.append(childNode)

    return None

#Iterative deepening Depth-first search
def IDS(stateObj, obstacles, storages, limit=10, increase=3):
    #Start a node with the state given, no parent and a depth 0
    startNode = NodeDepth (stateObj, None, 0)
    #Create a queue to save the nodes that represent the limit of the tree
    limitTree = deque([startNode])
    
    #https://wiki.python.org/moin/TimeComplexity
    #Make taboo the states that i have already reviewed, maybe for anothers paths
    #Pick set for complexity O(1) on average case for operation x E taboo (E: Pertenece)
    taboo = set()
    limit = limit - increase
    while limitTree:
        #The limits of the tree are the tree that we are going to expand
        tree = limitTree.copy()
        #Make the limit empty
        limitTree = deque()
        #increase the search limit
        limit = limit + increase
        while tree :
            #Get the last node added and maked taboo in the future
            currentNode = tree.pop()
            taboo.add(currentNode.state)
            #Check if we get a sate irresolvable then we ignore that node and continue
            if currentNode.state.isDeadLock(storages, obstacles):
                continue
            
            else:
                #Check if the depth of the node is on the limit
                #in that case we added this node to the limit deque
                if(currentNode.depth >= limit):
                    limitTree.append(currentNode)
                    continue
                #Check if we get a goal state
                if(currentNode.state.isGoalState(storages)):
                    return currentNode
                #Get the possible moves to generate new child nodes
                validMovesStates = currentNode.state.possibleMoves(storages, obstacles)
                validMovesStates.reverse()
                #Create a new node for each move and add to the tree if there is no a taboo state
                for childState in validMovesStates:
                    childNode = NodeDepth(childState, currentNode, currentNode.depth+1)
                    #if childNode.isParent() and (childNode.state in explored):
                    if childNode.state in taboo:
                        continue
                    else:
                        tree.append(childNode)
                        #taboo.add(childNode.state)



def printMap(matrix):
    high = len(matrix[0])
    width = len(matrix[0][0])
    for i in range(len(matrix)):
        for j in range(high):
            for k in range(width):
                print (matrix[i][j][k], end='')
            print ()
        print()


def readBoard(lines, obstacles, storages, stateObj):
    agent = ()
    boxes = {}
    numline = 0
    numstorages= 0
    flag = True
    for line in lines:
        if line == "\n":
            break
        if line[0] == "W" or line[0] == "0":
            width = len(line)
            for i in range(0,len(line)):
                if line[i] == "W":
                    obstacles.append((numline,i))
                else :
                    if line[i] == "X":
                        storages[(numline,i)] = numstorages
                        numstorages = numstorages + 1
            numline = numline +1
        else:
            if flag:
                high = numline
                coords = line[0:len(line)].split(",")
                agent = (int(coords[0]),int(coords[1]))
                numstorages = 0
                flag = False
            else:
                coords = line[0:len(line)].split(",")
                boxes[(int(coords[0]),int(coords[1]))] = numstorages
                numstorages = numstorages + 1
            stateObj = State(agent,boxes,(0,0))
            numline = numline + 1
    stateObj = State(agent,boxes,(0,0))
    return obstacles, storages, stateObj, high, width

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped:
            break
        lines.append(stripped)
    
    if lines:
            
        #obstacles: list of coordintates ((#,#), (#,#), ...)
        #storages: list of coordintates into a dict ((#,#):#, (#,#):#, ...)
            
        obstacles = []
        storages = {}

        #player: coordintate (#,#)
        #boxes: list of coordintates into a dict ((#,#):# , (#,#):#, ...)
        #movement: (0,1) or (1,0) or (0,-1) or (-1,0)
        #state: Object (player, boxes, movement)
        stateObj = None
        obstacles, storages, state, high, width = readBoard(lines, obstacles, storages, stateObj)
        
        result = BFS(state, obstacles, storages)
        
        if (result):
            #printMap (result.getPathMaps(obstacles, storages, high, width))
            print (result.getMoves())
        else:
            print ('No fue posible solucionar el mapa')
        
        result = DFS(state, obstacles, storages)
        
        if (result):
            #printMap (result.getPathMaps(obstacles, storages, high, width))
            print (result.getMoves())
        else:
            print ('No fue posible solucionar el mapa')
        
        result = IDS(state, obstacles, storages)
        

        if (result):
            #printMap (result.getPathMaps(obstacles, storages, high, width))
            print (result.getMoves())
        else:
            print ('No fue posible solucionar el mapa')
    