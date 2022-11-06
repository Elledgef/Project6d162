#Author: Faith Elledge
#Githubuser: elledgef
#Date: 11/5/22
#Description:

def row_puzzle(row, pos, loc_visited):
    pos = 0
    turn = row[pos]
    if pos < 0 or pos >= len(row):
        return False
    elif pos == (len(row)-1):
            return True
    left_turn = pos - turn
    right_turn = pos + turn

    if pos - turn > 0 or row_puzzle(row, pos + turn, loc_visited):
        return True
    if pos + turn < len(row) or row_puzzle(row,pos + turn, loc_visited):
        return True

    loc_visited.append(pos)




