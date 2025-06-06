def column_correct(sudoku: list, column_no: int):

    check = []

    for row in sudoku:
        char = row[column_no]
        if char != 0:
            if char in check:
                return False
            check.append(char)
    return True

