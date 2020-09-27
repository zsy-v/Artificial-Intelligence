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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

class node:
    def __init__(self,mystate):
        self.path = []
        self.cost = 0
        self.real_cost = 0
        self.state = mystate


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    q = PriorityQueue()
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    """innit"""
    now_state = problem.getStartState()
    mynode = node(now_state)
    q.push(mynode,mynode.cost)
    find = False

    """for"""
    debug = 0
    while not find:
        debug = debug + 1
        temp_node = q.pop()#from queue
        total_cost = 0
        successors = problem.getSuccessors(temp_node.state)
        count = len(successors)
        for i in range(count):
            if len(temp_node.path)!=0:
                if temp_node.path[-1] == s and successors[i][1] == n:   #(successor,action, stepCost)
                    continue
                if temp_node.path[-1] == n and successors[i][1] == s:
                    continue
                if temp_node.path[-1] == e and successors[i][1] == w:
                    continue
                if temp_node.path[-1] == w and successors[i][1] == e:
                    continue
            temp_state = successors[i][0]   #successor
            total_cost = successors[i][2]   #cost
            total_cost = total_cost + temp_node.real_cost  #realcost
            next_node = node(temp_state)    #create new
            next_node.state = temp_state    #assign state
            next_node.real_cost = total_cost     #assign realcost
            next_node.cost = total_cost + heuristic(temp_state,problem)     #assign cost
            next_node.path = list(temp_node.path)
            next_node.path.append(successors[i][1])     #append dir
            q.push(next_node,next_node.cost)    #push
            if problem.isGoalState(temp_state):
                find = True
            #print(temp_node.path)
            #if debug >= 3:
            #    break
    #print(next_node.path[0])
    return next_node.path

        

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch