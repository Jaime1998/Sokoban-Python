#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from state import *
from collections import deque


def DFS(stateObj, obstacles, storages):
    startNode = Node (stateObj, None)
    stack = deque([startNode])

    #https://wiki.python.org/moin/TimeComplexity
    #Make taboo the states that i have already reviewed, maybe for anothers paths
    #Pick set for complexity O(1) on average case for operation x E taboo (E: Pertenece)
    #taboo = set()
    #taboo.add(stateObj)
    
    while stack :
        currentNode = stack.pop()
        
        if currentNode.state.isDeadLock(storages, obstacles):
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


def BFS(stateObj, obstacles, storages):
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
    for i in range(len(matrix)):
        for j in range(6):
            for k in range(6):
                print (matrix[i][j][k], end='')
            print ()
        print()


def readBoard(obstacles, storages, stateObj, rows, columns):
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
            columns = len(line) - 1
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
                rows = numline
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
    return obstacles, storages, stateObj, rows, columns


if __name__ == '__main__':

    #obstacles = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,4), (1,5), (2,0), (2,5), (3,0), (3,3), (3,5), (4,0), (4,5), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]
    #storages = {(2,1): 0, (2,3):1}
    #stateObj = State((1,2), {(2,2):0, (2,3):1})
    #stateObj.possibleMoves(storages, obstacles)
    #stateObj = State((1,2), {(3,1):0, (2,3):1}, (0,0))
    obstacles = []
    storages = {}
    stateObj = None
    rows = 0
    columns = 0
    obstacles, storages, stateObj, rows, columns = readBoard(obstacles, storages, stateObj, rows, columns)
    print("obstacles")
    print(obstacles)
    print("storages")
    print(storages)
    print("rows")
    print(rows)
    print("columns")
    print(columns)
    result = BFS(stateObj, obstacles, storages)

    if (result):
        #printMap (result.getPathMaps(obstacles, storages))
        print("bfs")
        print (result.getMoves())
    else:
        'No fue posible solucionar el mapa'

    
    
    

    
    
