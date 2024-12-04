import sys

def solve_part_1(reports):
    return sum(is_safe(report) for report in reports)

def solve_part_2(reports):
    return sum(is_safe_with_tolerence(report) for report in reports)

def is_safe_with_tolerence(report):
    error_left_operand_index = find_error(report)
    error_right_operand_index = error_left_operand_index + 1

    if error_left_operand_index == -1:
        return True

    return is_safe(report[:error_left_operand_index] + report[error_left_operand_index+1:])\
        or is_safe(report[:error_right_operand_index] + report[error_right_operand_index+1:])\
        or is_safe(report[1:])

def is_safe(report):
    return find_error(report) == -1

def find_error(report):
    ascending = report[1] - report[0] > 0

    for i in range(len(report) - 1):
        current_value = report[i]
        next_value = report[i + 1]
        difference = next_value - current_value

        # first rule
        if ascending and difference < 0:
            return i
        if not ascending and difference > 0:
            return i

        # second rule
        if abs(difference) < 1 or abs(difference) > 3:
            return i
    return -1

def parse_lines(lines):
    reports = []
    for line in lines:
        report = line.split(' ')
        report = [int(level) for level in report]
        reports.append(report)
    return reports

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        reports = parse_lines(lines)
        answer_1 = solve_part_1(reports)
        answer_2 = solve_part_2(reports)
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
