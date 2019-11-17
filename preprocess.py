#!/usr/bin/env python


import numpy as np
import cv2
from PIL import Image
import tqdm


img_width = 512
img_height = 512
grid_size = 16 # 16 X 16 grid
X = []
Y = []


img_name = "img-{}-0.png"
annotation_file = "img-{}-0.txt"


#Reading Positive Images
for i in tqdm.tqdm(range(1092)):
    
    img_path = 'Data/positive/' + img_name.format(str(i).rjust(4, '0'))
    annotation_path = 'Data/Annotations/' + annotation_file.format(str(i).rjust(4, '0'))
    
    img = Image.open(img_path)
    img = img.resize((img_width, img_height))
    img = np.asarray(img)
    
    file = open(annotation_path)
    
    #format of annotation file
    #class center_x center_y width height
    #1 0.602778 0.606771 0.230556 0.772569
    
    output = np.zeros((grid_size,grid_size,1,5))

    for line in file:
        l = line.split()
        l = [float(i) for i in l]

        x = l[1]
        y = l[2]
        x = x * grid_size
        y = y * grid_size

        w = l[3]
        h = l[4]

        output[int(y), int(x), 0, 0] = 1
        output[int(y), int(x), 0, 1] = x - int(x)
        output[int(y), int(x), 0, 2] = y - int(y)
        output[int(y), int(x), 0, 3] = w
        output[int(y), int(x), 0, 4] = h
    
    X.append(img)
    Y.append(output)


#reading Negative Images
for i in tqdm.tqdm(range(192)):
    
    img_path = 'Data/negative/' + img_name.format(str(i).rjust(3, '0'))
    
    img = Image.open(img_path)
    img = img.resize((img_width, img_height))
    img = np.asarray(img)
    
    output = np.zeros((grid_size,grid_size,1,5))

    X.append(img)
    Y.append(output)


X = np.array(X)
Y = np.array(Y)

np.save('X.npy', X)
np.save('Y.npy', Y)

