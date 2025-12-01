def main():
    print("Hello from adventofcode!")
    sum = 50
    count = 0
    new_sum = 50
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

            if x[0] == 'L':
                new_sum -= 50

    print(sum)
    print(count)


if __name__ == "__main__":
    main()
