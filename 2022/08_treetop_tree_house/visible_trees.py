def parse_input():
    """
    Read input file and save data to the array

    :returns: two dimentional array with tree data
    """
    trees = []
    input_file = open("input", 'r')
    for i, tree_row in enumerate(input_file):
        trees.append([])
        for j, tree in enumerate(tree_row.strip()):
            trees[i].append(tree)
    return trees


def parse_trees(trees):
    """
    Find out tree visiablity (Part 1) and Max scenic score (Part 2)

    :trees: Two dimensional array with tree data
    :returns: Number of visible trees (Solution to part 1)
    """
    visible_trees = 0
    tree_scenic_score = []
    for i, tree_row in enumerate(trees):
        # Top edge trees are visible
        if i == 0 or i == len(trees) - 1:
            visible_trees += len(trees)
        else:
            for j, tree in enumerate(tree_row):
                # Edge trees Left and Right are visible
                if j == 0 or j == len(tree_row) - 1:
                    visible_trees += 1
                else:
                    if visible(trees, tree, i, j):
                        visible_trees += 1
                    # Calculate tree scenic score
                    tree_scenic_score.append(scenic_score(trees, tree, i, j))
    print("Max scenic score", max(tree_scenic_score))
    return visible_trees


def visible(trees, tree, i, j):
    """
    Find out if tree is visible

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: True if tree is visible
    """
    if top(trees, tree, i, j) or bottom(trees, tree, i, j) or left(trees, tree, i, j) or right(trees, tree, i, j):
        return True


def top(trees, tree, i, j):
    """
    Find out if tree is visible from the top

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: True if tree is visible from the top
    """
    top_trees = []
    for k, check in enumerate(trees):
        if k < i:
            top_trees.append(check[j])
    if max(top_trees) < tree:
        return True


def bottom(trees, tree, i, j):
    """
    Find out if tree is visible from the bottom

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: True if tree is visible from the bottom
    """
    bottom_trees = []
    for k, check in enumerate(trees):
        if k > i:
            bottom_trees.append(check[j])
    if max(bottom_trees) < tree:
        return True


def left(trees, tree, i, j):
    """
    Find out if tree is visible from the left

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: True if tree is visible from the left
    """
    if max(trees[i][:j]) < tree:
        return True


def right(trees, tree, i, j):
    """
    Find out if tree is visible from the right

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: True if tree is visible from the right
    """
    if max(trees[i][j+1:]) < tree:
        return True


def scenic_score(trees, tree, i, j):
    """
    Calculate scenic score for a tree

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: scenic score
    """
    top_trees = top_score(trees, tree, i, j)
    bottom_trees = bottom_score(trees, tree, i, j)
    left_trees = left_score(trees, tree, i, j)
    right_trees = right_score(trees, tree, i, j)
    return top_trees * bottom_trees * left_trees * right_trees


def top_score(trees, tree, i, j):
    """
    Calculate scenic score for a tree from the top

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: tree score for top
    """
    top_trees = []
    for k, check in enumerate(trees):
        if k < i:
            top_trees.append(check[j])
    top_trees.reverse()
    return calculate_score(top_trees, tree)


def bottom_score(trees, tree, i, j):
    """
    Calculate scenic score for a tree from the bottom

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: tree score for bottom
    """
    bottom_trees = []
    for k, check in enumerate(trees):
        if k > i:
            bottom_trees.append(check[j])
    return calculate_score(bottom_trees, tree)


def left_score(trees, tree, i, j):
    """
    Calculate scenic score for a tree from the left

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: tree score for left
    """
    left_trees = trees[i][:j]
    left_trees.reverse()
    return calculate_score(left_trees, tree)


def right_score(trees, tree, i, j):
    """
    Calculate scenic score for a tree from the right

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :i: x - tree position
    :j: y - tree position
    :returns: tree score for right
    """
    right_trees = trees[i][j+1:]
    return calculate_score(right_trees, tree)


def calculate_score(trees, tree):
    """
    Calculate scenic score for a tree from the top

    :trees: Two dimensional array with tree data
    :tree: Tree high
    :returns: Tree score
    """
    tree_score = 0
    for tr in trees:
        if tr >= tree:
            tree_score += 1
            break
        else:
            tree_score += 1
    return tree_score


def search_for_treetop_tree_house():
    """
    Part 1, part 2
    """
    trees = parse_input()
    print("Visible trees: ", parse_trees(trees))


if __name__ == "__main__":
    search_for_treetop_tree_house()
