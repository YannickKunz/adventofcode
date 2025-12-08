from collections import Counter
def main():
    l = []
    with open("input_day8.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            line = line.split(',')
            l.append(line)
    #print(l)

    s = set()
    #print(euclidean(l[0],l[1]))

    for p in range(len(l)-1):
        for q in range(p+1, len(l)):
            s.add((euclidean(l[p],l[q]), p, q))
    s = sorted(s)
    #print(s)

    assignments = {}
    for i in range(len(l)):
        assignments[i] = i

    #print(assignments)

    for dist, i, j in s[:1000]:
        id_i = assignments[i]
        id_j = assignments[j]

        if id_i != id_j:
            for k in range(len(l)):
                if assignments[k] == id_j:
                    assignments[k] = id_i

    circuit_sizes = Counter(assignments.values())
    ll = list(circuit_sizes.values())
    ll.sort(reverse=True)
    summation = 1
    for x in ll[:3]:
        summation *= x

    print(summation)

    # Part 2
    remaining_circuits = len(set(assignments.values()))
    for dist, i, j in s[999:]:
        id_i = assignments[i]
        id_j = assignments[j]

        if id_i != id_j:
            for k in range(len(l)):
                if assignments[k] == id_j:
                    assignments[k] = id_i
            remaining_circuits -= 1

            if remaining_circuits == 1:
                new_sum = int(l[i][0]) * int(l[j][0])
                print(new_sum)
                

def euclidean(p1, p2):
    return ((int(p2[0])-int(p1[0]))**2 + (int(p2[1])-int(p1[1]))**2 + (int(p2[2])-int(p1[2]))**2) 



if __name__ == "__main__":
    main()
