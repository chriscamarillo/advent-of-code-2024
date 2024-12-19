import sys

def solve_part_1(input):
    top_map, trail_heads = input
    print('======= TRAILS PT 1 =======')
    scores = [get_score(th, top_map, set(), f'{th} | ', False) for th in trail_heads]
    return sum(scores)

def solve_part_2(input):
    top_map, trail_heads = input
    print('======= TRAILS PT 2 =======')
    scores = [get_score(th, top_map, set(), f'{th} | ', True) for th in trail_heads]
    return sum(scores)

def get_score(head, top_map, peaks, trail, score_distinct=False):
    x, y = head
    height = len(top_map)
    width = len(top_map[0])
    if inbounds(x, y, width, height):
        current_elevation = top_map[y][x]
        if top_map[y][x] == 9 and ((x, y) not in peaks or score_distinct):
            peaks.add((x, y))
            print(trail + f'[[ ({x}, {y}) ]]')
            return 1
        else:
            up = 0 if not inbounds(x, y-1, width, height) or top_map[y-1][x] != current_elevation + 1 else get_score((x, y-1), top_map, peaks, trail+f'({x}, {y-1})->', score_distinct)
            down = 0 if not inbounds(x, y+1, width, height) or top_map[y+1][x] != current_elevation + 1 else get_score((x, y+1), top_map, peaks, trail+f'({x}, {y+1})->', score_distinct)
            left = 0 if not inbounds(x-1, y, width, height) or top_map[y][x-1] != current_elevation + 1 else get_score((x-1, y), top_map, peaks, trail+f'({x-1}, {y})->', score_distinct)
            right = 0 if not inbounds(x+1, y, width, height) or top_map[y][x+1] != current_elevation + 1 else get_score((x+1, y), top_map, peaks, trail+f'({x+1}, {y})->', score_distinct)
            return sum([up, down, left, right])
    return 0

def inbounds (x, y, width, height):
    return (0 <= x < width) and (0 <= y < height)

def parse_lines(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    top_map = [[int(e) for e in list(l)] for l in lines]
    trail_heads = []
    for y, row in enumerate(top_map):
        for x, col in enumerate(row):
            if col == 0:
                trail_heads.append((x, y))
    return top_map, trail_heads

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        input = parse_lines(lines)
        answer_1 = solve_part_1(input)
        answer_2 = solve_part_2(input)
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
