from utils import TrackLayers, TrackModes


class TrackMode:
    def __init__(self, track_kind_id: str, layer: TrackLayers, mode: TrackModes, border: str = None, base: str = None,
                 sleepers: str = None, rails: str = None, schema: int = 1):
        self.schema: int = schema
        self.track_kind_id: str = track_kind_id
        self.layer: TrackLayers = layer
        self.mode: TrackModes = mode
        self.border: str = border
        self.base: str = base
        self.sleepers: str = sleepers
        self.rails: str = rails

    def __str__(self) -> str:
        self.validate()
        string = f";----{self.mode.value}\n" \
                 f"[TrackMode]\n" \
                 f"schema={self.schema}\n" \
                 f"track_kind_id={self.track_kind_id}\n" \
                 f"layer={self.layer}\n" \
                 f"mode={self.mode.value}\n"
        if self.border is not None:
            string += f"border={self.border}\n"
        if self.base is not None:
            string += f"base={self.base}\n"
        if self.sleepers is not None:
            string += f"sleepers={self.sleepers}\n"
        if self.rails is not None:
            string += f"rails={self.rails}\n"
        return string

    def validate(self):
        if self.track_kind_id is None:
            raise ValueError("TrackMode.track_kind_id is None")
        if self.layer is None:
            raise ValueError("TrackMode.layer is None")
        if self.mode is None:
            raise ValueError("TrackMode.mode is None")


def default_track_mode_list(track_kind_id: str, layer: TrackLayers, max_speed: int = None) -> list[TrackMode]:
    track_mode_list = []
    sleepers = None
    for tm in TrackModes:
        if max_speed <= 160:
            if tm in [TrackModes.BUILT, TrackModes.BUILT_BRANCH, TrackModes.BUILT_DIAMOND]:
                sleepers = f"@stock/common/sleepers2.png"
            elif tm in [TrackModes.BLUEPRINT, TrackModes.BLUEPRINT_BRANCH, TrackModes.BLUEPRINT_DIAMOND]:
                sleepers = f"@stock/common/sleepers2_bp.png"
            else:
                sleepers = None

        track_mode_list.append(TrackMode(track_kind_id, layer, tm, sleepers=sleepers))
    return track_mode_list
