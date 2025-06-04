import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"

def find_game_paths(src):
    print(src)
    print(os.path.exists(src))
    game_paths = []
    for root , dirs , files in os.walk(src) :
        for dirss in dirs:
            if GAME_DIR_PATTERN in dirss :
                path = os.path.join(src,dirss)
                game_paths.append(path)
    return game_paths
            

def main_func(src,tgt):
    cwd = os.getcwd()
    src_path = os.path.join(cwd,src)
    tgt_path = os.path.join(cwd,tgt)
    
    gamepath = find_game_paths(src_path)
    print("Source Path",src_path)
    print("Target Path",tgt_path)
    print(gamepath)

if __name__ == '__main__' :
    args = sys.argv
    #print(args)
    if len(args) > 3 :
        raise Exception('You need to give two args only One source and one Target')
    src , tgt = args[1:]
    
    print ('Source :',src)
    print ('Target :',tgt)
    
    main_func(src,tgt)