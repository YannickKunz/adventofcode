import matplotlib.pyplot as plt

def visualize_grid():
    # 1. Parse the input
    points = []
    try:
        with open("input_day9.txt") as input_file:
            for line in input_file:
                line = line.strip()
                if not line: continue
                x, y = map(int, line.split(','))
                points.append((x, y))
    except FileNotFoundError:
        print("Error: input_day9.txt not found. Please ensure the file is in the same directory.")
        return

    # 2. Prepare data for plotting
    # We append the first point to the end to close the loop visually
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    
    x_vals.append(points[0][0])
    y_vals.append(points[0][1])

    # 3. Setup the plot
    plt.figure(figsize=(10, 10))
    
    # Plot the filled area (The "Inside")
    plt.fill(x_vals, y_vals, color='lightgreen', alpha=0.5, label='Inside Area (Green)')
    
    # Plot the boundary lines (The connecting Green tiles)
    plt.plot(x_vals, y_vals, color='darkgreen', linewidth=2, label='Boundary Connection')
    
    # Plot the vertices (The Red tiles)
    # Using a smaller scatter size (s) because there are many points
    plt.scatter(x_vals[:-1], y_vals[:-1], color='red', zorder=5, s=15, label='Red Tiles (Input)')

    # 4. Formatting to match the problem description
    plt.title("Day 9: Movie Theater Floor Pattern")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.axis('equal')  # Ensure squares look like squares

    # CRITICAL: In image processing and matrices (like this AoC grid), 
    # Y usually increases downwards. Matplotlib usually increases upwards.
    # We invert the Y axis to match the "top-down" mental model of the grid.
    plt.gca().invert_yaxis()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_grid()
