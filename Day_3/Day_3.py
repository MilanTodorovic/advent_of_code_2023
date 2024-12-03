# Advent of code 2023 - Day 3

from collections import defaultdict

SKIP = ".\n\t\r\b"
MAX_COL = 0

def remove_duplicates(results: dict[tuple]):
    # results = {(138, 129): [{137: (126, 129)}, {137: (130, 133)}]}
    #           star coords:   row:coords digits, ...
    new_dct = {}
    new_new_dct = {}
    for k, v in results.items(): # (,):[...]
        for j in v: # {int:(,)}
            for _k, _v in j.items():
                new_dct[_k] = list(set([i for i in _v]))
            new_new_dct[k] = new_dct
    return new_new_dct

def check_number(lines: str, row: int, col: int):
    # To get the solution for part_one change
    #   the return value to be a list [row, (front, back+1)]

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
                return {row:(front, back+1)} # back+1 so that it is inclusive range
            i += 1
            j += 1
    else:
        # no digit found
        return {-1: ()}
        

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
        if row > 0:
            if col > 0:
                res = check_number(lines, row-1, col-1)
                results[res[0]].append(res[1]) # works because we use defaultdict wich initializes a list on first call
            res = check_number(lines, row-1, col)
            results[res[0]].append(res[1])
            if col < MAX_COL:
                res = check_number(lines, row-1, col+1)
                results[res[0]].append(res[1])
        if col > 0:
            res = check_number(lines, row, col-1)
            results[res[0]].append(res[1])
        if col < MAX_COL:
            res = check_number(lines, row, col+1)
            results[res[0]].append(res[1])
        if row < max_row:
            if col > 0:
                res = check_number(lines, row+1, col-1)
                results[res[0]].append(res[1])
            res = check_number(lines, row+1, col)
            results[res[0]].append(res[1])
            if col < MAX_COL:
                res = check_number(lines, row+1, col+1)
                results[res[0]].append(res[1])
    results.pop(-1) # I was too lazy to make proper checks
    
    dct = remove_duplicates(results)

    lst = []

    for k,v in dct.items():
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

    results = defaultdict(list)
    for star in star_coords:
        tmp = {}
        row,col = star[0],star[1]
        # Do all 8 directions
        if row > 0:
            if col > 0:
                res = check_number(lines, row-1, col-1)
                if res.get(-1,1):
                    tmp[(row,col)].append(res) # works because we use defaultdict wich initializes a list on first call
            res = check_number(lines, row-1, col)
            if res.get(-1,1):
                tmp[(row,col)].append(res)
            if col < MAX_COL:
                res = check_number(lines, row-1, col+1)
                if res.get(-1,1):
                    tmp[(row,col)].append(res)
        if col > 0:
            res = check_number(lines, row, col-1)
            if res.get(-1,1):
                tmp[(row,col)].append(res)
        if col < MAX_COL:
            res = check_number(lines, row, col+1)
            if res.get(-1,1):
                tmp[(row,col)].append(res)
        if row < max_row:
            if col > 0:
                res = check_number(lines, row+1, col-1)
                if res.get(-1,1):
                    tmp[(row,col)].append(res)
            res = check_number(lines, row+1, col)
            if res.get(-1,1):
                tmp[(row,col)].append(res)
            if col < MAX_COL:
                res = check_number(lines, row+1, col+1)
                if res.get(-1,1):
                    tmp[(row,col)].append(res)
        if len(tmp.keys()) == 2:
            results.append(tmp)

    dct = remove_duplicates(results)
    print(dct)
    lst = []

    for k,v in dct.items():
        if len(v) == 2:
            a, b = v[0], v[1]
            x, y = lines[k[0]][a[0]:a[1]], lines[k[0]][b[0]:b[1]]
            #print(x,y)
            lst.append(int(x) * int(y))
    print("Summed part no.:", sum(lst)) # 

if __name__ == "__main__":
    #part_one()
    part_two()