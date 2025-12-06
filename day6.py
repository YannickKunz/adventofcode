import math

def main():
    print("Hello from advent of code day 6!")
    rows = []    
    total = 0
    part_two = 0
    with open("input_day6.txt") as input_file:
        for line in input_file:
            line = line.strip()
            line = line.split()
            rows.append(line)

        for i in range(len(rows[0])):
            if rows[-1][i] == '+':
                total += sum(int(rows[j][i]) for j in range(len(rows)-1))
            else:
                total += math.prod(int(rows[j][i]) for j in range(len(rows)-1))

        print(total)

    # Part 2
    part_two = 0
    new_rows = []

    with open("input_day6.txt") as input_file:
        for line in input_file:
            new_rows.append(line.rstrip('\n'))

    max_len = max(len(r) for r in new_rows)
    new_rows = [line.ljust(max_len) for line in new_rows]

    current_nums = []
    current_op = None

    for col in range(max_len - 1, -1, -1):
        col_string = ""
        for row in range(len(new_rows) - 1):
            char = new_rows[row][col]
            if char.isdigit():
                col_string += char

        bottom_char = new_rows[-1][col]
        if bottom_char in ['+', '*']:
            current_op = bottom_char

        if col_string != "":
            current_nums.append(int(col_string))

        if col_string == "" or col == 0:
            if current_nums:
                if current_op == '+':
                    part_two += sum(current_nums)
                elif current_op == '*':
                    part_two += math.prod(current_nums)

                current_nums = []
                current_op = None

    print(part_two)

if __name__ == "__main__":
    main()
