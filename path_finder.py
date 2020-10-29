from functools import reduce
import numpy as np

class Path_Finder:

    def __init__(self):
        self.maze = None
        self.array_maze = []

    def set_array_maze(self, maze):
        self.array_maze = maze
        self.n = len(self.array_maze)

    def set_string_maze(self, maze):
        self.maze = maze.split()
        self.array_maze = []
        self.locations = {}

        finish = False
        for i in range(len(self.maze)):
            new_line = []
            for j in range(len(self.maze[i])):
                new_line.append(self.maze[i][j])
                if self.maze[i][j] == '0':
                    self.locations[0] = [[i,j]]
                elif self.maze[i][j] == 'F':
                    finish = True
            self.array_maze.append(new_line)

        self.n = max(len(self.array_maze), len(self.array_maze[0]))
        if not self.locations:
            self.locations[0] = [[0,0]]
            self.array_maze[0][0] = 0

        if not finish:
            self.array_maze[-1][-1] = 'F'

    def find_path(self):
        self.path_tracks = [[[0,0]]]
        i = 0
        while True:
            if not self.locations[i]:
                return False
            for loc in self.locations[i]:

                # [[0,0], [0,1], ..]
                # [[0,0], [1,0], ..]
                # if self.find_steps == None
                # delete paths with that step in it
                # else copy path with that step for all find_steps found and add onto it


                if not i+1 in self.locations.keys():
                    self.locations[i+1] = []

                steps = self.find_steps(loc, self.n)

                # print(self.path_tracks)

                if len(steps) == 0:
                    t = []
                    for path in self.path_tracks:
                        if loc not in path:
                            t.append(path)
                    self.path_tracks = t[::]

                else:
                    t = []
                    paths_to_duplicate = []
                    for path in self.path_tracks:
                        if loc in path:
                            paths_to_duplicate.append(path)
                        else:
                            t.append(path)
                    self.path_tracks = t[::]

                    for step in steps:
                        if step == 'F':
                            self.path = np.array(paths_to_duplicate[0]).flatten().tolist()
                            return True

                        for path in paths_to_duplicate:
                            route = path + [step]
                            self.path_tracks.append(route)

                        self.array_maze[step[0]][step[1]] = i+1
                        self.locations[i+1].append(step)

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
        if loc[1] + 1 < len(self.array_maze[0]):
            right = self.array_maze[loc[0]][loc[1]+1]
            if right == 'F':
                return ['F']
            if right == '.':
                r_locs.append([loc[0], loc[1]+1])

        # down
        if loc[0]+1 < len(self.array_maze):
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
      ".W...." * 10,
      ".W...." * 10,
      ".W.WW." * 10,
      "....W." * 10,
      "....W." *10,
    ])


    pf = Path_Finder()
    pf.set_string_maze(d)
    pf.find_path()
    # pf.print_maze()
    print(pf.path)
    # print(reduce(lambda z, y :z + y, reduce(lambda z, y :z + y, pf.locations.values())))
