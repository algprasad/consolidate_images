#!/usr/bin/env python3

import cv2
import numpy as np
import os
from shutil import copyfile

dir_name_prefix='/home/alg/Downloads/vsr-duf-results/'
dst_dir = 'consolidated_images'
os.mkdir(dst_dir)
global_image_index  = 0
for dir_index in range(1,16):
    dir_name=dir_name_prefix + 'exp' + str(dir_index) + '/'
    for image_index in range(1, 51): # for a total of 51 images as it starts from 1
        #note that the image names are like Frame001.png
        image_index_3_width = str(image_index).zfill(3)
        print(image_index_3_width)
        image_name = dir_name + 'Frame' +  image_index_3_width + '.png'
        dst_filename = dst_dir + '/' + 'Frame' + str(global_image_index) + '.png'
        copyfile(image_name, dst_filename )
        global_image_index+=1

print('All files copied to' + dst_dir)
