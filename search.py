#!/usr/bin/python
# -*- coding: utf-8 -*-

from state import *
from collections import deque

#Depth-First Search
def DFS(stateObj, obstacles, storages):
    startNode = Node (stateObj, None)
    stack = deque([startNode])
    taboo = set()

    #https://wiki.python.org/moin/TimeComplexity
    #Make taboo the states that i have already reviewed, maybe for anothers paths
    #Pick set for complexity O(1) on average case for operation x E taboo (E: Pertenece)
    #taboo = set()
    #taboo.add(stateObj)
    
    while stack :
        currentNode = stack.pop()
        taboo.add(currentNode.state)
        if currentNode.state.isDeadLock(storages, obstacles):
            #print (currentNode.state.boxes)
            continue
        
        else:
            if(currentNode.state.isGoalState(storages)):
                return currentNode

            validMovesStates = currentNode.state.possibleMoves(storages, obstacles)

            for childState in validMovesStates:
                childNode = Node(childState, currentNode)
                #if childNode.isParent() and (childNode.state in explored):
                if childNode.state in taboo:
                    continue
                else:
                    stack.append(childNode)

    return None

#Breadth-First Search
def BFS(stateObj, obstacles, storages):
    startNode = Node (stateObj, None)
    stack = deque([startNode])
    taboo = set()

    #https://wiki.python.org/moin/TimeComplexity
    #Make taboo the states that i have already reviewed, maybe for anothers paths
    #Pick set for complexity O(1) on average case for operation x E taboo (E: Pertenece)
    #taboo = set()
    #taboo.add(stateObj)
    
    while stack :
        currentNode = stack.popleft()
        taboo.add(currentNode.state)
        if currentNode.state.isDeadLock(storages, obstacles):
            #print (currentNode.state.boxes)
            continue
        
        else:
            if(currentNode.state.isGoalState(storages)):
                return currentNode

            validMovesStates = currentNode.state.possibleMoves(storages, obstacles)

            for childState in validMovesStates:
                childNode = Node(childState, currentNode)
                #if childNode.isParent() and (childNode.state in explored):
                if childNode.state in taboo:
                    continue
                else:
                    stack.append(childNode)

    return None

#Iterative deepening Depth-first search
def IDS(stateObj, obstacles, storages, limit=10, increase=3):
    startNode = NodeDepth (stateObj, None, 0)
    limitStack = deque([startNode])
    
    #stack = deque([startNode])
    taboo = set()

    #https://wiki.python.org/moin/TimeComplexity
    #Make taboo the states that i have already reviewed, maybe for anothers paths
    #Pick set for complexity O(1) on average case for operation x E taboo (E: Pertenece)
    #taboo = set()
    while limitStack:
        stack = limitStack.copy()
        limitStack = deque()
        limit = limit + increase
        while stack :
            currentNode = stack.pop()
            taboo.add(currentNode.state)
            if currentNode.state.isDeadLock(storages, obstacles):
                continue
            
            else:
                if(currentNode.depth >= limit):
                    limitStack.append(currentNode)
                    continue

                if(currentNode.state.isGoalState(storages)):
                    return currentNode

                validMovesStates = currentNode.state.possibleMoves(storages, obstacles)

                for childState in validMovesStates:
                    
                    childNode = NodeDepth(childState, currentNode, currentNode.depth+1)
                    #if childNode.isParent() and (childNode.state in explored):
                    if childNode.state in taboo:
                        continue
                    else:
                        stack.append(childNode)



def BFSNoTaboo(stateObj, obstacles, storages):
    startNode = Node (stateObj, None)
    stack = deque([startNode])

    #https://wiki.python.org/moin/TimeComplexity
    #Make taboo the states that i have already reviewed, maybe for anothers paths
    #Pick set for complexity O(1) on average case for operation x E taboo (E: Pertenece)
    #taboo = set()
    #taboo.add(stateObj)
    
    while stack :
        currentNode = stack.popleft()
        
        if currentNode.state.isDeadLock(storages, obstacles):
            #print (currentNode.state.boxes)
            continue
        if currentNode.isParent():
            continue
        else:
            if(currentNode.state.isGoalState(storages)):
                return currentNode
                
            validMovesStates = currentNode.state.possibleMoves(storages, obstacles)
            for childState in validMovesStates:
                
                stack.append(Node(childState, currentNode))

    return None


def printMap(matrix):
    high = len(matrix[0])
    width = len(matrix[0][0])
    for i in range(len(matrix)):
        for j in range(high):
            for k in range(width):
                print (matrix[i][j][k], end='')
            print ()
        print()


def readBoard(obstacles, storages, stateObj):
    agent = ()
    boxes = {}
    numline = 0
    numstorages= 0
    flag = True
    while True:
        try:
            filename = input("mapa: ")
            file = open(str(filename))
            break
        except :
            print("archivo invalido")
    for line in file.readlines():
        if line == "\n":
            break
        if line[0] == "W" or line[0] == "0":
            width = len(line) - 1
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
                coords = line[0:len(line)-1].split(",")
                agent = (int(coords[0]),int(coords[1]))
                numstorages = 0
                flag = False
            else:
                coords = line[0:len(line)-1].split(",")
                boxes[(int(coords[0]),int(coords[1]))] = numstorages
                numstorages = numstorages + 1
            stateObj = State(agent,boxes,agent)
            numline = numline + 1
    file.close()
    print("agent")
    print(agent)
    print("boxes")
    print(boxes)
    stateObj = State(agent,boxes,(0,0))
    return obstacles, storages, stateObj, high, width


if __name__ == '__main__':

    #obstacles = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,4), (1,5), (2,0), (2,5), (3,0), (3,3), (3,5), (4,0), (4,5), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]
    #storages = {(2,1): 0, (2,3):1}
    #stateObj = State((1,2), {(2,2):0, (2,3):1})
    #stateObj.possibleMoves(storages, obstacles)
    #stateObj = State((1,2), {(3,1):0, (2,3):1}, (0,0))
    obstacles = []
    storages = {}
    stateObj = None
    obstacles, storages, stateObj, high, width = readBoard(obstacles, storages, stateObj)
    print("obstacles")
    print(obstacles)
    print("storages")
    print(storages)

    
    result = IDS(stateObj, obstacles, storages)

    if (result):
        printMap (result.getPathMaps(obstacles, storages, high, width))
        print (result.getMoves())
    else:
        'No fue posible solucionar el mapa'

    
    
    

    
    