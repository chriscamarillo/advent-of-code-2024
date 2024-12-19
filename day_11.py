import sys

def solve_part_1(stones):
    for _ in range(25):
        stones = blink(stones)
    return sum(stones[n] for n in stones)

def solve_part_2(stones):
    for _ in range(75):
        stones = blink(stones)
    return sum(stones[n] for n in stones)

def blink(stones):
    new_stones = {}
    for stone in stones:
        if stone == 0:
            new_stones[1] = new_stones.get(1, 0) + stones[stone]
        elif stone == 1:
            new_stones[2024] = new_stones.get(2024, 0) + stones[stone]
        elif len(str(stone)) % 2 == 0:
            left_half = str(stone)[:len(str(stone))//2]
            right_half = str(stone)[len(str(stone))//2:]
            if len(left_half) > 0:
                left_half = int(left_half)
                new_stones[left_half] = new_stones.get(left_half, 0) + stones[stone]
            if len(right_half) > 0:
                right_half = int(right_half)
                new_stones[right_half] = new_stones.get(right_half, 0) + stones[stone]
        else:
            new_stones[stone*2024] = new_stones.get(stone * 2024, 0) + stones[stone]
    return new_stones


def parse_lines(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    stones = [int(num) for num in lines[0].split(' ')]
    stones = {n: stones.count(n) for n in stones}
    return stones

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
