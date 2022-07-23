import glob
import cv2

smoke_paths = []
count = 0

for path in glob.glob("Testing/New Folder/*"):
    smoke_paths.append(path)

print(len(smoke_paths))

for path in smoke_paths:
    image = cv2.imread(path)
    image = cv2.resize(image, (250, 250))
    cv2.imwrite(f"Testing/nofire/{count}.jpg", image)
    count += 1
