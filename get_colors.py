# -*- coding: utf-8 -*-

import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans


PATH = 'C:\\Code\\Thesis\\LoGAN\\'
TRAINING = True
VERBOSE = True

if TRAINING:
    folders = ['data']
else:
    folders = ['green', 'purple', 'white', 'brown', 'blue', 'cyan', 'yellow', 'gray', 'red',  'pink', 'orange', 'black']
    PATH = PATH + 'results\\'

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


cnt= 0                    
for folder in folders:
    os.chdir(PATH + folder)

    if TRAINING:
        with open(PATH+'colors.csv', 'w') as the_file:
            the_file.write('file name;colors;amount color')
    else:
        with open(PATH+'results\\color_' + folder + '.csv', 'a') as the_file:
            the_file.write('file name;colors;amount color')


    if VERBOSE:
        print('\n' + folder)

    for fn in os.listdir('.'):
         if os.path.isfile(fn):
            if VERBOSE: 
                if TRAINING:
                    sys.stdout.write("Progress: {:.2%}\r".format(cnt/485377))
                    sys.stdout.flush()
                else:
                    sys.stdout.write("Progress: {:.2%}\r".format(cnt/26000))
                    sys.stdout.flush()            
            
            cnt += 1
            
            #read image
            img = cv2.imread(fn)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #represent as row*column,channel number
            img = img.reshape((img.shape[0] * img.shape[1],3)) 
            
            #find 3 clusters
            clt = MiniBatchKMeans(n_clusters=3)             
            clt.fit(img)
            
            hist = find_histogram(clt)
            
            #visualise colors of centroids
            # bar = plot_colors2(hist, clt.cluster_centers_)           
            # plt.axis("off")
            # plt.imshow(bar)
            # plt.show()
            
            if TRAINING:
                with open(PATH+'colors.csv', 'a') as the_file:
                    the_file.write('\n' + str(fn) + ';' + str(clt.cluster_centers_[0]) + ',' + str(clt.cluster_centers_[1]) + ',' + str(clt.cluster_centers_[2]) + ';' + str(hist))
            else:
                with open(PATH+'results\\color_' + folder + '.csv', 'a') as the_file:
                    the_file.write('\n' + str(fn) + ';' + str(clt.cluster_centers_[0]) + ',' + str(clt.cluster_centers_[1]) + ',' + str(clt.cluster_centers_[2]) + ';' + str(hist))
                
            
        
        
        
        
        