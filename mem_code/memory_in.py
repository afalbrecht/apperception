import shutil
import sys
import os
import pickle
from mem_code import *

# take in filename
dir = sys.argv[1]
input_name = sys.argv[2]
flag = sys.argv[3]
filename = dir + '_' + input_name

# print(recursive_traverse(tree, 'c_letter aospdifja'))
if "3" in flag:
    print("Deleting template_in file")
    os.remove(f'memory/{filename}_template_in.txt')

if "0" in flag and "3" not in flag:
    print("Using memory if possible")

    # Load in tree from JSON file
    with open('mem_code/mem_tree.pickle', 'rb') as f:
        tree = pickle.load(f)
    # data_tree = TreeNode.from_dict(data)

    # Read in sensory sequence input from input file
    with open(f'data/{dir}/{input_name}.lp', 'r') as file:
        input = file.read()

    # Parse input to isolate "senses" facts
    senses_list = parse_input(input)
    print(senses_list)
    # Retrieve essential marks from tree depending on input
    temp_dict = build_template(tree, input, senses_list)
    # print('----------------------------------------')
    # print(temp_dict)
    # print('----------------------------------------')     
    go = True

    if temp_dict["types"] != []:
        print("Using memory tree")
        template = mem_to_template(temp_dict, dir, input_name)
        print(template)
        filedata = template.splitlines(True)
        interpretation = build_interpretation(tree, temp_dict, senses_list, dir, input_name)
        print(interpretation)
        # with open(f'memory/{filename}_interpret_mem.lp', 'r') as file:
        #     interpretation = file.read()
    elif os.path.isfile(f'memory/{filename}_template_out.txt'):
        print("Using template files")
        # Read in template file
        with open(f'memory/{filename}_template_out.txt', 'r') as file:
            filedata = file.readlines()
        with open(f'memory/{filename}_interpret_mem.lp', 'r') as file:
            interpretation = file.read()
    else:
        go = False
        

    if go:
        # Replace the target string
        for i, line in enumerate(filedata):
            if 'aux' in line:
                filedata[i] = line.replace('[]', f'["{filename}_interpret_mem.lp"]')
                if not 'interpret' in filedata[i]:
                    filedata[i] = line.replace(']', f',"{filename}_interpret_mem.lp"]')

        # filedata = filedata.replace('aux_files = []', 'aux_files = ['+filename+'_interpret_mem.lp]')

        # Write the file out again
        with open(f'memory/{filename}_template_in.txt', 'w') as file:
            file.writelines(filedata)

        if "1" in flag:
            print("Using empty interpretation file")
            interpretation = ""
        
        with open(f'asp/{filename}_interpret_mem.lp', 'w') as file:
            file.write(interpretation)
        
        # shutil.copyfile(f'memory/{filename}_interpret_mem.lp', f'asp/{filename}_interpret_mem.lp')

if os.path.isfile(f'memory/{filename}_template_out.txt') and "2" in flag and "3" not in flag:
    print("Using saved template")
    # Read in the file
    with open(f'memory/{filename}_template_out.txt', 'r') as file:
        filedata = file.readlines()

    # Replace the target string
    for i, line in enumerate(filedata):
        if 'aux' in line:
            filedata[i] = line.replace('[]', f'["{filename}_interpret_mem.lp"]')
            if not 'interpret' in filedata[i]:
                filedata[i] = line.replace(']', f',"{filename}_interpret_mem.lp"]')

    # filedata = filedata.replace('aux_files = []', 'aux_files = ['+filename+'_interpret_mem.lp]')

    # Write the file out again
    with open(f'memory/{filename}_template_in.txt', 'w') as file:
        file.writelines(filedata)

    

    if "1" in flag:
        print("Using empty interpretation file")
        interpretation = ""
    else:
        with open(f'memory/{filename}_interpret_mem.lp', 'r') as file:
            interpretation = file.read()
    
    with open(f'asp/{filename}_interpret_mem.lp', 'w') as file:
            file.write(interpretation)

    # shutil.copyfile(f'memory/{filename}_interpret_mem.lp', f'asp/{filename}_interpret_mem.lp')


