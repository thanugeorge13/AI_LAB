import copy

def get_puzzle(name):
    print(f"\nEnter the {name} puzzle (3x3, use -1 for blank):")
    puzzle = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1} (space-separated 3 numbers): ").split()))
        puzzle.append(row)
    return puzzle

def move(puzzle, direction):
    # Create a deep copy to avoid mutating the original puzzle
    temp = copy.deepcopy(puzzle)
    for i in range(3):
        for j in range(3):
            if temp[i][j] == -1:
                x, y = i, j
                break

    if direction == "up" and x > 0:
        temp[x][y], temp[x-1][y] = temp[x-1][y], temp[x][y]
        return temp
    elif direction == "down" and x < 2:
        temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]
        return temp
    elif direction == "left" and y > 0:
        temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]
        return temp
    elif direction == "right" and y < 2:
        temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]
        return temp
    return None  # Invalid move

def dls(puzzle, depth, limit, last_move, goal):
    if puzzle == goal:
        return True, [puzzle], []

    if depth >= limit:
        return False, [], []

    for move_dir, opposite in [("up", "down"), ("left", "right"), ("down", "up"), ("right", "left")]:
        if last_move == opposite:
            continue  # Avoid backtracking

        new_state = move(puzzle, move_dir)
        if new_state is not None and new_state != puzzle:
            found, path, moves = dls(new_state, depth + 1, limit, move_dir, goal)
            if found:
                return True, [puzzle] + path, [move_dir] + moves

    return False, [], []

def ids(start, goal):
    for limit in range(1, 50):
        print(f"\nTrying depth limit = {limit}")
        found, path, moves = dls(start, 0, limit, None, goal)
        if found:
            print("\nSolution found!")
            for step in path:
                for row in step:
                    print(row)
                print()
            print("Moves:", moves)
            print("Path cost =", len(path) - 1)
            return
    print("Solution not found within depth limit.")

start_puzzle = get_puzzle("start")
goal_puzzle = get_puzzle("goal")

print("\n~~~~~~~~~~~~ IDDFS ~~~~~~~~~~~~")
ids(start_puzzle, goal_puzzle)
