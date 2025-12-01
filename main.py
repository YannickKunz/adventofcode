def main():
    print("Hello from adventofcode!")
    sum = 50
    count = 0
    new_sum = 50
    count_two = 0
    with open("input_day1.txt") as inp:
        for x in inp:
            if x[0] == 'L':
                sum -= int(x[1:])
                if sum%100==0:
                    count += 1
            else:
                sum += int(x[1:])
                if sum%100==0:
                    count += 1

            # Part 2
            if x[0] == 'L':
                dist_to_zero = new_sum if new_sum > 0 else 100
                if int(x[1:]) >= dist_to_zero:
                    count_two += 1
                    remaining_amount = int(x[1:])  - dist_to_zero
                    count_two += remaining_amount // 100
                new_sum = (new_sum - int(x[1:])) % 100
            else:
                new_sum += int(x[1:])
                count_two += new_sum // 100
                new_sum = new_sum % 100

    print(sum)
    print(count)
    print(new_sum)
    print(count_two)

if __name__ == "__main__":
    main()
