import sys

def solve_part_1(rules, updates):
    page_sum = 0
    for update in updates:
        if not find_errors(rules, update):
            n_mid = int(update[len(update)//2])
            page_sum += n_mid
    return page_sum

def solve_part_2(rules, updates):
    page_sum = 0
    for update in updates:
        errors = find_errors(rules, update)
        if errors:
            corrected_update = correct_update(update, rules, errors)
            n_mid = int(corrected_update[len(corrected_update)//2])
            page_sum += n_mid
    return page_sum

def correct_update(update, rules, errors):
    while errors:
        i_error = errors.pop(0)
        temp = update[i_error]
        update[i_error] = update[i_error + 1]
        update[i_error + 1] = temp
        errors = find_errors(rules, update)
    return update

def find_errors(rules, update):
    errors = []
    for i in range(len(update) - 1):
        n_curr = update[i]
        n_next = update[i+1]
        
        if n_curr in rules['before'] and n_next in rules['before'][n_curr]:
            errors.append(i)
        elif n_next in rules['after'] and n_curr in rules['after'][n_next]:
            errors.append(i)
    return errors
    

def parse_lines(lines):
    rules = {
        'before': {},
        'after': {},
    }
    updates = []

    for line in lines:
        line = line.strip()
        if len(line) > 0:
            if line.find('|') != -1:
                n_before, _, n_after = line.partition('|')
                
                if n_after not in rules['before']:
                    rules['before'][n_after] = set()
                if n_before not in rules['after']:
                    rules['after'][n_before] = set()

                rules['before'][n_after].add(n_before)
                rules['after'][n_before].add(n_after)
            else:
                updates.append(line.split(','))
    
    return rules, updates

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python {sys.argv[0]} filename')
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        rules, updates = parse_lines(lines)
        answer_1 = solve_part_1(rules, updates)
        answer_2 = solve_part_2(rules, updates)
        print('answer 1: {}, answer 2: {}'.format(answer_1, answer_2))
