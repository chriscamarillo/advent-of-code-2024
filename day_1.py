import sys

def solve_part_1(left_list, right_list):
    sorted_pairs = zip(sorted(left_list), sorted(right_list))
    differences = [abs(p[0] - p[1]) for p in sorted_pairs]
    return sum(differences)

def solve_part_2(left_list, right_list):
    counter = {}
    for right_val in right_list:
        if right_val in counter:
            counter[right_val] += 1
        else:
            counter[right_val] = 1
    similarity_score = 0
    for left_val in left_list:
        if left_val in counter:
            similarity_score += left_val * counter[left_val]
    return similarity_score

def parse_lines(lines):
    pairs = [_parse_line(line) for line in lines]
    left_list, right_list = zip(*pairs)
    return left_list, right_list

def _parse_line(line): 
    left_val, right_val = line.strip().split(' ', 1)
    left_val, right_val = int(left_val), int(right_val)
    return left_val, right_val

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        left_list, right_list = parse_lines(lines)
        answer_1 = solve_part_1(left_list, right_list)
        answer_2 = solve_part_2(left_list, right_list)
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
