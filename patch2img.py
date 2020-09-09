import h5py
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
from pathlib import Path


def main():
    for phase in ["train", "valid", "test"]:
        if not (Path(phase)/"x").exists():
            (Path(phase)/"x").mkdir(parents=True)

        print(f"[{phase} : X]")
        file_x = h5py.File(f"camelyonpatch_level_2_split_{phase}_x.h5", "r")
        data_x = file_x['x']
        for idx, img in tqdm(enumerate(data_x), total=len(file_x["x"])):
            cv2.imwrite(f"{phase}/x/{idx:06}.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

        print(f"[{phase} : Y]")
        file_y = h5py.File(f"camelyonpatch_level_2_split_{phase}_y.h5", "r")
        data_y = file_y['y']
        out = np.zeros(data_y.shape, dtype=np.uint8)
        data_y.read_direct(out)
        pd.DataFrame(out.ravel()).to_csv(f"{phase}/y.csv", header=None, index=None)


if __name__ == '__main__':
    main()
