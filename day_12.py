import sys

def solve_part_1(input):
    width = len(input[0])
    height = len(input)

    inbounds = lambda x, y: 0 <= x < width and 0 <= y < height
    visited = {}
    q = [(0, 0)]
    plot_areas = {}
    plot_fences = {}
    plot_n = 0

    while q:
        x, y = q.pop(0)
        if (x, y) in visited:
            continue
        plant = input[y][x]
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        neighbors = [(n_x, n_y) for n_x, n_y in neighbors if inbounds(n_x, n_y)]
        same_plant_neighbors = [(n_x, n_y) for n_x, n_y in neighbors if input[n_y][n_x] == plant]
        other_plant_neighbors = [(n_x, n_y) for n_x, n_y in neighbors if input[n_y][n_x] != plant]

        visited_same_plant_neighbors = [n for n in same_plant_neighbors if n in visited]
        unvisited_plant_neighbors = [n for n in same_plant_neighbors if n not in visited]
        q = same_plant_neighbors + q + other_plant_neighbors

        plot_i = plot_n

        if visited_same_plant_neighbors:
            plot_i = visited[visited_same_plant_neighbors[0]]

        visited[(x, y)] = plot_i

        plot_areas[plot_i] = plot_areas.get(plot_i, 0) + 1
        plot_fences[plot_i] = plot_fences.get(plot_i, 0) + 4 - len(same_plant_neighbors)

        if not unvisited_plant_neighbors:
            plot_n += 1

    price = 0
    for plot_i in plot_fences:
        price += plot_fences[plot_i] * plot_areas[plot_i]
    return price

def solve_part_2(input):
    pass

def parse_lines(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    return [list(l) for l in lines]

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
