import sys

def solve_part_1(tests):
    return sum(over_under(test[0], test[1:], 0) for test in tests)

def solve_part_2(tests):
    return sum(over_under_with_concat(test[0], test[1:], 0) for test in tests)

def over_under(test_value, values, accum):
    if not values:
        if test_value == accum:
            return test_value
        else:
            return 0
    if accum > test_value:
        return 0

    return max(
        over_under(test_value, values[1:], accum + values[0]),
        over_under(test_value, values[1:], accum * values[0])
    )

def over_under_with_concat(test_value, values, accum):
    if not values:
        if test_value == accum:
            return test_value
        else:
            return 0
    if accum > test_value:
        return 0

    return max(
        over_under_with_concat(test_value, values[1:], accum + values[0]),
        over_under_with_concat(test_value, values[1:], accum * values[0]),
        over_under_with_concat(test_value, values[1:], int(str(accum) + str(values[0])))
    )
    
def parse_lines(lines):
    tests = [l.strip().split(' ') for l in lines if len(l.strip()) > 0]
    tests = [[int(test[0][:-1])] + [int(t) for t in test[1:]] for test in tests]
    return tests

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        tests = parse_lines(lines)
        answer_1 = solve_part_1(tests)
        answer_2 = solve_part_2(tests)
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
