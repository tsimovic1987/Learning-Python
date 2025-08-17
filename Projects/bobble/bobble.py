import argparse
import subprocess


class BobbleCommands:
    def __init__(self, path, argument1, argumenmt2, **kwargs):
        self.path = path
        self.argument1 = argument1
        self.argument2 = argumenmt2
        self.kwargs = kwargs

    def __str__(self):
        output = f"{self.path} - {self.argument1} - {self.argument2}"
        if self.kwargs:
            for key, value in self.kwargs.items():
                output += f" - {key}:{value}"
        return output

    def __len__(self):
        return 3 + len(self.kwargs)

    def __eq__(self, other):
        if not isinstance(other, Bobble):
            return NotImplemented
        return (self.path == other.path and
                self.argument1 == other.argument1 and
                self.argument2 == other.argument2)

    def __hash__(self):
        return hash((self.path, self.argument1, self.argument2))

open_epic = BobbleCommands("pfad", "open", "as", user="root")
print(len(open_epic))
print(open_epic)


def create_command(keyword, file):
    parser = argparse.ArgumentParser(description="Bobble - I love CLI")
    parser.add_argument(keyword, help="Open Command for File/Exe")
    parser.add_argument(file, help="File name")
    args = parser.parse_args()
    if args.keyword == "open":
        try:
            subprocess.run([args.file])
        except FileNotFoundError:
            print(f"File: {args.file} doesnt exists")

create_command("open", "epic.exe")