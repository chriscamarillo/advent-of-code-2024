import sys
import re

mul_pattern = re.compile(r"mul\(\d{0,3},\d{0,3}\)")
arg_pattern = re.compile(r"(\d+),(\d+)")
cond_pattern = re.compile(r"(do\(\)|don't\(\))")

def solve_part_1(memory):
    mul_sum = 0

    for line in memory: 
        mul_sum += sum(parse_mul(match.group()) for match in mul_pattern.finditer(line))

    return mul_sum

def solve_part_2(memory):
    mul_sum = 0
    should_accumulate = True

    for line in memory:
        mul_ops = [(match.start(), match.group()) for match in mul_pattern.finditer(line)]
        conditions = [(match.start(), match.group()) for match in cond_pattern.finditer(line)]
        while mul_ops or conditions:
            if mul_ops and conditions and (conditions[0][0] < mul_ops[0][0] or not mul_ops):
                    should_accumulate = conditions.pop(0)[1] == 'do()'
            else:
                mul_sum += parse_mul(mul_ops.pop(0)[1]) * int(should_accumulate)
    
    return mul_sum

def parse_mul(mul_op):
    left_op, right_op = arg_pattern.search(mul_op).groups()
    left_op, right_op = int(left_op), int(right_op)
    return left_op * right_op

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        answer_1 = solve_part_1(lines)
        answer_2 = solve_part_2(lines)
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
