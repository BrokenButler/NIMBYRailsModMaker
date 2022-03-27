import os

from mod import TrackMod
from trackmod.track_kind import TrackKind
from trackmod.track_layer import TrackLayer
from utils import TrackLayers


def main():
    mod = TrackMod(name='Moar Speeds!', author='BrokenButler', version='1.0.0',
                   description='Adds tracks ranging from 10 to 600km/h (10km/h increments)')

    id_template = "BB_track_"
    for i in range(10, 601, 10):
        full_id = id_template + str(i)
        tk: TrackKind = TrackKind(track_kind_id=f"{full_id}", name_loc=f"{full_id}_name", name_en=f"{i}km/h")
        for layer in TrackLayers:
            tl: TrackLayer = TrackLayer(tk.track_kind_id, layer, max_speed=i, price=1000)
            tk.add_track_layer(tl)
        mod.add_track_kind(tk)
    os.mkdir(f"./output/{mod.name}")
    mod.export(file_path=f"./output/{mod.name}/mod.txt")


if __name__ == '__main__':
    main()
