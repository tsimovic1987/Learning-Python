class Bobble:
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

    def create_command(self):
        pass

comm1 = Bobble("pfad", "add", "table", user="root")
print(len(comm1))
print(comm1)