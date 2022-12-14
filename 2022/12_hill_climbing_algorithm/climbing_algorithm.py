# Next to z is {
# BFS

def parse_input(input_file):
    heightmap = []
    input_file = open(input_file, 'r')
    for path in input_file.readlines():
        heightmap.append(path.strip())
    return heightmap


def create_graph(heightmap):
    id = 0
    pre_graph = []
    for y, line in enumerate(heightmap):
        for x, element in enumerate(line):
            pre_graph.append({"id": id, "node": element, "x": x, "y": y})
            id += 1

    pre_graph[0]["node"] = 'a'

    for node in pre_graph:
        right = [d["id"] for d in pre_graph if d['x'] == node['x'] + 1 and d['y'] == node['y']]
        left = [d["id"] for d in pre_graph if d['x'] == node['x'] - 1 and d['y'] == node['y']]
        top = [d["id"] for d in pre_graph if d['x'] == node['x'] and d['y'] == node['y'] + 1]
        bottom = [d["id"] for d in pre_graph if d['x'] == node['x'] and d['y'] == node['y'] - 1]
        neighbours = [*right, *left, *top, *bottom]
        node["neighbours"] = neighbours

    for node in pre_graph:
        go = [d["id"] for d in pre_graph if ord(node['node']) - ord(d['node']) >= -1 and d["id"] in node["neighbours"]]
        node["go"] = go
    return pre_graph




def move_direction(heightmap, starting_position, steps):

    #print("____________________")
    #print("Way ", way_to_the_top)

    #if heightmap[starting_position["x"]][starting_position["y"]] == 'p':
    #    print("FOT DEBUG")

    if starting_position["x"] == 4 and starting_position["y"] == 3:
        print("DEBUG")

    if heightmap[starting_position["x"]][starting_position["y"]] == 69:
        print("On top")
        print("steps", steps)
        print_path(heightmap)

    if starting_position["x"] + 1 < len(heightmap):  # Up
        new_position = {"x": starting_position["x"] + 1, "y": starting_position["y"]}
        if cant_move(heightmap, starting_position, new_position):
            steps += 1
            hm = heightmap.copy()
            move_direction(hm, new_position, steps)

    if starting_position["x"] - 1 > -1:  # Down
        new_position = {"x": starting_position["x"] - 1, "y": starting_position["y"]}
        if cant_move(heightmap, starting_position, new_position):
            steps += 1
            hm = heightmap.copy()
            move_direction(hm, new_position, steps)

    if starting_position["y"] + 1 < len(heightmap[0]):
        new_position = {"x": starting_position["x"], "y": starting_position["y"] + 1}
        if cant_move(heightmap, starting_position, new_position):
            steps += 1
            hm = heightmap.copy()
            move_direction(hm, new_position, steps)

    if starting_position["y"] - 1 > -1:
        new_position = {"x": starting_position["x"], "y": starting_position["y"] - 1}
        if cant_move(heightmap, starting_position, new_position):
            steps += 1
            hm = heightmap.copy()
            move_direction(hm, new_position, steps)


def dont_move_back(position, prev_position):
    if position in prev_position:
        return False
    else:
        return True


def cant_move(heightmap, starting_position, new_position):
    #print(heightmap)
    #print("STR", starting_position, heightmap[starting_position["x"]][starting_position["y"]])
    #print("NEW", new_position, heightmap[new_position["x"]][new_position["y"]])
    starting_position_height = heightmap[starting_position["x"]][starting_position["y"]] == 83 and 97 or heightmap[starting_position["x"]][starting_position["y"]]
    new_position_height = heightmap[new_position["x"]][new_position["y"]] == 69 and 122 or heightmap[new_position["x"]][new_position["y"]]
    if new_position_height == 126 or starting_position_height - new_position_height < -1:
        return False
    else:
        heightmap[starting_position["x"]][starting_position["y"]] = 126
        return True



def move(heightmap, starting_position):
    steps = 0
    way_to_the_top = [{"x": 0, "y": 0}]
    # routes = []
    #print(heightmap[starting_position["x"]][starting_position["y"]])
    way = move_direction(heightmap, starting_position, steps)


def climbing():
    print("Climbing")
    heightmap = parse_input("input_test")

    pre_graph = create_graph(heightmap)
    print(pre_graph)


    #print_path(heightmap)
    #ove(heightmap, starting_position)


def print_path(heightmap):
    print("-------------")
    for line in heightmap:
        print(line.decode("ascii"))
    print("-------------")

if __name__ == "__main__":
    climbing()
