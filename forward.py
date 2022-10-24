import sys
import time

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def parse(path):
        matrix = []
        with open(path, 'r') as f:
            for line in f:
                l = list(line.strip())
                matrix.append(l)
        return Matrix(matrix)
    
    def print(self):
        for line in self.matrix:
            line = ''.join(line)
            print(line)
    
    def neighbours(self, i, j):
        dir = [1, 0, -1]
        n = 0
        for di in dir:
            for dj in dir:
                ci = i + di
                cj = j + dj
                if not (dj == 0 and di == 0) and cj >= 0 and ci >= 0 and ci < len(self.matrix) and cj < len(self.matrix[0]):
                    c = self.matrix[ci][cj]
                    if c == 'X':
                        n += 1
        return n

    def forwards(self):
        matrix = []
        for i in range(len(self.matrix)):
            l = []
            for j in range(len(self.matrix[0])):
                n = self.neighbours(i, j)
                c = self.matrix[i][j]
                if c == '.':
                    t = 'X' if n == 3 else '.'
                else:
                    t = 'X' if n == 2 or n == 3 else '.'    
                l.append(t)
            matrix.append(l)
                    
        return Matrix(matrix)
    
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Cogway Game of Life visualizer')
    parser.add_argument('path', help='Path to the starting point of the game of life')
    parser.add_argument('iterations', nargs='?', type=int, default=123, help='Number of forward iterations in the game of life')
    parser.add_argument('-mode', '-m', choices=['automatic', 'manual'], default='automatic', help='Operation mode for the visualizer')
    args = parser.parse_args()
    
    m = Matrix.parse(args.path)
    for it in range(args.iterations):
        clear_screen()
        print('=================')
        m.print()
        print('=================')
        m = m.forwards()
        if args.mode == 'automatic':
            sleep_time = 2 if it < 2 else 0.10
            time.sleep(sleep_time)
        elif it != args.iterations - 1:
            print('-------------')
            input('Press Enter to Continue')        
    
    print('-------------')
    print('Finished!')
    print('-------------')



if __name__ == '__main__':
    main()