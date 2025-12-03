def main():
	print("Hello from adventofcode day 2!")
	count = 0	
	part_two_count = 0
	with open("input_day2.txt") as input:
		for x in input:
			current = x.split(',')
			#print(current[0], current[1])			
			for ranges in current:
				values = ranges.split('-')
				for y in range(int(values[0]), int(values[-1])+1):
					if len(str(y)) % 2 == 0:
						if str(y)[:len(str(y))//2 + len(str(y))%2] == str(y)[len(str(y))//2 + len(str(y))%2:]:
							count += y
	# Part 2
		
					for l in range(1, len(str(y))//2+1):
						pattern = str(y)[:l]
						n = len(str(y)) // l
						if int(pattern*n) == y:
							part_two_count += y
							break
						
			
	print(count)
	print(part_two_count)					

if __name__ == "__main__":
	main()
