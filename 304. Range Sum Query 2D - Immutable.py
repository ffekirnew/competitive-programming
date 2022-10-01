class NumMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        # storing the matrix is not neccessary, reduces the coefficient of the big O by avoiding to save it
        
        # find the prefix sum of the box
        self.prefix = []
        for i in range(len(matrix)):
            self.prefix.append([])
            row = self.prefix[-1]
            row_sum = 0
            for j in range(len(matrix[0])):
                row_sum += matrix[i][j]
                row.append(row_sum)
                row[-1] += self.prefix[i-1][j] if (i > 0) else 0
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # find the prefix sum until the bottom corner
        answer = self.prefix[row2][col2]
        # reduce the prefix top of the first row of our box
        answer -= self.prefix[row1 - 1][col2] if (row1 > 0) else 0
        # reduce the prefix left of the left column of our box
        answer -= self.prefix[row2][col1 - 1] if (col1 > 0) else 0
        # add the intersection that was reduced twice  sort of like n(A U B) = n(A) + n(B) - n(A n B)
        answer += self.prefix[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0
        
        # return the object
        return answer
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
