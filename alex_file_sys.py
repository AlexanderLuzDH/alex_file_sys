class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.current_directory = self.root

    def ls(self):
        print(" ".join(self.current_directory.list_contents()))

    def mkdir(self, path):
        self.current_directory.add_directory(path)
        print(f"Directory '{path}' created.")

    def cd(self, path):
        if path == "/":
            self.current_directory = self.root
            return
        elif path == "..":
            self.current_directory = self.root
        else:
            for item in self.current_directory.contents.values():
                if isinstance(item, Directory) and item.name == path:
                    self.current_directory = item
                    return
            print(f"No such directory: {path}")

    def touch(self, file_name):
        self.current_directory.add_file(file_name)
        print(f"File '{file_name}' created.")

    def process_command(self, command):
        args = command.split()
        if not args:
            return
        cmd = args[0]
        if cmd == "ls":
            self.ls()
        elif cmd == "mkdir" and len(args) > 1:
            self.mkdir(args[1])
        elif cmd == "cd" and len(args) > 1:
            self.cd(args[1])
        elif cmd == "touch" and len(args) > 1:
            self.touch(args[1])
        else:
            print("Invalid command or missing arguments.")

if __name__ == "__main__":
    fs = FileSystem()
    print("File System Simulator. Type 'exit' to quit.")
    while True:
        command = input("> ").strip()
        if command.lower() == 'exit':
            break
        fs.process_command(command)