# -*- coding: utf-8 -*-
import os
import sys
import re
import pandas as pd
import webcolors

PATH = 'C:\\Code\\Thesis\\LoGAN\\'
TRAINING = True
VERBOSE = True

if TRAINING:
    folders = ['data']
else:
    folders = ['green', 'purple', 'white', 'brown', 'blue', 'cyan', 'yellow', 'gray', 'red',  'pink', 'orange', 'black']
    PATH = PATH + 'results\\'


os.chdir(PATH)

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
    return closest_name

def get_shade(color_name):

    if color_name == 'darkolivegreen' or color_name == 'olive' or color_name == 'olivedrab' or color_name == 'yellowgreen' or color_name == 'limegreen' or color_name == 'lime' or color_name == 'lawngreen' or color_name == 'chartreuse' or color_name == 'greenyellow' or color_name == 'springgreen' or  color_name == 'mediumspringgreen' or color_name == 'lightgreen' or color_name == 'palegreen' or color_name == 'darkseagreen' or color_name == 'mediumaquamarine' or  color_name == 'mediumseagreen' or color_name == 'seagreen' or color_name == 'forestgreen' or color_name == 'green' or color_name == 'darkgreen':
        shade =  'green'
    
    elif color_name == 'lavender' or color_name == 'thistle' or color_name == 'plum' or color_name == 'violet' or color_name == 'orchid' or color_name == 'fuchsia' or color_name == 'magenta' or color_name == 'mediumorchid' or color_name == 'mediumpurple' or color_name == 'blueviolet' or  color_name == 'darkviolet' or color_name == 'darkorchid' or color_name == 'darkmagenta' or color_name == 'purple' or color_name == 'indigo' or  color_name == 'darkslateblue' or color_name == 'slateblue' or color_name == 'mediumslateblue':
        shade =  'purple'
    
    elif color_name == 'white' or color_name == 'snow' or color_name == 'honeydew' or color_name == 'mintcream' or color_name == 'azure' or color_name == 'aliceblue' or color_name == 'ghostwhite' or color_name == 'whitesmoke' or color_name == 'seashell' or color_name == 'beige' or  color_name == 'oldlace' or color_name == 'floralwhite' or color_name == 'ivory' or color_name == 'aquawhite' or color_name == 'linen' or  color_name == 'lavenderblush' or color_name == 'mistyrose' or color_name == 'antiquewhite':
        shade =  'white'
    
    elif color_name == 'cornsilk' or color_name == 'blanchedalmond' or color_name == 'bisque' or color_name == 'navajowhite' or color_name == 'wheat' or color_name == 'burlywood' or color_name == 'tan' or color_name == 'rosybrown' or color_name == 'sandybrown' or color_name == 'goldenrod' or  color_name == 'darkgoldenrod' or color_name == 'peru' or color_name == 'chocolate' or color_name == 'saddlebrown' or color_name == 'sienna' or  color_name == 'brown' or color_name == 'maroon':
        shade =  'brown'
        
    elif color_name == 'lightsteelblue' or color_name == 'powderblue' or color_name == 'lightblue' or color_name == 'skyblue' or color_name == 'lightskyblue' or color_name == 'deepskyblue' or color_name == 'dodgerblue' or color_name == 'cornflowerblue' or color_name == 'steelblue' or color_name == 'royalblue' or  color_name == 'blue' or color_name == 'mediumblue' or color_name == 'darkblue' or color_name == 'navy' or color_name == 'midnightblue':
        shade =  'blue'
        
    elif color_name == 'aqua' or color_name == 'cyan' or color_name == 'lightcyan' or color_name == 'paleturquoise' or color_name == 'aquamarine' or color_name == 'turquoise' or color_name == 'mediumturquoise' or color_name == 'darkturquoise' or color_name == 'lightseagreen' or color_name == 'cadetblue' or  color_name == 'darkcyan' or color_name == 'teal':
        shade =  'cyan'   
        
    elif color_name == 'yellow' or color_name == 'lightyellow' or color_name == 'lemonchiffon' or color_name == 'lightgoldenrodyellow' or color_name == 'papayawhip' or color_name == 'moccasin' or color_name == 'peachpuff' or color_name == 'palegoldenrod' or color_name == 'khaki' or color_name == 'darkkhaki' or  color_name == 'gold':
        shade =  'yellow'        
                
    elif color_name == 'gainsboro' or color_name == 'lightgrey' or color_name == 'silver' or color_name == 'darkgrey' or color_name == 'grey' or color_name == 'dimgrey' or color_name == 'lightslategrey' or color_name == 'darkslategrey' or color_name == 'slategrey':
        shade =  'gray'
        
    elif color_name == 'lightgray' or color_name == 'darkgray' or color_name == 'gray' or color_name == 'dimgray' or color_name == 'lightslategray' or color_name == 'darkslategray' or color_name == 'slategray':
        shade =  'gray'
        
    elif color_name == 'lightsalmon' or color_name == 'salmon' or color_name == 'darksalmon' or color_name == 'lightcoral' or color_name == 'indianred' or color_name == 'crimson' or color_name == 'firebrick' or color_name == 'darkred' or color_name == 'red' :
        shade =  'red'
        
    elif color_name == 'pink' or color_name == 'lightpink' or color_name == 'hotpink' or color_name == 'deeppink' or color_name == 'palevioletred' or color_name == 'mediumvioletred':
        shade = 'pink'
        
    elif color_name == 'orangered' or color_name == 'tomato' or color_name == 'coral' or color_name == 'darkorange' or color_name == 'orange':
        shade = 'orange'
    
    elif color_name == 'black':
        shade = 'black'
    
    else:
        shade = 'unknown'
        
    return shade


