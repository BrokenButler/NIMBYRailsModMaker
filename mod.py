class Mod:
    def __init__(self, schema: int = 1, name: str = "Example Mod", author: str = "BrokenButler's Mod Maker",
                 version: str = "1.0.0", description: str = "Example description"):
        self.schema = schema
        self.name = name
        self.author = author
        self.version = version
        self.description = description

    def __str__(self):
        return f"[ModMeta]\n" \
               f"schema={self.schema}\n" \
               f"name={self.name}\n" \
               f"author={self.author}\n" \
               f"version={self.version}\n" \
               f"description={self.description}\n"

    def export(self, file_path: str = "mod.txt") -> None:
        with open(file_path, "w") as f:
            f.write(self.__str__())
