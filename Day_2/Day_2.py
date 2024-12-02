# Advent of Code 2023 - Day 2

def part_one():
	RED = 12
	GREEN = 13
	BLUE = 14
	possible_games = []
	with open("./input.txt", "r") as file:
		for line in file.readlines():
			game, rest = line.split(":")
			game_nr = int(game.split(" ")[1])
			draws = rest.split(";")
			bad_game = False
			for draw in draws:
				draw = draw.strip()
				cubes = draw.split(",")
				for cube in cubes:
					cube = cube.strip()
					r = cube.find("red")
					if r >= 0:
						num = cube[0:r-1]
						if RED < int(num):
							bad_game = True
							break
					g = cube.find("green")
					if g >= 0:
						num = cube[0:g-1]
						if GREEN < int(num):
							bad_game = True
							break
					b = cube.find("blue")
					if b >= 0:
						num = cube[0:b-1]
						if BLUE < int(num):
							bad_game = True
							break
				if bad_game == True:
					break
			else:
				print("Good game:", game_nr)
				possible_games.append(game_nr)
					

	print("Possible games:", sum(possible_games))

def part_two():
	power = []
	with open("./input.txt", "r") as file:
		for line in file.readlines():
			red, green, blue = [[],[],[]]
			_, rest = line.split(":")
			draws = rest.split(";")
			for draw in draws:
				draw = draw.strip()
				cubes = draw.split(",")
				for cube in cubes:
					cube = cube.strip()
					r = cube.find("red")
					if r >= 0:
						red.append(int(cube[0:r-1]))
					g = cube.find("green")
					if g >= 0:
						green.append(int(cube[0:g-1]))
					b = cube.find("blue")
					if b >= 0:
						blue.append(int(cube[0:b-1]))
			
			power.append(max(red)*max(green)*max(blue))
	print("Sum of powers:", sum(power))

if __name__ == "__main__":
	# part_one()
	part_two()