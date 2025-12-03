def main():
    print("Hello from adventofcode day 3!")
    count = 0
    with open("input_day3.txt") as input:
        for line in input:
            line = line.rstrip()
            m1 = 0
            for i in range(0, len(str(line))-1):
                for j in range(i+1, len(str(line))):
                    tens = int(str(line)[i])
                    ones = int(str(line)[j])
                    current_value = tens*10 + ones

                    if current_value > max_bank_value:
                        m1 = current_value
            count += m1

            # Part 2
            

        print(count)

if __name__ == "__main__":
    main()
