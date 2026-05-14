import os


def move_file(command: str) -> None:
    command_parts = command.split()

    source = command_parts[1]
    destination = command_parts[2]

    with open(source, "r") as file:
        text = file.read()

    folders = destination.split("/")

    path = ""

    for folder in folders[:-1]:

        path = path + folder + "/"

        if not os.path.exists(path):
            os.mkdir(path)

    with open(destination, "w") as file:
        file.write(text)

    os.remove(source)
