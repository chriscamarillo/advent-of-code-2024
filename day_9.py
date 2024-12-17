import sys
from copy import deepcopy

def solve_part_1(disk):
    space_pos = find_next_space(disk)
    num_pos = find_next_num(disk)
    while space_pos[0] < num_pos[0] or space_pos[1] < num_pos[1]:
        disk[space_pos[0]][space_pos[1]] = disk[num_pos[0]][num_pos[1]]
        disk[num_pos[0]][num_pos[1]] = '.'
        space_pos = find_next_space(disk)
        num_pos = find_next_num(disk)
    disk = [file for block in disk for file in block]
    return checksum(disk)

def solve_part_2(disk):
    n_files = len(disk)
    disk = [file for block in disk for file in block]
    for file_to_move in range(n_files)[::-1]:
        file_pos = disk.index(file_to_move)
        file_width = disk.count(file_to_move)
        free_space_pos = find_n_spaces(disk, file_width)
        if free_space_pos != -1 and free_space_pos < file_pos:
            p1 = disk[:free_space_pos]
            p2 = [file_to_move] * file_width
            p3 = disk[free_space_pos+file_width:file_pos]
            p4 = ['.'] * file_width
            p5 = disk[file_pos+file_width:]
            disk = p1 + p2 + p3 + p4 + p5
    return checksum(disk)

def checksum(disk):
    return sum(pos * int(id) for pos, id in enumerate(disk) if id != '.')

def find_n_spaces(flat_disk, n):
    for i in range(len(flat_disk) - n):
        if flat_disk[i:i+n] == ['.'] * n:
            return i
    return -1

def find_next_space(disk):
    for file_id in range(len(disk)):
        file = disk[file_id]
        for spot in range(len(file)):
            if file[spot] == '.':
                return (file_id, spot)
    return (-1, -1)

def find_next_num(disk):
    for file_id in range(len(disk))[::-1]:
        file = disk[file_id]
        for spot in range(len(file))[::-1]:
            if file[spot] != '.':
                return (file_id, spot)
    return (-1, -1)

def parse_lines(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    disk_map = lines[0]
    disk = []
    file_id = 0
    for file_i in range(0, len(disk_map), 2):
        n_blocks = int(disk_map[file_i])
        n_free_space = 0 if file_i+1 >= len(disk_map) else int(disk_map[file_i+1])
        file = [file_id for _ in range(n_blocks)]
        file.extend(['.' for _ in range(n_free_space)])
        disk.append(file)
        file_id += 1
    return disk
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        input = parse_lines(lines)
        answer_1 = solve_part_1(deepcopy(input))
        answer_2 = solve_part_2(deepcopy(input))
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
