from collections import OrderedDict

from anytree import Node, RenderTree


def check_devise_space():
    """
    Solution for part one and two
    """
    file = open("input", 'r')
    root = Node("/")
    device_folders = read_file_system(file.readlines(), root)
    used_memory = directory_size(device_folders)
    directory_to_remove_size(device_folders, used_memory)


def read_file_system(read_filesystem, current):
    """
    Parsing of terminal input into the Nodes

    :read_filesystem: terminal command output
    :line: root node
    :return: a list of folders found on the device
    """
    folders = []
    for command_line in read_filesystem:
        match command_line.split():
            case ['$', *commands]:
                if commands[0] == 'cd':
                    match commands[1].strip():
                        case "/":
                            folders.append(current)
                        case "..":
                            current = current.parent
                        case _:
                            node_childern = current.children
                            for child in node_childern:
                                if child.name == commands[1]:
                                    current = child
                                    break
            case [*commands]:
                if commands[0].isnumeric():
                    # Creating node for file
                    Node(commands[1], parent=current, data=commands[0])
                else:
                    # Creating node for folder, and add it to folder list
                    folder = Node(commands[1], parent=current)
                    folders.append(folder)
    return folders


def directory_size(folders):
    """
    Calculate sum of the total sizes for direcories smaller then 10000

    :folders: list with folder nodes
    :return: total used memory by all folders
    """
    print("------DIRECTORY PART ONE--------")
    used_memory = 0
    total_size = 0
    for folder in folders:
        size = 0
        for file in folder.leaves:
            size += int(file.data)

        if folder.name == "/":
            used_memory = size

        if size < 100000:
            total_size += size

    print("Total size", total_size)
    return used_memory


def directory_to_remove_size(folders, used_memory):
    """
    Calculate smallest directory to remove

    :folders: list with folder nodes
    :used_memory: total used memory by all folders
    """
    print("------DIRECTORY PART TWO--------")
    folders_size = []
    # Max memory on device 70000000
    available_memory = 70000000 - used_memory
    # Min memory to install update 30000000
    required_memory = 30000000 - available_memory
    for folder in folders:
        size = 0
        for file in folder.leaves:
            size += int(file.data)

        if size >= required_memory:
            folders_size.append(size)
    folders_size.sort()
    print("Folder to remove", folders_size[0])


if __name__ == "__main__":
    check_devise_space()