# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:16:15 2020

@author: Mohammad Saroughi
"""
#for install PIL : pip install Pillow
from PIL import Image
import imagehash
import argparse

def Image_Hash(Path_Current__Image,Path_Previous__Image,path):
    
    
    try:  
        Current_Image = Image.open(Path_Current__Image)
        Previous_Image = Image.open(Path_Previous__Image)
      
        hash_1 = imagehash.average_hash(Current_Image)
        hash_2 = imagehash.average_hash(Previous_Image)
            
        State = hash_1 == hash_2
        
        print(State)
        with open(path,"w+", encoding="utf-8") as f:
           f.write(str(State))
           f.close()
    except Exception as e:
        print(e)
        

      

    return 
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-pc', '--Path_currently',  help="Path_currently", required=True)
    parser.add_argument('-pp', '--Path_previouly',  help="Path_previouly", required=True)
    parser.add_argument('-t', '--textpath',  help="output text file ", required=True)
    
    args = parser.parse_args()
    path_currently = args.Path_currently
    path_previouly = args.Path_previouly
    text_output = args.textpath
    Image_Hash(path_currently,path_previouly,text_output)
    
main()



# python Hash_Image.py -pc "D:\\httpuokacirPrevious.png" -pp "D:\\httpsenuokacirENaspx.png" -t "D:\\hashoutput.txt"



