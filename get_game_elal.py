import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"
GAME_CODE_EXT = ".go"
GAME_COMPILE = ["go","build"]

def find_game_paths(src):
    print(src)
    print(os.path.exists(src))
    game_paths = []
    for root , dirs , files in os.walk(src) :
        for dirss in dirs:
            if GAME_DIR_PATTERN in dirss.lower() :
                path = os.path.join(src,dirss)
                game_paths.append(path)
    return game_paths

def cr_dir(tgt):
    if not os.path.exists(tgt) :
        os.mkdir(tgt)
        
def get_names_from_paths(path,to_strip):
    new_names = []
    for pathz in path :
        _,dir_name = os.path.split(pathz)
        new_dir_name = dir_name.replace(to_strip,"")
        new_names.append(new_dir_name)
    return new_names
      
def copy_and_replace(src,tgt):
    if os.path.exists(tgt):
        shutil.rmtree(tgt)
    shutil.copytree(src,tgt)  
    
def make_json_metadata_file(json_path,game_dirs) :
    data = {
        "Game Names" : game_dirs,
        "Number of Games" : len(game_dirs)
    }
    with open(json_path,'w') as f:
        json.dump(data,f)
        
def compile_game_code(path):
    code_file_name = None
    for roots,dirs,files in os.walk(path):
        for file in files :
            if GAME_CODE_EXT in file:
                code_file_name = file
                break
        break
    if code_file_name is None :
        return 
    command = GAME_COMPILE + [code_file_name]
    #print(command)
    run_command(command,path)
    

def run_command(cmd,path):
    cwd =  os.getcwd()
    os.chdir(path)
    result = run(cmd ,stdout=PIPE ,stdin=PIPE , universal_newlines=True ,shell=True)
    print("Compile reult :", result)
    os.chdir(cwd)
    
def main_func(src,tgt):
    cwd = os.getcwd()
    src_path = os.path.join(cwd,src)
    tgt_path = os.path.join(cwd,tgt)
    
    gamepath = find_game_paths(src_path)
    print("Source Path",src_path)
    print("Target Path",tgt_path)
    #print(gamepath)
    
    cr_dir(tgt_path)
    new_game_dirs = get_names_from_paths(gamepath,"_game")
    print(new_game_dirs)
    
    for src,tgt in zip(gamepath,new_game_dirs):
        dest_path = os.path.join(tgt_path,tgt)
        copy_and_replace(src,dest_path)
        compile_game_code(dest_path)
        #print(dest_path)
    
    json_path = os.path.join(tgt_path,"metadata.json")
    make_json_metadata_file (json_path,new_game_dirs)
    

if __name__ == '__main__' :
    args = sys.argv
    #print(args)
    if len(args) > 3 :
        raise Exception('You need to give two args only One source and one Target')
    src , tgt = args[1:]
    
    print ('Source :',src)
    print ('Target :',tgt)
    
    main_func(src,tgt)
