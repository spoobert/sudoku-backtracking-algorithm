class sudokuBoard():
    def __init__(self, filename):
        with open( filename, 'r' ) as f:
            self.plines = [line.split() for line in f]
		
		
    def check(self):
        boxes = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for n in range(9):
            i = self.getCol(n)
            j = self.getRow(n)
            k = self.getSq(boxes[n][0], boxes[n][1])
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for m in i:
                l[int(m)] += 1
            l[0] = 0
            for m in l:
                if(m > 1):
                    return False
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for m in j:
                l[int(m)] += 1
            l[0] = 0
            for m in l:
                if(m > 1):
                    return False
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for m in k:
                l[int(m)] += 1
            l[0] = 0
            for m in l:
                if(m > 1):
                    return False
        return True

    def show(self):
        for line in self.plines:
            print(line)

    def getRow(self,r):
        return self.plines[r]

    def getCol(self,c):
        tmp = []
        for row in range(9):
            tmp.append(self.plines[row][c])
        return tmp
    def getSq(self,r,c):
        tmp = []
        for row in range(3):
            for col in range(3):
                tmp.append(self.plines[row + ((r//3)*3)%9][col + ((c//3)*3)%9])
        return tmp
    
    def getVal(self, r, c):
        return int(self.plines[r][c])
    
    ##By: Trent
    def setVal(self, r, c, v):
        self.plines[r][c] = str(v)
        
    ##By: Trent
    def getNextVal(self, r, c):
        R = r
        C = c
        while(C < 9 and self.getVal(R, C) != 0):
            R = R+1
            if(R >= 9):
                R = 0
                C = C+1
        if(C >= 9):
            return (-1, -1)
        else:
            return (R, C)

    ##By: Trent
    def GISB(self, n, m):
        current = self.getVal(n, m)
        okay = False
        used = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
        for elements in self.getCol(m):
            used[int(elements)] = 1

        for stnemele in self.getRow(n):
            used[int(stnemele)] = 1

        for mentsele in self.getSq(n, m):
            used[int(mentsele)] = 1

        for p in range(10):
            q = -1
            if(used[p] == 0):
                q = p
                used[q] = 1
                break
        
        while(not okay):
            
            if(q == -1):
                self.setVal(n, m, 0)
                return False
            #set Value
            self.setVal(n, m, q)
            (r, c) = self.getNextVal(n, m)
            if((r, c) == (-1, -1)):
                return True
            okay = self.GISB(r, c)
            #select next valid number
            for p in range(10):
                q = -1
                if(used[p] == 0):
                    q = p
                    used[q] = 1
                    break
        return okay

def main():
    filename = input('Enter sudoku puzzle filename: ') 
    b = sudokuBoard(filename)
    if(not b.check()):
        print("No Solution")
    else:
        (r,c) = b.getNextVal(0,0)
        if b.GISB(r,c):
            print('Valid Sudoku')
            print('#######################')            
            b.show()
            print('#######################')
        else:
            print('No Solution')    

if __name__ == "__main__":
    main()
