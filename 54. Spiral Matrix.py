class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # create variables to hold the length and height of the matrix
        row = len(matrix)
        col = len(matrix[0])
        # create the object to be returned
        answer = []
        # create a hashmap to keep track of the already visited rows
        rows = {}
        columns = {}
        # create direction guide
        curr_direction = 'r'
        # create a variable to aid in the looping
        i, j = 0, 0
        while len(rows.keys()) <= len(matrix):
            answer.append(matrix[i][j])
            if curr_direction == 'r':
                next_col = j + 1
                if next_col in columns or next_col == col:
                    next_row = i + 1
                    if next_row in rows or next_row == row: break
                    else: 
                        rows[i] = 1
                        i, curr_direction = next_row, 'd'
                else: j = next_col
            elif curr_direction == 'd':
                next_row = i + 1
                if next_row in rows or next_row == row:
                    next_col = j - 1
                    if next_col in columns or next_col == -1: break
                    else:
                        columns[j] = 1
                        j, curr_direction = next_col, 'l'
                else: i = next_row
            elif curr_direction == 'l':
                next_col = j - 1
                if next_col in columns or next_col == -1:
                    next_row = i - 1
                    if next_row in rows or next_row == -1: break
                    else:
                        rows[i] = 1
                        i, curr_direction = next_row, 'u'
                else: j = next_col
            else:
                next_row = i - 1
                if next_row in rows or next_row == -1:
                    next_col = j + 1
                    if next_col in columns or next_col == col: break
                    else:
                        columns[j] = 1
                        j, curr_direction = next_col, 'r'
                else: i = next_row
            
                    
        # return the object
        return answer
