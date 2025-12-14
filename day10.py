import time
from collections import deque

def main():
    l = []

    with open("input_day10.txt") as input_file:
        for line in input_file:
            parts = line.strip().split(' ')
            
            # Remove brackets
            t = parts[0].strip('[]')
            # Turn . to 0 and # to 1
            target = [1 if char == '#' else 0 for char in t]
            
            buttons = []

            for b in parts[1:-1]:
                nums = b.strip('()')
                buttons_indices = [int(x) for x in nums.split(',')]
                buttons.append(buttons_indices)

            l.append({'target': target, 'buttons': buttons})


    for machine in l:
        target = machine['target']
        buttons = machine['buttons']
        start = [0] * len(target)

        dq = deque([start])
        visited = set()
        # print(start, target)
        while dq:
            node = dq.popleft()
            

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print("Elapsed time: ", end_time - start_time)
