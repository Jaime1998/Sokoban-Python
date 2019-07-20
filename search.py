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


if __name__ == '__main__':
    obstacles = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,4), (1,5), (2,0), (2,5), (3,0), (3,3), (3,5), (4,0), (4,5), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]
    storages = {(2,1): 0, (2,3):1}
    #stateObj = State((1,2), {(2,2):0, (2,3):1})
    #stateObj.possibleMoves(storages, obstacles)

    stateObj = State((1,2), {(3,1):0, (2,3):1}, (0,0))
    result = BFS(stateObj, obstacles, storages)

    if (result):
        printMap (result.getPathMaps(obstacles, storages))
        print (result.getMoves())
    else:
        'No fue posible solucionar el mapa'
    
    
    
    

    
    