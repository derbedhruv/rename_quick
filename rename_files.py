# This is a very simple utility to rename files
# Here it is being used to rename all the files in the folder into .dcm
# Remember that none of these files have any extension and there are no other filetypes in this folder.
# Should you need to use this, make appropriate modifications
import os,sys

folder = "./DICOM/"	# We assume this file is one level above the folder

for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       newname = infilename + ".dcm"
       output = os.rename(infilename, newname)
