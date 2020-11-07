import xml.etree.ElementTree as ET

from glob import glob
import os
#from tqdm import tqdm

def function(x,new):
    """
    Function to add element "new" in each xml filename and the filename 
        element for corresponding image name
    ----------
    x : name of xml folder 
    new : new variable i.e supposed to be added to each imagename and xml filename

    Returns
    -------
    None.

    """
    for data in glob(x):
        file = data
        tree=ET.parse(data)
        root=tree.getroot()
        
        for child in root:
            
            if child.tag == "filename":
                child.text = new + child.text
                
        with open(data,"wb") as text_file:
            tree.write(text_file)
        
        new_name = os.path.join(os.path.split(data)[0], new + os.path.split(data)[1])
        os.rename(file,new_name)
        # break
        
if __name__ == '__main__':
    
    dir_ann = r"C:\Users\Administrator\Desktop\images\New folder (2)" #annotaion directory
    dir_img =r"C:\Users\Administrator\Desktop\images\New folder (2)" #images directory
    new_element = "new_" #new variable i.e supposed to be added to each image and xml file name
    
    print(" Renaming xml files...\n")
    function(os.path.join(dir_ann,"*.xml"),new_element)
    #"""
    print("\n Renaming image files...\n")
    for img in glob(os.path.join(dir_img,"*.jpg")):
        # rename each image filename by adding element "new_element"
        new_img = os.path.join(os.path.split(img)[0],new_element+os.path.split(img)[1])
        os.rename(img,new_img)
        
    print("\n All files are renamed successfully !!!")