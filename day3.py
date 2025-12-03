def main():
    print("Hello from adventofcode day 3!")
    count = 0
    new_count = 0
    with open("input_day3.txt") as input:
        for line in input:
            line = line.rstrip()
            m1 = 0
            for i in range(0, len(str(line))-1):
                for j in range(i+1, len(str(line))):
                    tens = int(str(line)[i])
                    ones = int(str(line)[j])
                    current_value = tens*10 + ones

                    if current_value > m1:
                        m1 = current_value
            count += m1

            # Part 2
            current_index = -1
            result_string = ""

            for i in range(11, -1, -1):
                digit = max(line[current_index + 1 : len(line)-i]) 
                current_index = line.index(digit, current_index+1)
                result_string += str(digit)
            new_count += int(result_string) 

        print(count)
        print(f"Part two count: {new_count}")

if __name__ == "__main__":
    main()
