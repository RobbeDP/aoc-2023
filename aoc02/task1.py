from collections import defaultdict


thresholds = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def main(file):
    games = read_input(file)
    valid_games = get_valid_games(games)

    return sum(valid_games)


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


def get_valid_games(games):
    return [index + 1 for index, game in enumerate(games) if test_game(game)]


def test_game(game):
    for cube_set in game:
        if (
            cube_set['red'] > thresholds['red'] or
            cube_set['green'] > thresholds['green'] or
            cube_set['blue'] > thresholds['blue']
        ):
            return False

    return True


if __name__ == '__main__':
    print(main('input.txt'))
