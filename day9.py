import time

def main():
    l = []
    with open("input_day9.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            line = line.split(',')
            l.append(line)

    # print(l)
    area_set = set()
    for p1 in range(len(l)-1):
        for p2 in range(p1+1, len(l)):
            length = abs(int(l[p2][0]) - int(l[p1][0])) + 1
            width = abs(int(l[p2][1]) - int(l[p1][1])) + 1
            area = length*width
            area_set.add((area, p1, p2))
    area_set = sorted(area_set)
    # print(area_set)
    print(area_set[-1][0])

    # Part 2
    print(max(l[1]), max(l[2]))
    my_list = []
    for p in range(len(l)-1):
        q = p+1
        my_list.append((l[p], l[q]))
    
    total_length = 0
    for p1, p2 in my_list:
        # print(p1, p2)
        if p1[0] == p2[0]:
            dist = abs(int(p2[1]) - int(p1[1]))
        else:
            dist = abs(int(p2[0]) - int(p1[0]))
        total_length += dist

    poly_lines = []

    for i in range(len(l)):
        p_start = l[i]
        p_end = l[(i + 1) % len(l)]
        lx1, lx2 = sorted((int(p_start[0]), int(p_end[0])))
        ly1, ly2 = sorted((int(p_start[1]), int(p_end[1])))
        poly_lines.append((lx1, lx2, ly1, ly2))

    candidates = []
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            p1 = l[i]
            p2 = l[j]
            width = abs(int(p1[0]) - int(p2[0])) + 1
            height = abs(int(p1[1]) - int(p2[1])) + 1
            area = width * height
            
            rx1, rx2 = sorted((int(p1[0]), int(p2[0])))
            ry1, ry2 = sorted((int(p1[1]), int(p2[1])))
            candidates.append((area, (rx1, rx2, ry1, ry2)))

    candidates.sort(key=lambda x: x[0], reverse=True)

    for area, rect in candidates:
        rx1, rx2, ry1, ry2 = rect
        overlap = False
        for lx1, lx2, ly1, ly2 in poly_lines:
            if rx1 < lx2 and rx2 > lx1 and ry1 < ly2 and ry2 > ly1:
                overlap = True
                break
        
        if not overlap:
            print(area)
            break
       
        
    #print(my_list)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print("Elapsed time: ", end_time-start_time)
