import sys
from itertools import combinations

def solve_part_1(antenna_map, grid_width, grid_height):
    all_anti_nodes = set()
    for frequency in antenna_map:
        anti_nodes = find_anti_nodes(antenna_map, frequency, grid_width, grid_height)
        all_anti_nodes = all_anti_nodes.union(anti_nodes)
    return len(all_anti_nodes)

def solve_part_2(antenna_map, grid_width, grid_height):
    all_anti_nodes = set()
    for frequency in antenna_map:
        anti_nodes = find_anti_nodes(antenna_map, frequency, grid_width, grid_height, True)
        all_anti_nodes = all_anti_nodes.union(anti_nodes)
    return len(all_anti_nodes)

def find_anti_nodes(antenna_map, frequency, grid_width, grid_height, all_grid_search=False):
    antennas = antenna_map[frequency]
    pairs = combinations(antennas, 2)
    anti_nodes = set()
    inbounds = lambda x, y: (0 <= x < grid_width) and (0 <= y < grid_height)
    for a, b in pairs:
        a_x, a_y = a
        b_x, b_y = b
        dx, dy = b_x - a_x, b_y - a_y
        if all_grid_search:
            while inbounds(a_x, a_y):
                anti_nodes.add((a_x, a_y))
                a_x, a_y = a_x - dx, a_y - dy
            while inbounds(b_x, b_y):
                anti_nodes.add((b_x, b_y))
                b_x, b_y = b_x + dx, b_y + dy 
        else:
            if inbounds(a_x - dx, a_y - dy):
                anti_nodes.add((a_x - dx, a_y - dy))
            if inbounds(b_x + dx, b_y + dy):
                anti_nodes.add((b_x + dx, b_y + dy))
    return anti_nodes


def parse_lines(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    grid_width = len(lines[0])
    grid_height = len(lines)
    antenna_map = {}
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            if col != '.':
                if col not in antenna_map:
                    antenna_map[col] = set()
                antenna_map[col].add((x, y))    
    return antenna_map, grid_width, grid_height

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        antenna_map, grid_width, grid_height = parse_lines(lines)
        answer_1 = solve_part_1(antenna_map, grid_width, grid_height)
        answer_2 = solve_part_2(antenna_map, grid_width, grid_height)
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
