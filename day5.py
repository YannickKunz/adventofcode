def main():

    ranges = []
    counter = 0
    sum = 0
    with open("input_day5.txt") as input_file:
        for line in input_file:
            line = line.strip()
            if '-' in line:
                r = line.split('-')
                ranges.append([int(r[0]), int(r[1])])
            elif line == "":
                ranges.sort()
                merged_ranges = []
                if ranges:
                    merged_ranges.append(ranges[0])

                for current_range in ranges[1:]:
                    last_added = merged_ranges[-1]

                    if current_range[0] <= last_added[1]:
                        last_added[1] = max(current_range[1], last_added[1])
                    else:
                        merged_ranges.append(current_range)
                ranges = merged_ranges

                #print(ranges)
                continue
            else:
                ids = int(line)
                #print(ids)
                for r in ranges:
                    if r[0] <= ids <= r[1]:
                        counter += 1
                        break

    for r in ranges:
        sum += r[1] - r[0] + 1
    print(counter)
    print(sum)





if __name__ == "__main__":
    main()
