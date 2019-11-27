import collections
import sys
class SnakeGame:

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.height = height
        self.width = width
        self.o_d = collections.OrderedDict()
        self.o_d.update({(0,0):1})
        self.head = (0,0)
        self.food = collections.deque()
        for element in food:
            self.food.append(element)
        self.length = 1
    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        if direction == "R":
            move = [0,1]
        elif direction == "L":
            move = [0,-1]
        elif direction == "U":
            move = [-1,0]
        elif direction == "D":
            move = [1,0]
        else:
            return sys.maxsize
        n_r,n_c = self.head[0] + move[0], self.head[1] + move[1]
        if n_r >= 0 and n_c >= 0 and n_r < self.height and n_c < self.width and (n_r,n_c) not in self.o_d.keys():
            self.o_d.update({(n_r,n_c):1})
            self.head = (n_r,n_c)
            if self.food:
                if n_r == self.food[0][0] and n_c == self.food[0][1]:
                    self.food.popleft() 
                    self.length += 1
                    return self.length - 1

                else:
                    self.o_d.popitem(last = False)
                    return self.length - 1
            else:
                self.o_d.popitem(last = False)
                return self.length - 1
        else:
            tail = self.o_d.popitem(last = False)
            if  n_r == tail[0][0] and n_c == tail[0][1]:
                self.o_d.update({(n_r,n_c):1})
                self.head = (n_r,n_c)
                return self.length - 1
            else:
                return -1
            


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)


a = SnakeGame(3,3,[[2,0],[0,0],[0,2],[2,2]])


m = [["D"],["D"],["R"],["U"],["U"],["L"],["D"],["R"],["R"],["U"],["L"],["D"]]
for movement in m:
    print(a.move(movement[0]))