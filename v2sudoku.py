
class sudokuBoard():
    def __init__(self, filename):
        self.box = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        self.plines = []
        with open( filename, 'r' ) as f:
            for line in f:
                tmp = []
                for char in line:
                    if char.isnumeric():
                        tmp.append(int(char))
                if tmp != []:
                    self.plines.append(tmp)
                


            
    def check(self, numArr):
        numCount = [1,0,0,0,0,0,0,0,0,0]
        for num in numArr:
            numCount[num] += 1
        for i in range(1,10):
            if numCount[i] > 1:
                return False
        return True

    #returns col 0-8
    #returns (-1) when row is full
    def nextFill(self, r, c):
        for col in range(c,9):
            if self.getRow(r)[col] == 0:
                return col
        return (-1)

    def setVal(self, val, r, c):
        self.plines[r][c] = val            

    def show(self):
        for line in self.plines:
            print(line)
    
    #values to be checked 1-9
    def getRow(self,r):
        return self.plines[r]
    
    #values to be check 1-9
    def getCol(self, c):
        tmp = []
        for row in range(9):
            tmp.append(self.plines[row][c])
        return tmp

    #values to be check 1-9
    def getSq(self,r,c):
        tmp = []
        for row in range(3):
            for col in range(3):
                tmp.append(self.plines[row + ((r//3)*3)%9][col + ((c//3)*3)%9])
        return tmp


    def getVal(self, r, c):
        return self.plines[r][c]

    #If all vals in row contain non-zero there is no next col
    def nextCol(self, r):
        for col in range(9):
            if self.plines[r][col] == 0:
                return col
        return False

    #returns 1,2..,9 when valid -1 otherwise
    def nextVal(self,r,c):
        return -1

    #i 1,2,..,9 if available and usedArr is updated
    #i is -1 if none available usedArr remains the same
    def checkUsed(self,usedArr):
        for i in range(1,10):
            if usedArr[i] == 0:
                usedArr[i] = 1
                return (i, usedArr)
        return (-1, usedArr)


    def gisb(self, r, c):
        if r > 8:
            return True
        C = self.nextFill( r, c )
        solved = False
        used = [1,0,0,0,0,0,0,0,0,0] 
        for val in self.getCol(C):
            used[val] = 1
        for val in self.getRow(r):
            used[val] = 1
        for val in self.getSq(r,C):
            used[val] = 1
        (newVal, used) = self.checkUsed(used)
        print('newVal: ',newVal,'R, C: ', r , C)
        while( not solved ):
            if newVal == -1:
                self.setVal(r, C, 0)
                return False
            self.setVal(newVal,r,C)
            if r > 8 and C == -1:
                return True
            solved = self.gisb(r + 1,C)
            (newVal, used) = self.checkUsed(used)

        return solved


def main():
    #TODO input('Enter sudoku puzzle filename: ') 
    filename = 'puzzle'
    b = sudokuBoard(filename)
    print('#######################')
    print(b.gisb(0,0))
    print('#######################')


if __name__ == "__main__":
    main()
