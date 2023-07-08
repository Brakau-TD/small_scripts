class UserInterface:
    def __init__(self) -> None:
        pass

    def set_folders(self) -> list:
        folders = []
        while True:
            name = input("Enter folder name: ")
            if name == "":
                break
            folders.append(name)
        folders.insert(0, "back one level")
        return folders