def reed_input():
    return open("input", 'r')


def parse_input(trees):
    input_file = reed_input()
    for i, tree_row in enumerate(input_file):
        trees.append([])
        for j, tree in enumerate(tree_row.strip()):
            trees[i].append(tree)


def find_visible_trees(trees):
    visible_t = 0
    ss = []
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
                    ss.append(scenic_score(trees, tree, i, j))
    print("scenic score", ss)
    print("Max scenic score", max(ss))
    return visible_t


def visible(trees, tree, i, j):
    if top(trees, tree, i, j):
        return True

    if bottom(trees, tree, i, j):
        return True

    if left(trees, tree, i, j):
        return True

    if right(trees, tree, i, j):
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
    top = top_score(trees, tree, i, j)
    bottom = bottom_score(trees, tree, i, j)
    left = left_score(trees, tree, i, j)
    right = right_score(trees, tree, i, j)
    # print(top, left, bottom, right)
    return top * bottom * left * right

def top_score(trees, tree, i, j):
    top_trees = []
    tree_score = 0
    for k, check in enumerate(trees):
        if k < i:
            top_trees.append(check[j])
    top_trees.reverse()
    for tr in top_trees:
        if tr >= tree:
            tree_score += 1
            break
        else:
            tree_score += 1
    return tree_score


def bottom_score(trees, tree, i, j):
    bottom_trees = []
    tree_score = 0
    for k, check in enumerate(trees):
        if k > i:
            bottom_trees.append(check[j])
    for tr in bottom_trees:
        if tr >= tree:
            tree_score += 1
            break
        else:
            tree_score += 1
    return tree_score


def left_score(trees, tree, i, j):
    tree_score = 0
    left_trees = trees[i][:j]
    left_trees.reverse()
    for tr in left_trees:
        if tr >= tree:
            tree_score += 1
            break
        else:
            tree_score += 1
    return tree_score


def right_score(trees, tree, i, j):
    tree_score = 0
    right_trees = trees[i][j+1:]
    # print(right_trees)
    for tr in right_trees:
        if tr >= tree:
            tree_score += 1
            break
        else:
            tree_score += 1
    return tree_score


def visible_trees():
    trees = []
    parse_input(trees)
    print("Visible trees: ", find_visible_trees(trees))


if __name__ == "__main__":
    visible_trees()