

class Path_Finder:

    def __init__(self):
        self.maze = None
        self.array_maze = []

    def set_array_maze(self, maze):
        self.array_maze = maze

    def set_maze(self, maze):
        self.maze = self.maze.split()
        self.array_maze = []
        locations = {}

        for i in range(len(self.maze)):
            new_line = []
            for j in range(len(self.maze[i])):
                new_line.append(self.maze[i][j])
                if self.maze[i][j] == '0':
                    locations[0] = [[i,j]]
            self.array_maze.append(new_line)

        n = len(self.array_maze)
        if not locations:
            locations[0] = [[0,0]]
            self.array_maze[0][0] = 0

    def find_path(self, maze):
        self.array_maze = maze
        locations = {0:[[0,0]]}
        self.array_maze[0][0] = 0

        i = 0
        while True:
            if not locations[i]:
                return False
            for loc in locations[i]:
                if not i+1 in locations.keys():
                    locations[i+1] = []
                for step in self.find_steps(loc, n):
                    if step == 'F':
                        return True
                    self.array_maze[step[0]][step[1]] = i+1
                    locations[i+1].append(step)

            # self.print_maze()
            i+=1

    def find_steps(self, loc, n):
        r_locs = []

        # up
        if loc[0] > 0:
            up = self.array_maze[loc[0]-1][loc[1]]
            if up == 'F':
                return ['F']
            if up == '.':
                r_locs.append([loc[0]-1, loc[1]])

        #right
        if loc[1] < n-1:
            right = self.array_maze[loc[0]][loc[1]+1]
            if right == 'F':
                return ['F']
            if right == '.':
                r_locs.append([loc[0], loc[1]+1])

        # down
        if loc[0] < n-1:
            down = self.array_maze[loc[0]+1][loc[1]]
            if down == 'F':
                return ['F']
            if down == '.':
                r_locs.append([loc[0]+1, loc[1]])

        #left
        if loc[1] > 0:
            left = self.array_maze[loc[0]][loc[1]-1]
            if left == 'F':
                return ['F']
            if left == '.':
                r_locs.append([loc[0], loc[1]-1])

        return r_locs

    def print_maze(self):
        for line in self.array_maze:
            print(line)
        print("\n")



if __name__ == "__main__":

    d = "\n".join([
      ".W.F.." + ".W...." * 5,
      ".W...." * 6,
      ".W.WW." * 6,
      "....W." * 6,
      "....W." * 6,
      "....W." * 5 + "....W0"
    ])


    pf = Path_Finder()
    pf.set_maze(d)
    pf.find_path()
