def main():
    offsets = [(-1, -1), (-1, 0), (-1, 1), 
               (0, -1),           (0, 1), 
               (1, -1),  (1, 0),  (1, 1)]
    grid = []
    with open("input_day4.txt") as input_file:
        for line in input_file:
            line = line.strip()
            grid.append(list(line)) 
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            neighbor_count = 0
            for (dr, dc) in offsets:
                neighbor_r = r + dr
                neighbor_c = c + dc

                if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols:
                    if grid[neighbor_r][neighbor_c] == '@':
                        neighbor_count += 1
            
            if neighbor_count < 4:
                count += 1

    print(f"Count: {count}")

if __name__ == "__main__":
    main()
