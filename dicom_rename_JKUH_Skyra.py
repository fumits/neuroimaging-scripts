# This script was described for Siemens Skyra 3.0T at JKUH.
# PACS at JKUH devide all the MR data into multiple folders.
# This script resolve the problem. You can get all the renamed files in a newly created folder "all_dicoms".
# Rename DICOM folder copied from each DVD-ROM (originally named "DICOM") to such as "DICOM_1", "DICOM_2"...
# Copy these renamed "DICOM" folders and this script to a directory.
# When you run it, it creates "all_dicoms" folder in which all the renamed DICOM files.

import os, glob, tkinter.filedialog
from distutils.dir_util import copy_tree

dir = tkinter.filedialog.askdirectory()
os.chdir(dir)

os.mkdir('./all_dicoms')
dicom_folder = sorted(glob.glob('./DICOM_*'))

i,j = 0,0
count = 1
for i in dicom_folder:
    file_names = glob.glob(i+'/00000000/*')
    file_folders = i+'/00000000/'
    for j in file_names:
        os.rename(j,os.path.join(file_folders,str(count)+os.path.basename(j)))
    copy_tree(file_folders,'./all_dicoms')
    count = count+1