def reed_input():
    return open("input", 'r')


def parse_input(trees):
    input_file = reed_input()
    for i, tree_row in enumerate(input_file):
        trees.append([])
        for j, tree in enumerate(tree_row.strip()):
            trees[i].append(tree)


def parse_trees(trees):
    visible_t = 0
    tree_scenic_score = []
    for i, tree_row in enumerate(trees):
        if i == 0 or i == len(trees) - 1:
            visible_t += len(trees)
        else:
            for j, tree in enumerate(tree_row):
                if j == 0 or j == len(tree_row) - 1:
                    visible_t += 1
                else:
                    if visible(trees, tree, i, j):
                        visible_t += 1
                    tree_scenic_score.append(scenic_score(trees, tree, i, j))
    print("Max scenic score", max(tree_scenic_score))
    return visible_t


def visible(trees, tree, i, j):
    if top(trees, tree, i, j) or bottom(trees, tree, i, j) or left(trees, tree, i, j) or right(trees, tree, i, j):
        return True


def top(trees, tree, i, j):
    top_trees = []
    for k, check in enumerate(trees):
        if k < i:
            top_trees.append(check[j])
    if max(top_trees) < tree:
        return True


def bottom(trees, tree, i, j):
    bottom_trees = []
    for k, check in enumerate(trees):
        if k > i:
            bottom_trees.append(check[j])
    if max(bottom_trees) < tree:
        return True


def left(trees, tree, i, j):
    if max(trees[i][:j]) < tree:
        return True


def right(trees, tree, i, j):
    if max(trees[i][j+1:]) < tree:
        return True


def scenic_score(trees, tree, i, j):
    top_trees = top_score(trees, tree, i, j)
    bottom_trees = bottom_score(trees, tree, i, j)
    left_trees = left_score(trees, tree, i, j)
    right_trees = right_score(trees, tree, i, j)
    return top_trees * bottom_trees * left_trees * right_trees


def top_score(trees, tree, i, j):
    top_trees = []
    for k, check in enumerate(trees):
        if k < i:
            top_trees.append(check[j])
    top_trees.reverse()
    return calculate_score(top_trees, tree)


def bottom_score(trees, tree, i, j):
    bottom_trees = []
    for k, check in enumerate(trees):
        if k > i:
            bottom_trees.append(check[j])
    return calculate_score(bottom_trees, tree)


def left_score(trees, tree, i, j):
    left_trees = trees[i][:j]
    left_trees.reverse()
    return calculate_score(left_trees, tree)


def right_score(trees, tree, i, j):
    right_trees = trees[i][j+1:]
    return calculate_score(right_trees, tree)


def calculate_score(trees, tree):
    tree_score = 0
    for tr in trees:
        if tr >= tree:
            tree_score += 1
            break
        else:
            tree_score += 1
    return tree_score


def visible_trees():
    trees = []
    parse_input(trees)
    print("Visible trees: ", parse_trees(trees))


if __name__ == "__main__":
    visible_trees()