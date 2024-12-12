import sys
from itertools import product

def solve_part_1(input):
    tiles_visited, _ = simulate_patrol(*input)
    return tiles_visited

def solve_part_2(input):
    num_rows, num_cols, guard_pos, guard_direction, obstacles = input
    possible_obstacle_pos = (coords for coords in product(range(num_cols), range(num_rows)) if coords not in obstacles and coords != guard_pos)
    
    loop_inducing_obstacles = sum(
        simulate_patrol(num_rows, num_cols, guard_pos, guard_direction, obstacles.union({po_pos}))[1] 
        for po_pos in possible_obstacle_pos
    )
    return loop_inducing_obstacles

def simulate_patrol(num_rows, num_cols, guard_pos, guard_direction, obstacles):
    tiles_visited = set()

    step = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0),
    }

    rotations = ['^', '>', 'v', '<']
    inbounds = lambda pos: (0 <= pos[0] < num_cols) and (0 <= pos[1] < num_rows)
    move = lambda pos, direction: tuple(px + dx for px, dx in zip(pos, step[direction]))
    turn = lambda direction: rotations[(rotations.index(direction) + 1) & 0x3]

    looped = False
    path = set()

    while inbounds(guard_pos) and not looped:
        if (guard_pos, guard_direction) in path:
            looped = True

        tiles_visited.add(guard_pos)
        path.add((guard_pos, guard_direction))
        next_pos = move(guard_pos, guard_direction)

        if next_pos in obstacles:
            guard_direction = turn(guard_direction)
        else:
            guard_pos = next_pos

    return (len(tiles_visited), looped)

def parse_lines(lines):
    # clean up lines
    lines = [l.strip() for l in lines if len(l.strip()) > 0]

    num_rows = len(lines)
    num_cols = len(lines[0])

    obstacles = set()
    guard_pos = None
    guard_direction = None

    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            if tile == '<' or tile == '>' or tile == '^' or tile == 'v':
                guard_pos = (x, y)
                guard_direction = tile
            elif tile == '#':
                obstacle_pos = (x, y)
                obstacles.add(obstacle_pos)

    return (num_rows, num_cols, guard_pos, guard_direction, obstacles)

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
