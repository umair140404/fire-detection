import glob
import random
import shutil
import os

NUMBER_OF_IMAGES = 60

smoke_paths = []

for path in glob.glob("Dataset/Testing/smoke-large/*"):
    smoke_paths.append(path)

print(len(smoke_paths))

random.shuffle(smoke_paths)
smoke_paths = smoke_paths[0:NUMBER_OF_IMAGES]

for src in smoke_paths:
    filename = src.split("\\")[1]
    dst = "Dataset/Testing/smoke\\" + filename
    shutil.copy(src, dst)

print("END")
