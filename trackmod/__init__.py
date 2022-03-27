from collections.abc import Iterator

from mod import Mod
from trackmod.track_kind import TrackKind


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
        for tkind in self.track_kinds:
            string += f"{tkind.__str__()}\n\n"
        return string

    def get_track_kind(self, track_kind_id: str) -> TrackKind:
        for tkind in self.track_kinds:
            if tkind.track_kind_id == track_kind_id:
                return tkind
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
