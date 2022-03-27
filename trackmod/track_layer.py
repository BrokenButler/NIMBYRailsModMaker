from collections.abc import Iterable

from trackmod.track_mode import TrackMode, default_track_mode_list
from enums import TrackLayers, TrackModes


class TrackLayer:
    def __init__(self, track_kind_id: str, layer: TrackLayers, max_speed: int, price: int,
                 angle_speed_factor: float = 5.21, station_price_mul: float = 10, depot_price_mul: float = 25,
                 crossing_price: int = 125000, collides_ways: bool = True, conflicts_tracks: bool = False,
                 track_modes: list[TrackMode] = None, schema: int = 1):
        self.schema: int = schema
        self.track_kind_id: str = track_kind_id
        self.layer: TrackLayers = layer
        if max_speed < 10 or max_speed > 600:
            raise ValueError("max_speed must be between 10 and 600")
        self.max_speed: int = max_speed
        if price < 1000 or price > 10000000000:
            raise ValueError("price must be between 1000 and 10000000000")
        self.price: int = price
        if angle_speed_factor < 0.1 or angle_speed_factor > 100:
            raise ValueError("angle_speed_factor must be between 0.1 and 100")
        self.angle_speed_factor: float = angle_speed_factor
        if station_price_mul < 1 or station_price_mul > 1000:
            raise ValueError("station_price_mul must be between 1 and 1000")
        self.station_price_mul: float = station_price_mul
        if depot_price_mul < 1 or depot_price_mul > 1000:
            raise ValueError("depot_price_mul must be between 1 and 1000")
        self.depot_price_mul: float = depot_price_mul
        if crossing_price < 1000 or crossing_price > 1000000000:
            raise ValueError("crossing_price must be between 1000 and 1000000000")
        self.crossing_price: int = crossing_price
        self.collides_ways: bool = collides_ways
        self.conflicts_tracks: bool = conflicts_tracks
        if track_modes is not None:
            self.track_modes = track_modes
        else:
            self.track_modes = default_track_mode_list(track_kind_id, layer)

    def __str__(self):
        self.validate()
        string = f";----------------------------\n" \
                 f";--------{self.layer.value}\n" \
                 f";----------------------------\n" \
                 f"[TrackLayer]\n" \
                 f"schema={self.schema}\n" \
                 f"track_kind_id={self.track_kind_id}\n" \
                 f"layer={self.layer.value}\n" \
                 f"max_speed={self.max_speed}\n" \
                 f"price={self.price}\n"
        if self.angle_speed_factor is not None:
            string += f"angle_speed_factor={self.angle_speed_factor}\n"
        if self.station_price_mul is not None:
            string += f"station_price_mul={self.station_price_mul}\n"
        if self.depot_price_mul is not None:
            string += f"depot_price_mul={self.depot_price_mul}\n"
        if self.crossing_price is not None:
            string += f"crossing_price={self.crossing_price}\n"
        if self.collides_ways is not None:
            string += f"collides_ways={self.collides_ways}\n"
        if self.conflicts_tracks is not None:
            string += f"conflicts_tracks={self.conflicts_tracks}\n"
        for track_mode in self.track_modes:
            string += f"{track_mode}"
        return string

    def get_track_mode(self, mode: TrackModes) -> TrackMode:
        for track_mode in self.track_modes:
            if track_mode.mode == mode:
                return track_mode
        raise ValueError(f"Track mode {mode} not found")

    def get_all_track_modes(self) -> list[TrackMode]:
        return self.track_modes

    def _remove_track_mode(self, mode: TrackModes):
        try:
            self.track_modes.remove(self.get_track_mode(mode))
        except ValueError:
            pass

    def add_mode(self, track_mode: TrackMode):
        self._remove_track_mode(track_mode.mode)
        self.track_modes.append(track_mode)

    def add_modes(self, track_modes: Iterable[TrackMode]) -> None:
        for track_mode in track_modes:
            self.add_mode(track_mode)

    def validate(self):
        if self.track_kind_id is None:
            raise ValueError("TrackLayer.track_kind_id is None")
        if self.layer is None:
            raise ValueError("TrackLayer.layer is None")
        if self.max_speed is None:
            raise ValueError("TrackLayer.max_speed is None")
        if self.price is None:
            raise ValueError("TrackLayer.price is None")
