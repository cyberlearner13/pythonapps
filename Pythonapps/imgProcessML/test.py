import cv2

file = open("cv2dir.txt","w+")

modules = dir(cv2)

for module in modules:
    file.write(module + "\n")

file.close()
