# -*- coding: utf-8 -*-

import os
import pandas as pd 

PATH = 'C:\\Code\\Thesis\\LoGAN\\results\\'
VERBOSE = True


count = 0
folders = ['black','blue','brown', 'cyan','gray', 'green','orange','pink','purple','red','white','yellow']

with open('confusion_matrix_second_color_epoch_400.csv', 'w') as the_file:
        the_file.write('Class;black;blue;brown;cyan;gray;green;orange;pink;purple;red;white;yellow')
         
for folder in folders:
    os.chdir(PATH)
    if VERBOSE:
        print('\n' + folder)
    colors = pd.read_csv('colors-sorted-english-'+folder+'.csv', sep=';')    
   
    color_count_1st = {'black': 0, 'blue': 0, 'brown': 0, 'cyan': 0, 'gray': 0, 'green':0, 'orange':0, 'pink':0, 'purple':0, 'red':0, 'white':0, 'yellow':0}

    for row in range(25936, 26000):
        color_count_1st[colors['compact middle'][row]] += 1
      
             
    with open('C:\\Code\\Thesis\\AC-WGAN-GP_from_vm\\results\\confusion_matrix_second_color_epoch_400.csv', 'a') as the_file:
        the_file.write('\n' + folder )
        for i in range(0,12):
            the_file.write(';' + str(color_count_1st[folders[i]]))
            
       
    
        