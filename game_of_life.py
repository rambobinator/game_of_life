from time import sleep

def get_map_from_file(filename):
	_map = []
	with open(filename) as f:
		for line in f:
			row = []
			for c in line[:-1]:
				row.append(True if c == '1' else False)
			_map.append(row)
		return _map

def display_map(_map, old_map, iteration):
	s = "Iteration: {}\n".format(iteration)
	for y, row in enumerate(_map):
		for x, cell in enumerate(row):
			if cell:
				s += 'o' if old_map[y][x] else '.'
			else:
				s += ' '
		s += '\n'
	print(s, end='')

def get_neighbors_count(_map, cell_pos):
	try:
		row_len = len(_map[0])
	except IndexError:
		return 0
	neighbors_pos_list = frozenset([
		(-1, -1), (-1, 0), (-1, 1),
		(0, -1), (0, 1),
		(1, -1), (1, 0), (1, 1),
	])
	cy, cx = cell_pos
	neighbors_count = 0
	for np in neighbors_pos_list:
		ny, nx = np
		y, x = (ny + cy, nx + cx)
		if y >= 0 and y < len(_map) and x >= 0 and x < row_len:
			if _map[y][x]:
				neighbors_count += 1
	return neighbors_count

def update_map(_map):
	new_map = [[False for x in range(0, len(_map[0]))]
		for y in range(0, len(_map))]
	for y, row in enumerate(_map):
		for x, cell in enumerate(row):
			neighbors_count = get_neighbors_count(_map, (y, x))
			if neighbors_count == 3 or (neighbors_count == 2 and _map[y][x]):
				new_map[y][x] = True
	return new_map

def run(_map):
	iteration = 0
	while True:
		iteration += 1
		old_map = _map[:]
		_map = update_map(_map)
		display_map(_map, old_map, iteration)
		sleep(1)

if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		_map = get_map_from_file(sys.argv[1])
		run(_map)
	else:
		print("Usage: python game_of_life.py map")
