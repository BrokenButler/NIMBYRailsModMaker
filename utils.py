from enum import Enum


class TrackModes(Enum):
    BUILT = "built"
    BUILT_BRANCH = "built_branch"
    BUILT_DIAMOND = "built_diamond"
    BLUEPRINT = "blueprint"
    BLUEPRINT_BRANCH = "blueprint_branch"
    BLUEPRINT_DIAMOND = "blueprint_diamond"


class TrackLayers(Enum):
    VIADUCT = "viaduct"
    GROUND = "ground"
    TUNNEL = "tunnel"
