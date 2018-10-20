# LoGAN user guide

This README will explain how to set-up and run the code for LoGAN: Generating Logos with a Generative Adversarial Neural Network Conditioned on Colour.

# Getting the data and Training the model

  - Download LLD-Icons PNG files from: https://data.vision.ee.ethz.ch/sagea/lld/data/LLD-icon_PNG.zip
  - Set up a Python 3.5 environment with the packages mentioned below
   - Run get_colors.py (change the PATH variable to main directory)   
       - In your current directory a file 'colors.csv' will be created with 3 columns (name of file, top 3 colors in file, amount of each of the top 3 colors)
    - Run change_colors_to_words.py (change path variable to main directory) 
        - A one hot encoding of the colors extracetd previously will be created in the data folder
    - Change the path of the data and the one-hot-encoding csv on read_images.py
    - Run main.py 

# Overview of the files

| File | Function | Parameters
| ------ | ------ |------ |
|get_colors.py| Uses the logos to find RGB centroids for the KMeans clusters for each image (output:colors.csv)| PATH - of working directory, TRAINING - true in training mode, VERBOSE - wether to print details |
|change_colors_to_words.py  | Uses colors.csv to create a one-hot-encoding for the labels (output:one_hot_encoding_color_icon.csv) | PATH - of working directory, TRAINING - true in training mode, VERBOSE - wether to print details
| acgan.py | The class of the ACGAN |
| main.py | The main class. Use this to start training the model and tweak the parameters. | gan_type - only ACWGANGP, dataset - only available dataset lld, epoch - number of epochs to train, batch_size - size of batch to train, z_dim - dimension of noise vector, checkpoint_dir-to save checkpoint, result_dir-directory to save results, log_dir-tensorboard log directory
| ops.py | Defines the layers. | 
| utils.py| Defines useful functions. | 
| read_images.py| Defines two methods, to read images, and labels in one hot encoding format. | Data_PATH, label_csv_PATH, IMAGE_SIZE - size of the images, CATEGORIES - classes, BATCH_SIZE - size of batch, VERBOSE - wether to print details
| make_confusion_matrix.py | Used to get the confusion matrix to get the results as in paper. | 


# Necessary packages
Python 3.5
tensorflow (1.4+)
numpy (1.13.1 and 1.14.1)
PIL (pillow) (5.1.0)
pandas (0.20.3)
webcolors (1.8.1)
scikit-learn (0.19.0)
matplotlib (2.12.2)
cv2 (opencv-python) (3.4.0.12)

