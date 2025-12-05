def main():
    offsets = [(-1, -1), (-1, 0), (-1, 1), 
               (0, -1),           (0, 1), 
               (1, -1),  (1, 0),  (1, 1)]
    
    grid = []

    with open("input_day4.txt") as input_file:
        for line in input_file:
            grid.append(list(line.strip())) 

    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0

    # Start the simulation loop
    while True:
        removed_this_round = []

        # 1. SCAN PHASE: Find everything that needs to be removed
        for r in range(rows):
            for c in range(cols):
                
                # Check if it is a paper roll
                if grid[r][c] == '@':
                    neighbor_count = 0
                    
                    # Check neighbors
                    for (dr, dc) in offsets:
                        neighbor_r = r + dr
                        neighbor_c = c + dc

                        if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols:
                            if grid[neighbor_r][neighbor_c] == '@':
                                neighbor_count += 1
                    
                    # If accessible, mark for removal (don't remove yet!)
                    if neighbor_count < 4:
                        removed_this_round.append((r, c))

        # 2. CHECK PHASE: Did we find anything?
        if len(removed_this_round) == 0:
            break # Stop the simulation if nothing changed
        
        # 3. UPDATE PHASE: Remove the rolls from the grid
        total_removed += len(removed_this_round)
        
        for (r, c) in removed_this_round:
            grid[r][c] = '.' # Turn the paper roll into empty space

        # Optional: Print progress to watch it work
        print(f"Round complete. Removed {len(removed_this_round)} rolls.")

    print(f"Total rolls removed: {total_removed}")

if __name__ == "__main__":
    main()
