# Advent of code 2023 - Day 3

from collections import defaultdict

SKIP = ".\n\t\r\b"
MAX_COL = 0

def remove_duplicates(results: dict[tuple]):
    new_dct = {}
    for k, v in results.items():
        new_dct[k] = list(set([i for i in v]))
    return new_dct

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
                return [row, (front, back+1)] # back+1 so that it is inclusive range
            i += 1
            j += 1
    else:
        # no digit found
        return [-1, ()]
        

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
    pass

if __name__ == "__main__":
    part_one()