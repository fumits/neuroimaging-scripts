# This script was described for Siemens Skyra 3.0T at the Jikei University Hospital (JUH) by Fumitoshi Kodaka from Department of Psychiatry.
# PACS at JUH devide all the MR data into two folders, thus you may be irritable to rename and copy these numerous DICOM files in each folder.
# This script resolve the problem. You can get all the renamed files in a newly created folder "DICOM_renamed_all".
# Please rename second original folder "000000" in each DICOM folder to "000001", and you have "000000" and "000001" in one folder.
# Then you execute dicom_rename_JUH_Skyra.py. Enjoy!

import os, glob
from distutils.dir_util import copy_tree

if os.path.exixts('./000000') and os.path.exists('./000001'):
    
    file_name_folder1 = glob.glob('./000000/*')
    file_name_folder2 = glob.glob('./000001/*')

    file_list_folder1,file_name_folder2 = [],[]
    i,j = 0,0

    for i in file_name_folder1:
        os.rename(i,os.path.join('./000000/','1'+os.path.basename(i)))

    for j in file_name_folder2:
        os.rename(j,os.path.join('./000001/','2'+os.path.basename(j)))

    os.makedir('./DICOM_renamed_all')
    copy_tree('./000000','./DICOM_renamed_all')
    copy_tree('./000000','./DICOM_renamed_all')

else:
    print('No apopropriate directories: please rename your Jikei DICOM folder to 000000 and 000001')



