import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mp_image
# required magic to display matplotlib plots in notebooks
%matplotlib inline

source_folder = "J:/edX"

#set a fig of an appropriate size
fig = plt.figure(figsize = (6,6))

#os.walk function take you to the dir and find all the folder there and also data inside the folder.
for root,folders,filenames in os.walk(source_folder):
    image_num = 0
    num_folders = len(folders)
    for folder in folders:
        image_num +=1
        # os.listdir(path) return the list contain the entity in the given path
        # os.path.join function join the first argument to another and so on by anly one '/' forward slash.  
        # the below line give the intity name inside a folder i.e a picture having name '1.jpg' 
        # so it just return the name of the image and the [] define that which entity we are looking for 
        file_name = os.listdir(os.path.join(root,folder))[0]
        # The below line give the entire path of the entity
        file_path = os.path.join(root,folder,file_name)
        image = mp_image.imread(file_path)
        # fig.add_subplot(111) mean 1x1 at 1st grid
        a=fig.add_subplot(num_folders, 1, image_num)
        image_plot = plt.imshow(image)
        
plt.show()        
    