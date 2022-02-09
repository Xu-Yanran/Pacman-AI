# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import Stack
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))      // this line cause the failure of q1????? 
    actions = []
    start_point = problem.getStartState()
    fringe = Stack()
    visited = []
    fringe.push([start_point, actions])
    flag = False
    while flag != True:
        if fringe.isEmpty():
            print("Failure.")
        node, act = fringe.pop()
        if problem.isGoalState(node):
            flag = True
            print("Found solution")
            actions = act
            break
        if node not in visited:                                             # Important!!!!!!!!!!!!!!
            visited.append(node)
            child_node = problem.getSuccessors(node)
            for i in child_node:
                if i[0] not in visited:
                    # print("-------------------------------")
                    # for v in visited:
                    #     print(v)
                    # print("-------------------------------")
                    # print(i[0])
                    temp = act.copy()
                    temp.append(i[1])
                    # print(act)
                    # print(temp)
                    fringe.push([i[0], temp])
                
    # for i in actions:
    #     print(i)
    # print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # actions = []
    return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import Queue
    visited = []
    actions = []
    fringe = Queue()
    start_point = problem.getStartState()
    flag = False
    count = 0

    fringe.push([start_point, actions])
    while flag != True:
        count += 1
        if fringe.isEmpty():
            print("Failure")
            break
        node, act = fringe.pop()
        if problem.isGoalState(node):
            print("Found solution")
            actions = act
            break
        if node not in visited:                                             # Important!!!!!!!!!!!!!!
            visited.append(node)
            # print(visited)
            child_node = problem.getSuccessors(node)
            for i in child_node:
                if i[0] not in visited:
                    # print(i[0])
                    # print("-------------------------------")
                    # print("count: ", count)
                    # print("node: ", node)
                    # for v in visited:
                    #     print(v)
                    # print("child: ", i[0])
                    # print("-------------------------------")
                    temp = act.copy()
                    temp.append(i[1])
                    # print(temp)
                    fringe.push([i[0], temp])
    # for i in actions:
    #     print(i)
    # print(visited)
    # actions = []
    return actions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import PriorityQueue
    visited = []
    actions = []
    cost = 0
    fringe = PriorityQueue()
    start_point = problem.getStartState()
    
    fringe.push([start_point, actions, cost], 0)
    while(True):
        if fringe.isEmpty():
            print("Failure")
            break
        node, act, c = fringe.pop()
        if problem.isGoalState(node):
            print("Found solution")
            actions = act
            break
        if node not in visited:
            visited.append(node)
            child_node = problem.getSuccessors(node)
            for i in child_node:
                if i[0] not in visited:
                    temp = act.copy()
                    temp.append(i[1])
                    fringe.push([i[0], temp, c+i[2]], c+i[2])

    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import PriorityQueue
    visited = []
    actions = []
    cost = 0
    fringe = PriorityQueue()
    start_point = problem.getStartState()
    
    fringe.push([start_point, actions, cost], heuristic(start_point, problem))
    while(True):
        if fringe.isEmpty():
            print("Failure")
            break
        node, act, c = fringe.pop()
        if problem.isGoalState(node):
            print("Found solution")
            actions = act
            break
        if node not in visited:
            visited.append(node)
            child_node = problem.getSuccessors(node)
            for i in child_node:
                if i[0] not in visited:
                    temp = act.copy()
                    temp.append(i[1])
                    fringe.push([i[0], temp, c+i[2]], c+i[2]+heuristic(i[0], problem))
    return actions

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
