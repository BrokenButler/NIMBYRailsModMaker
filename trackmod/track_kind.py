from collections.abc import Iterable

from trackmod.track_layer import TrackLayer
from utils import TrackLayers


class TrackKind:
    def __init__(self, track_kind_id: str, name_loc: str, name_en: str, tags: list[str] = None,
                 track_layers: list[TrackLayer] = None, schema: int = 1):
        self.schema: int = schema
        self.track_kind_id: str = track_kind_id
        self.name_loc: str = name_loc
        self.name_en: str = name_en
        self.tags: list[str] | None = tags
        self.track_layers: list[TrackLayer] = track_layers if track_layers is not None else []

    def __str__(self):
        self.validate()
        string = f";----------------------------------------\n" \
                 f";------------{self.name_en}\n" \
                 f";----------------------------------------\n" \
                 f"[TrackKind]\n" \
                 f"schema={self.schema}\n" \
                 f"id={self.track_kind_id}\n" \
                 f"name_loc={self.name_loc}\n" \
                 f"name_en={self.name_en}\n"
        if self.tags is not None:
            string += f"tags={self.tags}\n"
        string += f"\n"
        for track_layer in self.track_layers:
            string += f"{track_layer}\n"
        return string

    def get_track_layer(self, layer: TrackLayers) -> TrackLayer:
        for track_layer in self.track_layers:
            if track_layer.layer == layer:
                return track_layer
        raise ValueError(f"Layer type {layer} not found")

    def get_all_track_layers(self) -> list[TrackLayer]:
        return self.track_layers

    def _remove_track_layer(self, layer: TrackLayers) -> None:
        try:
            self.track_layers.remove(self.get_track_layer(layer))
        except ValueError:
            pass

    def add_track_layer(self, new_track_layer: TrackLayer) -> None:
        self._remove_track_layer(new_track_layer.layer)
        self.track_layers.append(new_track_layer)

    def add_track_layers(self, new_track_layers: Iterable[TrackLayer]) -> None:
        for new_track_layer in new_track_layers:
            self.add_track_layer(new_track_layer)
            return

    def validate(self) -> None:
        if self.track_kind_id is None:
            raise ValueError("TrackKind.id is None")
        if self.name_loc is None:
            raise ValueError("TrackKind.name_loc is None")
        if self.name_en is None:
            raise ValueError("TrackKind.name_en is None")
