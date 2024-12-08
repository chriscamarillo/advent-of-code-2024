import sys

def solve_part_1(crossword):
    n_rows = len(crossword)
    n_cols = len(crossword[0].strip())

    horiz = 0
    vert = 0
    diag = 0

    for y in range(n_rows):
        for x in range(n_cols):
            if y < n_rows - 3 and x < n_cols - 3:
                back_slash = ''.join(crossword[y+i][x+i] for i in range(4))
                forward_slash = ''.join(crossword[y+3-i][x+i] for i in range(4))
                if back_slash == 'XMAS' or back_slash == 'SAMX':
                    diag += 1
                if forward_slash == 'XMAS' or forward_slash == 'SAMX':
                    diag += 1
            if y < n_rows - 3:
                bar = ''.join(crossword[y+i][x] for i in range(4))
                if bar == 'XMAS' or bar == 'SAMX':
                    vert += 1
            if x < n_cols - 3:
                dash = ''.join(crossword[y][x+i] for i in range(4))
                if dash == 'XMAS' or dash == 'SAMX':
                    horiz += 1
    return horiz + vert + diag 

def solve_part_2(crossword):
    n_rows = len(crossword)
    n_cols = len(crossword[0].strip())

    diag = 0

    for y in range(n_rows):
        for x in range(n_cols):
            if y < n_rows - 2 and x < n_cols - 2:
                back_slash = ''.join(crossword[y+i][x+i] for i in range(3))
                forward_slash = ''.join(crossword[y+2-i][x+i] for i in range(3))
                if (back_slash == 'MAS' or back_slash == 'SAM') and (forward_slash == 'MAS' or forward_slash == 'SAM'):
                    diag += 1
    return diag 

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        answer_1 = solve_part_1(lines)
        answer_2 = solve_part_2(lines)
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
