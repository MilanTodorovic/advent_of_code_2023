# Advent of code 2023 - Day 3

from collections import defaultdict

SKIP = ".\n\t\r\b"
MAX_COL = 0

def check_number(lines: str, row: int, col: int):
    global MAX_COL

    if lines[row][col].isdigit():
        i = 1
        j = 1
        front = col
        back = col
        front_end = False
        back_end = False
        while True:
            if not front_end and lines[row][col-i].isdigit():
                front = col-i
                if col-i-1 < 0:
                    front_end = True
            else:
                front_end = True
            if not back_end and lines[row][col+j].isdigit():
                back = col+j
                if col+j+1 > MAX_COL:
                    back_end = True
            else:
                back_end = True
            if front_end and back_end:
                return int(lines[row][front:back+1])
                #return [row, (front, back+1)] # back+1 so that it is inclusive range
            i += 1
            j += 1
    else:
        # no digit found
        return None
        

def part_one():
    global MAX_COL

    lines = []
    symbols = []
    with open("./input.txt", "r") as file:
        lines = list(file.readlines())

    MAX_COL = len(lines[0])
    max_row = len(lines)

    for row, line in zip(range(len(lines)),lines):
        for col, ch in zip(range(len(line)),line):
            if not ch.isalnum() and ch not in SKIP:
                # Save symbol location
                symbols.append([row,col])

    results = defaultdict(list) # row:[digits]
    for sym in symbols:
        tmp = []
        row,col = sym[0],sym[1]
        # Do all 8 directions
        if col > 0:
            # Left
            res = check_number(lines, row, col-1)
            if res:
                results[res[0]].append(res[1])
        if col < MAX_COL:
            # Right
            res = check_number(lines, row, col+1)
            if res:
                results[res[0]].append(res[1])
        if row > 0:
            # Upper mid
            res = check_number(lines, row-1, col)
            # If no number is found right above the *
            #   check left, then right
            if not res:
                # Upper left
                res = check_number(lines, row-1, col-1)
                if res:
                    results[res[0]].append(res[1])
                # Upper right
                res = check_number(lines, row-1, col+1)
                if res:
                    results[res[0]].append(res[1])
            else:
                results[res[0]].append(res[1])
        if row < max_row:
            # Same as above
            res = check_number(lines, row+1, col)
            if not res:
                # Bottom left
                res = check_number(lines, row+1, col-1)
                if res:
                    results[res[0]].append(res[1])
                # Bottom right
                res = check_number(lines, row+1, col+1)
                if res:
                    results[res[0]].append(res[1])
            else:
                results[res[0]].append(res[1])

    lst = []

    for k,v in results.items():
        for i in v:
            lst.append(int(lines[k][i[0]:i[1]]))
    print("Summed part no.:", sum(lst)) # 529618

def part_two():
    global MAX_COL

    lines = []
    star_coords = []
    with open("./input.txt", "r") as file:
        lines = list(file.readlines())

    MAX_COL = len(lines[0])
    max_row = len(lines)

    for row, line in zip(range(len(lines)),lines):
        for col, ch in zip(range(len(line)),line):
            if ch == "*":
                # Save symbol location
                star_coords.append([row,col])

    results = []
    for star in star_coords:
        row,col = star[0],star[1]
        tmp = []
        # Do all 8 directions
        if col > 0:
            # Left
            res = check_number(lines, row, col-1)
            if res is not None:
                tmp.append(res)
        if col < MAX_COL:
            # Right
            res = check_number(lines, row, col+1)
            if res is not None:
                tmp.append(res)
        if row > 0:
            # Upper mid
            res = check_number(lines, row-1, col)
            # If no number is found right above the *
            #   check left, then right
            if res is None:
                # Upper left
                res = check_number(lines, row-1, col-1)
                if res is not None:
                    tmp.append(res)
                # Upper right
                res = check_number(lines, row-1, col+1)
                if res is not None:
                    tmp.append(res)
            else:
                tmp.append(res)
        if row < max_row:
            # Same as above
            res = check_number(lines, row+1, col)
            if res is None:
                # Bottom left
                res = check_number(lines, row+1, col-1)
                if res is not None:
                    tmp.append(res)
                # Bottom right
                res = check_number(lines, row+1, col+1)
                if res is not None:
                    tmp.append(res)
            else:
                tmp.append(res) # works because we use defaultdict wich initializes a list on first call

        if len(tmp) == 2:
            results.append(tmp[0]*tmp[1])

    print("Summed part no.:", sum(results)) # 

if __name__ == "__main__":
    #part_one()
    part_two()