
from queue import PriorityQueue
from math import sqrt


class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal

        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDist(self):
        pass

    def CreateChildren(self):
        pass


class State_Puzzle(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(State_Puzzle, self).__init__(value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):

        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            if self.value[i] != self.goal[i] and self.value[i] != '0':
                dist += 1
        f = dist + len(self.path)
        print("f(n) = g(n) + h(n)")
        print("f(n): " + str(f) + " g(n): " +
              str(len(self.path)) + " h(n): " + str(dist))
        print("Dist: " + str(dist) + " Path: " + str(len(self.path)))
        print("\n")
        return dist

    def CreateChildren(self):
        size = int(sqrt(len(self.goal)).real)
        if not self.children:
            i = self.value.index("0")
            if not int(i % size) == size - 1:
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_Puzzle(val, self)
                self.children.append(child)

            if not int(i % size) == 0:
                val = self.value
                val = val[:i-1] + val[i] + val[i-1] + val[i+1:]
                child = State_Puzzle(val, self)
                self.children.append(child)

            if i < len(self.value) - size:
                val = self.value
                val = val[:i] + val[i+size] + \
                    val[i+1:i+size] + val[i] + val[i+size+1:]
                child = State_Puzzle(val, self)
                self.children.append(child)

            if i > size - 1:
                val = self.value
                val = val[:i-size] + val[i] + \
                    val[i-size+1:i] + val[i-size] + val[i+1:]
                child = State_Puzzle(val, self)
                self.children.append(child)


class AStar_solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_Puzzle(self.start, 0, self.start, self.goal)
        count = 0

        self.priorityQueue.put((0, count, startState))
        while (not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))

        if not self.path:
            print("Goal of " + self.goal + " is not possible")

        return self.path


if __name__ == "__main__":
    # start = "283164705"
    # goal = "123804765"
    start = "152043786"
    goal = "123456780"
    print('starting...')

    a = AStar_solver(start, goal)
    a.Solve()

    for i in range(len(a.path)):
        print("%d) " % i + a.path[i])

    # # for i in range(len(a.path)):
    # #     state = a.path[i]
    # #     print("%d) " % i + state.value + " f(n): " + str(state.dist) +
    # #           " g(n): " + str(len(state.path)) + " h(n): " + str(state.dist - len(state.path)))
    # for i in range(len(a.path)):
    #     state = a.path[i]
    #     value = state.value if isinstance(state, State) else state
    #     dist = state.dist if isinstance(state, State_Puzzle) else 0
    #     print("%d) " % i + value + " f(n): " + str(dist + len(state.path)) +
    #           " g(n): " + str(len(state.path)) + " h(n): " + str(dist))
