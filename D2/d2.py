def part1(play):
	points = (ord(play[1]) - 1) % 3 + 1

	if ord(play[0]) % 3 == ord(play[1]) % 3: #Win
		return points + 6
	if (ord(play[0]) - 1) % 3 == ord(play[1]) % 3: #Draw
		return points + 3

	return points #Lose

def part2(play):
	result = (ord(play[1]) - 1) % 3 * 3

	if result == 6: #Win
		return result + (ord(play[0]) - 1)  % 3 + 1
	if result == 3: #Draw
		return result + (ord(play[0]) + 1) % 3 + 1

	return result + (ord(play[0]))  % 3 + 1 #Lose


with open("example.txt", "r") as f:
	lst = [el.strip().split() for el in f.readlines()]
	print(sum(list(map(part1, lst)))) # Part1
	print(sum(list(map(part2, lst)))) # Part2