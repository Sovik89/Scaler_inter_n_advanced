# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# A partially filled sudoku which is valid.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


def isValidSudoku( A):
        # We are going to take an inventory of row, column and each 3X3 block
        # We are going to iterate each items in the 9x9 matrix
        # We are going to keep it as ROW_<value>_POS:<position>,COL_<value>_POS:<position> and
        # BOX_<value>_POS:<position> in hashset, if it is present in hashset. return 0
        # else insert. If we make it through every thing we return 1(means valid)
        #Note we dont consider cellls with "."
        seen = set()
    
        for row in range(9):
            for col in range(9):
                if A[row][col] !=".":
                    string_row="ROW"+"_"+A[row][col]+"_"+"POS:"+str(row)
                    string_col="COL"+"_"+A[row][col]+"_"+"POS:"+str(col)
                    string_box="BOX"+"_"+A[row][col]+"_"+"POS:"+str((row//3)*3+(col//3))
                    
                    if string_row in seen:
                        return 0
                    else:
                        seen.add(string_row)
                    if string_col in seen:
                        return 0
                    else:
                        seen.add(string_col)
                    if string_box in seen:
                        return 0
                    else:
                        seen.add(string_box)  



        #print(seen)
        return 1
    

print(isValidSudoku(
    ["53..7....", 
     "6..195...", 
     ".98....6.", 
     "8...6...3", 
     "4..8.3..1", 
     "7...2...6", 
     ".6....28.", 
     "...419..5", 
     "....8..79"]
))
