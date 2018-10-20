# -*- coding: utf-8 -*-

import csv
import glob
import os
import sys

import numpy as np
import tensorflow as tf
from PIL import Image

Data_PATH = 'C:\\Code\\Thesis\\LoGAN\\data\\logos' 
label_csv_PATH = 'C:\\Code\\Thesis\\LoGAN\\data\\one_hot_encoding_color_icon.csv' 


# Parameters
IMAGE_SIZE = 32
IMAGE_SHAPE = [IMAGE_SIZE, IMAGE_SIZE, 3] # 3 is number of channels
CATEGORIES = ['green', 'purple', 'white', 'brown', 'blue', 'cyan', 'yellow', 'gray', 'red',  'pink', 'orange', 'black'] # the different classes for the one-hot encoding
num_classes = len(CATEGORIES)
BATCH_SIZE = 64 # used in example in the end
VERBOSE = True 


def read_labels_from(path=label_csv_PATH):
    if VERBOSE:
        print('Reading labels ...')
    with open(path, 'r') as label_file:
        data_iter = csv.reader(label_file)
        train_labels = [data for data in data_iter]

    # pre process labels to int
    train_labels = np.array(train_labels, dtype=np.uint32)

    return train_labels


def read_images_from(path=Data_PATH):
    images = []
    png_files_path = glob.glob(os.path.join(path, '*.[pP][nN][gG]')) # extract all png files
    
    if VERBOSE:
        print("Reading images ...")
    
    cnt=0
    for filename in png_files_path:
        im = Image.open(filename) 
        im = np.asarray(im, np.uint8)

        # get image name, not path
        image_name = filename.split('\\')[-1].split('.')[0]
        images.append([int(image_name), im])
        
        cnt+=1
        if VERBOSE:
            sys.stdout.write("Progress loading images: {:.2%}\r".format(cnt/485377))
            sys.stdout.flush()

    images = sorted(images, key=lambda image: image[0])
      
    images_only = [np.asarray(image[1], np.uint8) for image in images]  
    images_only = np.array(images_only)

    return images_only

'''
if '__main__':
    # Example usage for getting the next batch (together with Dataset)
    from util.dataset import Dataset
  
    images = read_images_from()
    labels = read_labels_from()

    dataset = Dataset(images, labels)

    next_batch_img, next_batch_label = dataset.next_batch(BATCH_SIZE)

    # test conversion to tensorflow tensor
    data_tf = []
    for image in next_batch_img:
        data_tf.append(tf.convert_to_tensor(image))

    sess = tf.InteractiveSession()  
    print(data_tf[0].eval())
    sess.close()
'''


