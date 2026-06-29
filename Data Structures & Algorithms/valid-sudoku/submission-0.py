class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # HashMap for row
        # HashMap for col
        # HashMap for square
        # Formula (row/3)*3 + col/3

        # For row
        row_set = set()
        for i in range(9):
            row_set = set()

            for j in range(9):
                num = board[i][j]

                if num in row_set and num != '.':
                    return False
                row_set.add(num)
            
        # For col
        col_set = set()
        for i in range(9):
            col_set = set()

            for j in range(9):
                num = board[j][i]

                if num in col_set and num != '.':
                    return False
                col_set.add(num)

        board_map = {}
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                num_hash = (i//3)*3 + (j//3)

                if num_hash not in board_map:
                    board_map[num_hash] = set()

                if num in board_map[num_hash]:
                    return False
                
                board_map[num_hash].add(num)
        
        return True





        