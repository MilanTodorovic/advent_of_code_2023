# Advent of Code 2023 - Day 1

WORDS = {"one":"1", "two":"2", "three":"3", "four":"4", 
		"five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def part_one():
	nums = []
	with open("./input.txt", "r") as file:
		for line in file.readlines():
			tmp = []
			for ch in line:
				if ch.isdigit():
					tmp.append(ch)
			nums.append(int(tmp[0] + tmp[-1]))
	print("Sum: ", sum(nums)) # 55090


def part_two():
	nums = []
	with open("./input.txt", "r") as file:
		for line in file.readlines():
			tmp = {}
			# Find all digits
			for i, ch in zip(range(len(line)-1), line):
				if ch.isdigit():
					tmp[i] = ch
			# Find all words representing digits
			for k,v in WORDS.items():
				# finds only the first occurance, starts at 0
				j = line.find(k)
				if j >= 0: # find returns -1 if it doesn't find anything
					tmp[j] = v # store the starting index of that word as key
					# find all the other, if they exist
					while True:
						l = line.find(k, j+len(k))
						if l >= 0:
							tmp[l] = v
							j = l # set new starting index
						else:
							break

			# sort all the keys
			y = list(tmp.keys())
			y.sort()

			print(y)
			print(tmp)
			nums.append(int(tmp[y[0]] + tmp[y[-1]]))
			print(nums[-1])

	print("Sum: ", sum(nums)) # 54845

if __name__ == "__main__":
	# part_one()
	part_two()