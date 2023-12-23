from collections import defaultdict


def main(file):
    games = read_input(file)
    powers = get_powers(games)

    return sum(powers)


def read_input(file):
    games = []

    with open(file) as input_file:
        for line in input_file:
            game = line.rstrip('\n').split(': ')[1]
            games.append(transform_cube_sets(game.split('; ')))

    return games


def transform_cube_sets(cube_sets):
    return [transform_cube_set(cube_set) for cube_set in cube_sets]


def transform_cube_set(cube_set):
    cube_map = defaultdict(int)

    for cube in cube_set.split(', '):
        result = cube.split(' ')
        cube_map[result[1]] = int(result[0])

    return cube_map


def get_powers(games):
    powers = []

    for game in games:
        red, green, blue = get_cubes_used(game)
        powers.append(max(red) * max(green) * max(blue))

    return powers


def get_cubes_used(game):
    red = []
    green = []
    blue = []

    for cube_set in game:
        red.append(cube_set['red'])
        green.append(cube_set['green'])
        blue.append(cube_set['blue'])

    return red, green, blue


if __name__ == '__main__':
    print(main('input.txt'))
