import sys

def parse_lines(lines):
    reports = []
    for line in lines:
        report = line.split(' ')
        report = [int(level) for level in report]
        reports.append(report)
    return reports

def is_safe(report):
    sign = None

    for current_index in range(len(report) - 1):
        next_index = current_index + 1

        current_value = report[current_index]
        next_value = report[next_index]

        difference = next_value - current_value

        # second rule
        if abs(difference) < 1 or abs(difference) > 3:
            return False
        
        # first rule
        if sign == None:
            if difference < 0:
                sign = 'neg'
            else:
                sign = 'pos'
        else:
            if sign == 'neg' and difference > 0:
                return False
            if sign == 'pos' and difference < 0:
                return False
    return True

def find_failure(report):
    sign = None

    for current_index in range(len(report) - 1):
        next_index = current_index + 1

        current_value = report[current_index]
        next_value = report[next_index]

        difference = next_value - current_value

        # second rule
        if abs(difference) < 1 or abs(difference) > 3:
            return current_index, next_index
        
        # first rule
        if sign == None:
            if difference < 0:
                sign = 'neg'
            else:
                sign = 'pos'
        else:
            if sign == 'neg' and difference > 0:
                return current_index, next_index
            if sign == 'pos' and difference < 0:
                return current_index, next_index
    raise Exception('why did this even get reached???')

def solve_part_1(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count

def solve_part_2(reports):
    count = 0
    saved = 0
    for report in reports:
        if is_safe(report):
            count += 1
        else:
            current_index_of_failure, next_index_of_failure = find_failure(report)
            previous_index_of_failure = current_index_of_failure - 1
            if is_safe(report[:current_index_of_failure] + report[current_index_of_failure + 1:])\
                or is_safe(report[:next_index_of_failure] + report[next_index_of_failure + 1:])\
                or is_safe(report[:previous_index_of_failure] + report[previous_index_of_failure + 1:]):
                print(report)
                saved += 1
                count += 1
    print('saved: ', saved)
    return count

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
