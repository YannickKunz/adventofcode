from collections import defaultdict
def main():
    split_count = 0
    drawing_list =[]
    
    with open("input_day7.txt") as input_file:
        for line in input_file:
            drawing_list.append(line)
        
    start_index = drawing_list[0].index('S')
    print(start_index)
    print(drawing_list[0][start_index])
    current_indices = []
    current_indices.append(start_index)

    for row in drawing_list[1:]:
        next_indices = set()
        for index in current_indices:
            if row[index] == '^':
                split_count += 1
                next_indices.add(index+1)
                next_indices.add(index-1)
            else:
                next_indices.add(index)
        current_indices = []
        current_indices.extend(next_indices)

    # Part 2
    current_indices = {start_index:1}
    for row in drawing_list[1:]:
        next_indices = defaultdict(int)
        for index, particle_count in current_indices.items():
            if row[index] == '^':
                next_indices[index + 1] += particle_count
                next_indices[index - 1] += particle_count
            else:
                next_indices[index] += particle_count
        current_indices = next_indices



    print(split_count)
    print(sum(current_indices.values()))

if __name__ == "__main__":
    main()