def one_hot_encode(data, folder):
    one_hot_encoding = pd.DataFrame(columns = ['image','green', 'purple', 'white', 'brown', 'blue', 'cyan', 'yellow', 'gray', 'red',  'pink', 'orange', 'black']) 
    
    one_hot_encoding['image'] = data['file name']
    
    for img in data.index:
        if data['compact most'][img] == 'green':
            one_hot_encoding['green'][img] = 1
        elif data['compact most'][img] == 'purple':
            one_hot_encoding['purple'][img] = 1
        elif data['compact most'][img] == 'white':
            one_hot_encoding['white'][img] = 1
        elif data['compact most'][img] == 'brown':
            one_hot_encoding['brown'][img] = 1
        elif data['compact most'][img] == 'blue':
            one_hot_encoding['blue'][img] = 1
        elif data['compact most'][img] == 'cyan':
            one_hot_encoding['cyan'][img] = 1
        elif data['compact most'][img] == 'yellow': 
            one_hot_encoding['yellow'][img] = 1
        elif data['compact most'][img] == 'gray':
            one_hot_encoding['gray'][img] = 1
        elif data['compact most'][img] == 'red':
            one_hot_encoding['red'][img] = 1
        elif data['compact most'][img] == 'pink': 
            one_hot_encoding['pink'][img] = 1
        elif data['compact most'][img] == 'orange':
            one_hot_encoding['orange'][img] = 1
        elif data['compact most'][img] == 'black':
            one_hot_encoding['black'][img] = 1
        
    one_hot_encoding.fillna(0, inplace=True)
    
    one_hot_encoding.drop(one_hot_encoding.columns[0], axis=1, inplace= True)
    one_hot_encoding.to_csv(folder +'\\one_hot_encoding_color_icon.csv', index = False, header = False)
    




for folder in folders:
    os.chdir(PATH)

    if VERBOSE:
        print('\n' + folder)

    if TRAINING:
        colors = pd.read_csv('colors.csv', sep = ';')
    else:
        colors = pd.read_csv('color_'+folder+'.csv', sep = ';')   
    
    #read the lists in the csv
    color_rgb = []
    color_amount = []
    cnt = 0
    for img in colors.index:
        color_rgb.append([[float(_.group(0)) for _ in re.finditer(r"\d{1,3}[.]\d{0,8}", i)] for i in colors['colors'].iloc[img].split(',')])
        color_amount.append([float(_.group(0)) for _ in re.finditer(r"\d{1,3}[.]\d{0,8}", colors['amount color'].iloc[img])])
        cnt+=1
        if VERBOSE: 
                if TRAINING:
                    sys.stdout.write("Progress: {:.2%}\r".format(cnt/485377))
                    sys.stdout.flush()
                else:
                    sys.stdout.write("Progress: {:.2%}\r".format(cnt/26000))
                    sys.stdout.flush()            
            
    colors['colors'] = color_rgb
    colors['amount color'] = color_amount

    if VERBOSE:
        print("\nFormat change complete.")

    
    #match color RGB to real word
    list_colors_3 = []
    list_compact_3 = []
    cnt = 0 
    for color in colors['colors']:
        list_colors = []
        list_colors_compact = []
        for i in range(0,3):
            #get real name of color
            color_name = get_colour_name(color[i])
            list_colors.append(color_name)
            #get one of 12 shades/classes
            list_colors_compact.append(get_shade(color_name))
        list_colors_3.append(list_colors)
        list_compact_3.append(list_colors_compact)
        cnt+=1
        if VERBOSE:
            if TRAINING:
                    sys.stdout.write("Progress: {:.2%}\r".format(cnt/485377))
                    sys.stdout.flush()
                else:
                    sys.stdout.write("Progress: {:.2%}\r".format(cnt/26000))
                    sys.stdout.flush()    
    colors['color word'] = list_colors_3  
    colors['color word compact'] = list_compact_3
    
    if VERBOSE:
        print("\nColor word match complete.")   

    '''
    Sort the color list:
    '''
    word_least = []     # 3rd place for actual color
    word_middle = []    # 2nd place for actual color
    word_most = []      # 1st place for actual color
    compact_least = []  # 3rd place for shace/class 
    compact_middle = [] # 2nd place for shace/class 
    compact_most = []   # 1st place for shace/class 
    for img in colors.index:
        #sort according to amount of color
        color_word_sorted=[x for _,x in sorted(zip(colors['amount color'][img],colors['color word'][img]))]
        word_least.append(color_word_sorted[0])
        word_middle.append(color_word_sorted[1])
        word_most.append(color_word_sorted[2])
        #sort according to amount of color
        color_word_compact_sorted = [x for _,x in sorted(zip(colors['amount color'][img],colors['color word compact'][img]))]
        compact_least.append(color_word_compact_sorted[0])
        compact_middle.append(color_word_compact_sorted[1])
        compact_most.append(color_word_compact_sorted[2])        
        
    colors.drop(colors.columns[[2,3]], axis=1, inplace= True )
    colors['word least'] = word_least
    colors['word middle'] = word_middle
    colors['word most'] = word_most
    colors['compact least'] = compact_least
    colors['compact middle'] = compact_middle
    colors['compact most'] = compact_most

   

    if TRAINING:
        one_hot_encode(colors, folder)
    else:
        colors.to_csv('colors-sorted-english-'+folder+'.csv', sep=';')



   