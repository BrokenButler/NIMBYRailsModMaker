from collections.abc import Iterator

from trackmod.track_kind import TrackKind


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


class TrackMod(Mod):
    def __init__(self, schema: int = 1, name: str = "Example Mod", author: str = "BrokenButler's Mod Generator",
                 version: str = "1.0.0", description: str = "Example description", track_kinds: list[TrackKind] = None):
        super().__init__(schema, name, author, version, description)
        if track_kinds is not None:
            self.track_kinds = track_kinds
        else:
            self.track_kinds = []

    def __str__(self):
        string: str = f"{super().__str__()}\n"
        for track_kind in self.track_kinds:
            string += f"{track_kind.__str__()}\n\n"
        return string

    def get_track_kind(self, track_kind_id: str) -> TrackKind:
        for track_kind in self.track_kinds:
            if track_kind.track_kind_id == track_kind_id:
                return track_kind
        raise ValueError(f"Track kind with id {track_kind_id} not found")

    def get_all_track_kinds(self) -> list[TrackKind]:
        return self.track_kinds

    def remove_track_kind(self, track_kind_id: str) -> None:
        try:
            self.track_kinds.remove(self.get_track_kind(track_kind_id))
        except ValueError:
            pass

    def add_track_kind(self, new_track_kind: TrackKind) -> None:
        self.remove_track_kind(new_track_kind.track_kind_id)
        self.track_kinds.append(new_track_kind)

    def add_track_kinds(self, new_track_kinds: Iterator[TrackKind]) -> None:
        for new_track_kind in new_track_kinds:
            self.add_track_kind(new_track_kind)

    def export(self, file_path: str = "mod.txt") -> None:
        with open(file_path, "w") as f:
            f.write(self.__str__())
